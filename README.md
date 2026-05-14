# Lumentree Inverter HASS

Fork of [`ngoviet/lumentreeHA`](https://github.com/ngoviet/lumentreeHA) for testing and improving support for Lumentree inverters in Home Assistant.

The Home Assistant integration domain is still `lumentree` so existing entities and config entries can continue to work.

## Changes In This Fork

- Renamed the integration display name to **Lumentree Inverter HASS**.
- Fixed Home Assistant 2025.11 coordinator lifecycle warning by replacing delayed `async_config_entry_first_refresh()` calls with normal refresh calls.
- Reduced noisy warnings from empty/unsupported battery-cell MQTT responses.
- Exposed full raw MQTT payload data in the **Last Raw MQTT Hex** entity attributes.
- Added a disabled-by-default diagnostic entity: **Raw MQTT Registers**.
- Decoded all 95 realtime MQTT registers into diagnostic attributes:
  - `register_hex`
  - `register_uint`
  - `register_int`
  - `named_registers`
  - `request_hex`
  - `response_hex`
  - `crc_ok`
- Fixed `AC Input Power` parsing to read register `53` as signed instead of unsigned.
- Added `tools/lumentree_api_probe.py` for dumping raw Lumentree cloud API JSON.

## Install With HACS

1. Open HACS.
2. Go to **Integrations**.
3. Add custom repository:

   ```text
   https://github.com/nlkcodenew/LumentreeHASS
   ```

4. Select category **Integration**.
5. Install **Lumentree Inverter HASS**.
6. Restart Home Assistant.

## Diagnostic Notes

The **Raw MQTT Registers** entity is disabled by default. Enable it from Home Assistant entity settings when debugging register mappings.

The **Last Raw MQTT Hex** entity keeps a short state preview, but this fork stores the full MQTT payload in attributes so it can be read through the Home Assistant API.

## Upstream

Original project: [`ngoviet/lumentreeHA`](https://github.com/ngoviet/lumentreeHA)

This fork is experimental and focused on debugging Lumentree 6 kW inverter MQTT/API data.
