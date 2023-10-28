import requests
import argparse
import json
import ipaddress
import logging

API_URL = 'http://ip-api.com/json/'

def get_public_ip_info(ip):
    try:
        ipaddress.IPv4Address(ip)  # Validate the IP address
    except ipaddress.AddressValueError:
        raise InvalidIPAddressError(f"Invalid IP address: {ip}")

    try:
        response = requests.get(API_URL + ip)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        raise RequestError(f"Request Error: {e}")
    except requests.exceptions.HTTPError as e:
        raise HTTPError(f"HTTP Error: {e}")
    except json.JSONDecodeError as e:
        raise JSONParsingError(f"JSON Parsing Error: {e}")


if __name__ == "__main__":
    logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

    parser = argparse.ArgumentParser(description="Get information about a public IP address.")
    parser.add_argument("ip", help="Public IP address to lookup")
    args = parser.parse_args()

    try:
        ip_info = get_public_ip_info(args.ip)
        if ip_info:
            print(f"Public IPv4 Address: {ip_info['query']}")
            print(f"ISP: {ip_info['isp']}")
            print(f"Organization: {ip_info['org']}")
            print(f"Timezone: {ip_info['timezone']}")
            print(f"Location: {ip_info['city']}, {ip_info['country']}")
            print(f"Country Code: {ip_info['countryCode']}")
            print(f"Region: {ip_info['regionName']}")
            print(f"City: {ip_info['city']}")
    except (InvalidIPAddressError, RequestError, HTTPError, JSONParsingError) as e:
        logging.error(e)
        print(f"An error occurred. Check the error_log.txt file for details.")