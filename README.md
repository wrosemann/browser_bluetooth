# Bluetooth Scanner Web Application

A modern web application for scanning Bluetooth devices and capturing advertisement data directly from your browser.

## Features

- 🔍 **Real-time Bluetooth scanning** - Scan for nearby Bluetooth devices
- 📱 **Device discovery** - Discover and display device information
- 🔧 **Advanced filtering** - Filter devices by name or advertisement data
- 📊 **Live statistics** - Track total devices, filtered devices, and scan time
- 🎨 **Modern UI** - Beautiful, responsive design with smooth animations
- ⚙️ **Configurable settings** - Customize scan duration and display options

## Files

- `index.html` - **Default BLE Advertisement Scanner** - Scans for BLE advertisements without pairing
- `basic-scanner.html` - Basic Bluetooth scanner with simulated device discovery
- `bluetooth-scanner.html` - Advanced scanner with more features and real Web Bluetooth API integration

## Browser Requirements

This application requires a browser that supports the Web Bluetooth API:

- **Chrome** (version 56+) - Full support
- **Edge** (version 79+) - Full support
- **Opera** (version 43+) - Full support

**Note**: Firefox and Safari do not currently support the Web Bluetooth API.

## Usage

### BLE Advertisement Scanner (`index.html`) - **Default**

1. Open `index.html` in a supported browser
2. Click "Start BLE Scan" to begin scanning for advertisements
3. Use the filter inputs to narrow down results:
   - **Name Filter**: Filter devices by their name (supports `*` wildcards, e.g. `iPhone*`)
   - **Data Filter**: Filter devices by advertisement data content (supports `*` wildcards)
4. Toggle "Show all devices" to display unfiltered results
5. Click "Stop Scan" to end the scanning process
6. Use "Clear Results" to reset the device list

**Wildcard Filtering**: Use `*` as a wildcard character:
- `iPhone*` matches "iPhone 13", "iPhone 14", etc.
- `*Galaxy*` matches "Samsung Galaxy", "Galaxy Tab", etc.
- `*BLE*` matches any device name containing "BLE"

### Advanced Scanner (`bluetooth-scanner.html`)

1. Open `bluetooth-scanner.html` in a supported browser
2. Configure scan settings:
   - **Scan Duration**: Set how long to scan (1-60 seconds)
   - **Allow Duplicates**: Choose whether to show duplicate devices
   - **Show Services**: Display discovered Bluetooth services
3. Set up filters in the Filter Settings section
4. Click "Start Scan" and grant Bluetooth permissions when prompted
5. Monitor the live statistics and discovered devices
6. Use the controls to stop scanning or clear results

## Features Explained

### Device Information Displayed

- **Device Name**: The friendly name of the Bluetooth device
- **Device ID**: Unique identifier for the device
- **RSSI**: Signal strength indicator (in dBm)
- **Advertisement Data**: Raw advertisement data in hexadecimal format
- **Services**: Discovered Bluetooth services (if enabled)

### Filtering Options

- **Name Filter**: Search for devices by their name with wildcard support (case-insensitive)
  - Use `*` as wildcard: `iPhone*`, `*Galaxy*`, `*BLE*`
- **Data Filter**: Search within the advertisement data with wildcard support (case-insensitive)
- **Show All Devices**: When unchecked, only shows devices matching filters

### Scan Settings

- **Scan Duration**: How long to scan for devices (1-60 seconds)
- **Allow Duplicates**: Whether to show the same device multiple times
- **Show Services**: Display discovered Bluetooth services as tags

## Technical Details

### Web Bluetooth API

The application uses the Web Bluetooth API to:

1. **Request Device Access**: Prompt user for Bluetooth permissions
2. **Connect to Devices**: Establish connections to discovered devices
3. **Read Characteristics**: Access device information and services
4. **Capture Advertisement Data**: Extract and display advertisement packets

### Advertisement Data Format

Advertisement data is displayed in hexadecimal format, which typically includes:

- **Flags**: Device capabilities and connection state
- **Service UUIDs**: Available Bluetooth services
- **Manufacturer Data**: Vendor-specific information
- **Device Name**: Human-readable device name

### Browser Permissions

When you start a scan, the browser will:

1. Request permission to access Bluetooth
2. Show a device selection dialog
3. Connect to the selected device
4. Begin scanning for additional devices

## Troubleshooting

### Common Issues

1. **"Bluetooth is not supported"**
   - Use Chrome, Edge, or Opera
   - Ensure you're using HTTPS (required for Web Bluetooth)

2. **"No Bluetooth devices found"**
   - Make sure Bluetooth is enabled on your device
   - Ensure there are Bluetooth devices nearby
   - Check that devices are in discoverable mode

3. **Permission denied**
   - Click "Allow" when prompted for Bluetooth access
   - Refresh the page and try again

4. **No devices appearing**
   - Check that your Bluetooth devices are discoverable
   - Try increasing the scan duration
   - Clear any filters that might be hiding devices

### Development Notes

- The application includes simulated device discovery for demonstration purposes
- Real Bluetooth scanning requires user interaction and device selection
- Advertisement data format may vary between devices and manufacturers
- Some devices may not broadcast all information due to privacy settings

## Browser Compatibility

| Browser | Version | Support |
|---------|---------|---------|
| Chrome | 56+ | ✅ Full |
| Edge | 79+ | ✅ Full |
| Opera | 43+ | ✅ Full |
| Firefox | Any | ❌ Not supported |
| Safari | Any | ❌ Not supported |

## Security Considerations

- Web Bluetooth API requires HTTPS
- User must explicitly grant permission
- Only works with user interaction (no background scanning)
- Device selection is always user-controlled

## Future Enhancements

- Support for specific device types (heart rate monitors, etc.)
- Export scan results to CSV/JSON
- Real-time signal strength monitoring
- Connection to discovered devices
- Custom advertisement data parsing

## License

This project is open source and available under the MIT License. 