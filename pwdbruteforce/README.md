# pwdbruteforce

This simple script takes the dictionary file and the login page defined as a global variables in order to brute force and try to 
find the correct password through POST requests.

## Set up

You'll need to have installed python3 in your machine to run the script.

You'll have to update the 2 global variables: `login_url` the url you want to attemp the requests to and 
`dictionary_path` is the file which contains the passwords you want to use for the brute-force attack.
Additionally, the `post_data` variable within `bruteForcePassword` function corresponds to the login fields of the login page and 
it has to be changed if they're different from `email` and `password`.
```python
# Global variables
# to be changed
login_url = "http://your-domain.com/login"
dictionary_path = "/usr/share/wordlists/rockyou_utf.txt"

# function
def bruteForcePassword():

    post_data = {
      'email': 'admin',
      'password': passw
    }

```

## Output Example

```
Brute Forcing:   1%|█                                                                             | 111971/14344392 [01:21<2:53:43, 1365.39it/s]

[!] Password found! 
Credentials: admin:123456
```
