import requests

API_URL = f'http://ip-api.com/json/192.168.68.114'

def get_public_ip_info():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return None

if __name__ == "__main__":
    ip_info = get_public_ip_info()
    if ip_info:
        print(f"Public IPv4 Address: {ip_info['query']}")
        print(f"ISP: {ip_info['isp']}")
        print(f"Organization: {ip_info['org']}")
        print(f"Timezone: {ip_info['timezone']}")
        print(f"Location: {ip_info['city']}, {ip_info['country']}")
        print(f"Country Code: {ip_info['countryCode']}")
        print(f"Region: {ip_info['regionName']}")
        print(f"City: {ip_info['city']}")