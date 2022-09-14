# pwddumpstatscrack

This script takes a `.csv` file defined in `usersPathFile` global variable 
that was previously dumped from a database. 
It reads the file and gets the `user_name` and `user_password` fields 
discarding the empty passwords to finally create 
a list with all the valid records. When done, it shows the initial stats 
of the obtained records.Additionally, it checks 
if there's any repeated passwords and stores them in a new list. 

Once the initial analysis is finished, the user has to type y/n and press 
Enter in order to start the process of trying to crack the passwords by 
using 
[Hashcat](https://hashcat.net/hashcat0) tool. Firstly, this task starts 
with the repeated passwords since there's a higher 
probability of them using a default or easy one. Lastly, the process ends 
with the list of unique passwords and prints the
results of the program.

## Set up

You'll need to have installed python3 in your machine to run the script.

You'll have to update the global variables listed below. `usersPathFile` 
corresponds to the path of the .csv file with the users' records. 
`dictionaryList`
stores the path of the file that you want to use as a dictionary with 
Hashcat for cracking the passwords - the bigger this file is the longer 
it'll take
to finalise the process. Lastly, `hashcatHashMode` is the number related 
to type of hash of the passwords - run the command `hashcat -h` to see the 
different modes.
You can also change the variables for storing the generated files with a 
different name.
```python
usersPathFile = 'company_users.csv' 
dictionaryList = '/usr/share/wordlists/john.lst'
hashcatHashMode = 3200 
```

Hashcat is run by using the correspondent global variables such as the 
names of the output files and hash mode. With their values, it will be 
something 
as follows:
```bash
$ hashcat -m 3200 -a 0 file_with_unique_passwords.txt 
/usr/share/wordlists/john.lst -o cracked_unique_passwords.txt
```

## Output Example

* Initial stats

```
**** Initial file stats:
Total of records in file: 7032.
Users with empty password: 752.
--> Final number of records to analise: 6280.

**** Checking duplicate passwords...
2 duplicate passwords have been found!
--> Password [ 
$2a$10$EKrNWQS/yAOVdXUeI2pn7er3.jbwlLHFI5Yb2KeW6PCA0YSS/ZXUa ] is 
duplicate 2 times and used by [ peter, jasmine ] usernames.
--> Password [ 
$2a$10$dhzRkka10e4WgIlQx.VHfOYlF1cefOOd96WHEmevvQsJs8PIgjchO ] is 
duplicate 3 times and used by [ john, test, charles ] usernames.
```

* User confirmation to start cracking

```
The file "company_users.csv" has been analised succesfully. Would you like 
to crack the passwords using Hashcat? (type y/n and press Enter):
```

* Passwords files creation

```
**** Creating passwords files for cracking...
File with 2 repeated passwords has been successfully created --> 
"file_with_repeated_passwords.txt"
File with 6275 unique passwords has been successfully created --> 
"file_with_unique_passwords.txt"
```

* User confirmation to crack the repeated passwords

```
Firstly, I will crack the repeated passwords due to a higher probability 
of them using a default or easy one.
If you want to continue please, press Enter.
```

* User confirmation to crack the unique passwords

```
There is a total of 6275 unique passwords in 
"file_with_unique_passwords.txt". Please be aware this process can take a 
long time to complete.
If you want to continue please, press Enter. 
```

* Final stats

````
**** Final stats:
--> 1/2 repeated passwords were cracked.
--> 8/6275 unique passwords were cracked.
```
