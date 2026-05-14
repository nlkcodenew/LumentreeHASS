# Lumentree Inverter HASS

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub release](https://img.shields.io/github/release/nlkcodenew/LumentreeHASS.svg)](https://github.com/nlkcodenew/LumentreeHASS/releases)
[![GitHub stars](https://img.shields.io/github/stars/nlkcodenew/LumentreeHASS.svg)](https://github.com/nlkcodenew/LumentreeHASS/stargazers)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-ffdd00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/ngoviet)

<a href="https://my.home-assistant.io/redirect/hacs_repository/?owner=nlkcodenew&repository=LumentreeHASS&category=integration" class="my badge" target="_blank"><img src="https://my.home-assistant.io/badges/hacs_repository.svg" alt="Open this repository in HACS" width="200" height="36"></a>

A high-performance Home Assistant integration for Lumentree solar inverters with real-time MQTT data and daily statistics via HTTP API.

## 📸 Screenshots

### Sensors Overview
![Sensors Entity Overview](images/sensors_entity_overview.jpg)

### Dashboard - Energy Charts (24h)
![Dashboard Energy Charts 24h](images/dashboard_energy_charts_24h.jpg)

### Dashboard - Statistics Summary
![Dashboard Statistics Summary](images/dashboard_statistics_summary.jpg)

## ✨ Features

### 🔄 Real-time Data (MQTT)
- **PV Power**: Solar generation power
- **Battery Management**: Power, voltage, current, SOC, status
- **Grid Power**: Import/export power and status
- **Load Power**: Consumption monitoring
- **AC Output**: Voltage, frequency, power, apparent power
- **Device Status**: Temperature, online status, UPS mode
- **Battery Cells**: Individual cell voltage monitoring

### 📊 Daily Statistics (HTTP API)
- **PV Generation**: Daily solar production
- **Battery Charge/Discharge**: Daily energy flow
- **Grid Import**: Daily grid consumption
- **Load Consumption**: Daily energy usage

### 📈 Advanced Statistics (v4.0.0)

#### Monthly Statistics
- **PV Generation Month**: Current month's solar production (kWh)
- **Grid Import Month**: Current month's grid consumption (kWh)
- **Load Consumption Month**: Current month's load usage (kWh)
- **Battery Charge/Discharge Month**: Current month's battery energy flow (kWh)
- **Energy Saved Month**: Current month's energy savings (kWh)
- **Cost Savings Month**: Current month's cost savings (VND)

#### Yearly Statistics
- **PV Generation Year**: Current year's solar production (kWh)
- **Grid Import Year**: Current year's grid consumption (kWh)
- **Load Consumption Year**: Current year's load usage (kWh)
- **Battery Charge/Discharge Year**: Current year's battery energy flow (kWh)
- **Energy Saved Year**: Current year's energy savings (kWh)
- **Cost Savings Year**: Current year's cost savings (VND)
- **Monthly Arrays**: 12-month breakdown arrays for charting and visualization

#### Total/Lifetime Statistics
- **PV Generation Total**: Lifetime solar production (kWh)
- **Grid Import Total**: Lifetime grid consumption (kWh)
- **Load Consumption Total**: Lifetime load usage (kWh)
- **Battery Charge/Discharge Total**: Lifetime battery energy flow (kWh)
- **Energy Saved Total**: Lifetime energy savings (kWh)
- **Cost Savings Total**: Lifetime cost savings (VND)

**Statistics Features:**
- Automatic aggregation from daily data
- Cache-based computation for performance
- Monthly arrays for advanced dashboard visualization
- Automatic period finalization when months/years change
- Historical data support across multiple years

### 🚀 Performance Optimizations (v4.0.0)
- **40-50% faster parsing** with struct caching
- **3x faster API calls** with concurrent requests
- **20-30% memory reduction** with `__slots__`
- **Professional architecture** with clean separation of concerns
- **English documentation** for international community

## 📋 Requirements

- **Home Assistant**: 2023.1 or later
- **Python**: 3.9 or later
- **Dependencies**: aiohttp>=3.8.0, paho-mqtt>=1.6.0, crcmod>=1.7
- **Network**: Internet connection for API calls, MQTT access

## 🛠️ Installation

### Option 1: HACS (Recommended)

1. Open **HACS** in Home Assistant
2. Go to **Integrations**
3. Click **Custom Repositories**
4. Add repository: `https://github.com/nlkcodenew/LumentreeHASS`
5. Select **Integration** category
6. Install **Lumentree Inverter HASS**
7. Restart Home Assistant

### Option 2: Manual Installation

1. Download the [latest release](https://github.com/nlkcodenew/LumentreeHASS/releases)
2. Extract to `custom_components/lumentree/` in your Home Assistant config
3. Restart Home Assistant

## ⚙️ Configuration

### Adding the Integration

1. Go to **Configuration** → **Integrations**
2. Click **Add Integration**
3. Search for **Lumentree Inverter HASS**
4. Enter your **Device ID** (found on device label or mobile app)
5. Follow the setup wizard
6. Confirm device information

### Device ID

The Device ID is typically:
- **Format**: `H240909079` (H + 9 digits)
- **Location**: Device label or Lumentree mobile app
- **Example**: `H240909079`, `H240909080`, etc.

## 📊 Available Entities

### Sensors

#### Power & Energy
- **PV Power**: Current solar generation (W)
- **Battery Power**: Battery power (W), positive = Charging, negative = Discharging
- **Grid Power**: Grid import/export power (W)
- **Load Power**: Current load consumption (W)
- **AC Output Power**: Inverter output power (W)
- **AC Input Power**: Grid input power (W)
- **Total Load Power**: Calculated total load (W)

#### Voltage & Current
- **Battery Voltage**: Battery pack voltage (V)
- **Battery Current**: Battery current (A), positive = Charging, negative = Discharging
- **AC Output Voltage**: Inverter output voltage (V)
- **Grid Voltage**: Grid voltage (V)
- **AC Input Voltage**: Grid input voltage (V)
- **PV1/PV2 Voltage**: Solar panel voltages (V)

#### Frequency & Temperature
- **AC Output Frequency**: Inverter frequency (Hz)
- **AC Input Frequency**: Grid frequency (Hz)
- **Device Temperature**: Inverter temperature (°C)

#### Status & Information
- **Battery SOC**: State of charge (%)
- **Battery Status**: Charging/Discharging
- **Grid Status**: Importing/Exporting
- **Battery Type**: Battery type information
- **Master/Slave Status**: System status
- **Device SN (MQTT)**: Device serial number

#### Daily Statistics
- **PV Generation Today**: Daily solar production (kWh)
- **Battery Charge Today**: Daily charge energy (kWh)
- **Battery Discharge Today**: Daily discharge energy (kWh)
- **Grid Input Today**: Daily grid consumption (kWh)
- **Load Consumption Today**: Daily load usage (kWh)

### Binary Sensors

- **Online Status**: Device connectivity status
- **UPS Mode**: Uninterruptible power supply mode

## 🔧 Advanced Configuration

### Polling Intervals

- **MQTT Data**: 5 seconds (configurable)
- **Daily Statistics**: 10 minutes (configurable)

### Error Handling

The integration includes robust error handling:
- **Automatic reconnection** for MQTT
- **Retry logic** for API calls
- **Graceful degradation** on errors

## 📈 Performance

### v4.0.0 Improvements

- **Parser Speed**: 40-50% faster with struct caching
- **API Calls**: 3x faster with concurrent requests
- **Memory Usage**: 20-30% reduction with `__slots__`
- **Startup Time**: 15-20% faster without fallback overhead
- **Code Size**: 30-40% reduction

### Resource Usage

- **Memory**: ~20-30% lower than v2.x
- **CPU**: ~10-15% lower usage
- **Network**: Optimized batch updates

## 🐛 Troubleshooting

### Common Issues

#### Integration Not Found
- Restart Home Assistant
- Clear browser cache
- Check HACS cache

#### Authentication Failed
- Verify Device ID is correct
- Check network connection
- Try again in a few minutes

#### No Data Updates
- Check MQTT connection
- Verify device is online
- Check Home Assistant logs

#### Missing Entities
- Restart Home Assistant
- Check entity registry
- Re-add integration if needed

### Log Analysis

Check logs for these patterns:

```bash
# Good - Integration working
INFO [custom_components.lumentree] Setting up Lumentree: Device Name
INFO [custom_components.lumentree] MQTT connected successfully

# Warning - Non-critical issues
WARNING [custom_components.lumentree] HTTP Token missing for H240909079

# Error - Needs attention
ERROR [custom_components.lumentree] Authentication failed
ERROR [custom_components.lumentree] MQTT connection failed
```

### Debug Mode

Enable debug logging:

```yaml
logger:
  logs:
    custom_components.lumentree: debug
    paho: debug
```

## 🔄 Migration from v2.x

**Important**: v5.0.0 includes major improvements and fixes. Existing configurations remain valid. No migration steps required.

## 📝 Changelog

### v5.0.0 (Latest)

**Major Improvements:**
- Fixed savings calculation for monthly/yearly statistics
- Improved dashboard templates with direct calculations (no longer dependent on separate sensor entities)
- Enhanced error handling and data validation
- Code optimization and performance improvements
- Cleaned up internal documentation files

**Bug Fixes:**
- Fixed monthly/yearly savings showing 0.0 when total_load was positive
- Improved calculation logic to ensure saved_kwh and savings_vnd are correctly computed
- Enhanced API response validation
- Fixed dashboard display issues for savings data

**Technical Improvements:**
- Optimized cache recomputation logic
- Improved date parsing and validation
- Enhanced input validation for API calls
- Better error context in logs

### v4.0.0

- Major statistics enhancements
- Monthly and yearly statistics with daily arrays
- Lifetime/total statistics aggregation
- Performance optimizations

## 📁 Architecture

### v5.0.0 Structure

```
custom_components/lumentree/
├── __init__.py                 # Integration entry point
├── manifest.json               # v5.0.0 metadata
├── const.py                    # Constants
├── config_flow.py              # Configuration flow
├── strings.json                # UI strings
├── core/                       # Core business logic
│   ├── api_client.py          # HTTP API client
│   ├── mqtt_client.py         # MQTT client
│   ├── modbus_parser.py       # Modbus parser
│   └── exceptions.py          # Custom exceptions
├── coordinators/               # Data coordinators
│   ├── daily_coordinator.py   # Daily stats
│   ├── monthly_coordinator.py # Monthly stats
│   ├── yearly_coordinator.py  # Yearly stats
│   ├── total_coordinator.py   # Total/lifetime stats
│   └── stats_coordinator.py   # Legacy stats
├── entities/                   # Entity implementations
│   ├── sensor.py              # Sensor entities
│   ├── binary_sensor.py       # Binary sensors
│   └── base_entity.py         # Base entity class
└── models/                     # Data models
    ├── device_info.py         # Device info model
    └── sensor_data.py         # Sensor data model
```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Lumentree**: For providing the API and MQTT access
- **Home Assistant Community**: For support and feedback
- **HACS**: For easy installation and updates

## 📞 Support

- **GitHub Issues**: [Report problems](https://github.com/nlkcodenew/LumentreeHASS/issues)
- **Discussions**: [Community discussions](https://github.com/nlkcodenew/LumentreeHASS/discussions)
- **Documentation**: [Full documentation](https://github.com/nlkcodenew/LumentreeHASS)
- **☕ Buy Me A Coffee**: [Support this project](https://buymeacoffee.com/ngoviet)

## 📊 Changelog

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

---

**Made with ❤️ for the Home Assistant community**
