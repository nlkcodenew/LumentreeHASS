#!/usr/bin/env python3
"""Probe Lumentree cloud API and print raw JSON responses.

Usage:
    python3 tools/lumentree_api_probe.py --device-id DEVICE_ID
    python3 tools/lumentree_api_probe.py --device-id DEVICE_ID --date 2026-05-14 --year 2026 --month 5
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request
from datetime import date
from typing import Any


BASE_URL = "http://lesvr.suntcn.com"
HEADERS = {
    "versionCode": "1.6.3",
    "deviceType": "1",
    "platform": "2",
    "wifiStatus": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36",
    "Accept": "application/json, text/plain, */*",
}


def request_json(
    method: str,
    path: str,
    *,
    params: dict[str, Any] | None = None,
    data: dict[str, Any] | None = None,
    token: str | None = None,
) -> dict[str, Any]:
    url = f"{BASE_URL}{path}"
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"

    body = None
    headers = dict(HEADERS)
    if token:
        headers["Authorization"] = token
    if data:
        body = urllib.parse.urlencode(data).encode()
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def authenticate(device_id: str) -> str:
    server_time_resp = request_json("GET", "/lesvr/getServerTime")
    server_time = server_time_resp.get("data", {}).get("serverTime")
    if not server_time:
        raise RuntimeError(f"Missing serverTime: {server_time_resp}")

    token_resp = request_json(
        "POST",
        "/lesvr/shareDevices",
        data={"deviceIds": device_id, "serverTime": str(server_time)},
    )
    token = token_resp.get("data", {}).get("token")
    if not token:
        raise RuntimeError(f"Missing token: {token_resp}")
    return token


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device-id", required=True)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--year", type=int, default=date.today().year)
    parser.add_argument("--month", type=int, default=date.today().month)
    args = parser.parse_args()

    token = authenticate(args.device_id)
    probes = {
        "deviceManage": (
            "POST",
            "/lesvr/deviceManage",
            {"page": "1", "snName": args.device_id},
        ),
        "getPVDayData": (
            "GET",
            "/lesvr/getPVDayData",
            {"deviceId": args.device_id, "queryDate": args.date},
        ),
        "getBatDayData": (
            "GET",
            "/lesvr/getBatDayData",
            {"deviceId": args.device_id, "queryDate": args.date},
        ),
        "getOtherDayData": (
            "GET",
            "/lesvr/getOtherDayData",
            {"deviceId": args.device_id, "queryDate": args.date},
        ),
        "getMonthData": (
            "GET",
            "/lesvr/getMonthData",
            {"deviceId": args.device_id, "year": args.year, "month": args.month},
        ),
        "getYearData": (
            "GET",
            "/lesvr/getYearData",
            {"deviceId": args.device_id, "year": args.year},
        ),
    }

    for name, (method, path, params) in probes.items():
        print(f"\n===== {name} =====")
        try:
            result = request_json(method, path, params=params, token=token)
            print(json.dumps(result, indent=2, ensure_ascii=False))
        except Exception as exc:
            print(f"ERROR: {exc}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
