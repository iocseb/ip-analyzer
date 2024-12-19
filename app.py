from flask import Flask, request, render_template
import requests
import user_agents
import ipaddress

app = Flask(__name__)

def is_private_ip(ip):
    try:
        ip_addr = ipaddress.ip_address(ip)
        return ip_addr.is_private or ip_addr.is_loopback
    except ValueError:
        return False

@app.route('/')
def index():
    # Override IP for testing
    ip = "135.180.150.115"
    
    # The following code is now skipped for testing
    # if request.headers.get('X-Forwarded-For'):
    #     ip = request.headers.get('X-Forwarded-For').split(',')[0]
    # else:
    #     ip = request.remote_addr
    
    # Parse user agent
    user_agent = str(request.user_agent)
    ua_parser = user_agents.parse(user_agent)
    
    # Check IP type and get geolocation data
    if is_private_ip(ip):
        geo_data = {
            "info": "This is a private/local IP address. Geolocation is not available.",
            "city": "Local Network",
            "region": "N/A",
            "country": "Local Network",
            "lat": "N/A",
            "lon": "N/A",
            "isp": "Local Network",
            "as": "N/A"
        }
    else:
        # Get geolocation data for public IPs using ip-api.com
        try:
            geo_response = requests.get(f'http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,lat,lon,isp,as')
            geo_data = geo_response.json()
            
            # Check for ip-api.com error responses
            if geo_data.get('status') == 'fail':
                geo_data = {
                    "error": f"API Error: {geo_data.get('message', 'Unknown error')}",
                    "city": "N/A",
                    "region": "N/A",
                    "country": "N/A",
                    "lat": "N/A",
                    "lon": "N/A",
                    "isp": "N/A",
                    "as": "N/A"
                }
        except Exception as e:
            geo_data = {
                "error": f"Failed to fetch geolocation data: {str(e)}",
                "city": "N/A",
                "region": "N/A",
                "country": "N/A",
                "lat": "N/A",
                "lon": "N/A",
                "isp": "N/A",
                "as": "N/A"
            }
    
    # Get all headers
    headers = dict(request.headers)
    
    return render_template('index.html',
                         ip=ip,
                         user_agent=user_agent,
                         ua_details=ua_parser,
                         geo_data=geo_data,
                         headers=headers)

if __name__ == '__main__':
    app.run(debug=True) 