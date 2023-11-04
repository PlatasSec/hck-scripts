# ssrf_check_ip_backend

This script checks the correct IP address within an IP subnet and port. It's used to verify the backend system hosting a web application that's not externally accessible. It loops through the 255 possible values and prints the result for a 200 response status code.

## Setup

You'll need to have Python 3 installed on your machine to run the script.

You must update the global variables listed below to target the desired `SUBNET` with its corresponding internal `PORT`. Additionally, adjust the URL and endpoint in `response` for the POST request.

```python
SUBNET = "192.168.0."
PORT = "8080"
response = requests.post("https://0af7002c03eee20d80ed442f0063009a.web-security-academy.net/product/stock", data=post_data)
```

## Output Example

```bash
IP Address 192.168.0.106 returned HTTP 200 (OK)
```
