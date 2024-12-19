# Browser Information Display

A Flask-based web application that provides detailed information about the client's browser, including IP geolocation, user agent details, and request headers. The application features a clean, responsive interface with both light and dark mode support.

## Features

- **IP Address Information**
  - Displays client IP address with one-click copy functionality
  - Shows detailed geolocation data including city, region, and country
  - Provides ISP and ASN (Autonomous System Number) information
  - Special handling for private/local IP addresses

- **Browser & System Details**
  - Comprehensive user agent information
  - Browser type and version
  - Operating system details
  - Device type detection (PC, mobile, tablet)

- **Request Headers**
  - Complete list of HTTP request headers
  - Organized in an easy-to-read format

- **User Interface**
  - Clean, modern design
  - Dark/Light mode toggle with system preference detection
  - Responsive layout
  - Smooth transitions and animations
  - Tooltip-enhanced interactions

## Installation / Usage

1. Clone the repository: 

```bash
git clone https://github.com/iocseb/ip-analyzer
cd ip-analyzer
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Access the application:

Open your web browser and navigate to `http://localhost:5000`.

## API Dependencies

The application uses the following external API:
- [ip-api.com](https://ip-api.com/) for IP geolocation data (free tier: 45 requests per minute)

## Technical Details

- **Framework**: Flask 3.0.0
- **Python Version**: 3.8+
- **Key Dependencies**:
  - `flask`: Web framework
  - `requests`: HTTP library for API calls
  - `user-agents`: User agent string parser

## Browser Compatibility

- Chrome 60+
- Firefox 60+
- Safari 12+
- Edge 79+
- Opera 47+

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [ip-api.com](https://ip-api.com/) for providing the geolocation API
- [user-agents](https://github.com/selwin/python-user-agents) for user agent parsing
