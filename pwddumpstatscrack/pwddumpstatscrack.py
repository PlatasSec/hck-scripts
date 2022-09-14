#!/usr/bin/env python3

import csv
import pandas as pd
import os
import subprocess

# files to read and check
usersPathFile = 'company_users.csv' # the users file dumped from database to analise and cracking
fileWithRepeatedPass = 'file_with_repeated_passwords.txt' # file name to store the repeated passwords found
fileWithUniquePass = 'file_with_unique_passwords.txt' # file name to store unique the passwords found
dictionaryList = '/usr/share/wordlists/john.lst' # path to the passwords dictionary
outputFileWithRepeatedCrackedPass = 'cracked_repeated_passwords.txt' # file name to store the cracked repeated passwords
outputFileWithUniqueCrackedPass = 'cracked_all_passwords.txt' # file name to store the unique the cracked passwords
hashcatHashMode = 3200  # run hashcat -h and find the proper hash of your passwords, this example is "bcrypt $2*$, Blowfish (Unix)"

# Users arrays
finalUniqueUsersRecords = []  # Users in file without blank/empty password
userRepeatedPass = []  # Users with the same password -> [{password, [usernames]}]

# Counter
totalFileRecords = 0  # Total number of users in file

def getUsersWithSamePassword():
    print('\n**** Checking duplicate passwords...')
    global userRepeatedPass, finalUniqueUsersRecords

    # Creating a DataFrame object
    df = pd.DataFrame(finalUniqueUsersRecords,
                      columns=['username', 'password'])

    # duplicate passwords, grouped by password column
    userRepeatedPass = df[df.duplicated(subset=['password'], keep=False)].groupby(
        ['password']).agg(list).reset_index().values.tolist()

    if len(userRepeatedPass) > 0:
        # Remove repeated passwords from the unique list 
        # to improve performance and avoid extra iterations
        finalUniqueUsersRecords = df.drop_duplicates(subset=["password"], keep=False).groupby(
            ['password']).agg(list).reset_index().values.tolist()
        return True
    else:
        return False

def createFilesForCracking():
        print('\n**** Creating passwords files for cracking...')

        with open(fileWithRepeatedPass, 'w') as newFileRepeated:
            for record in userRepeatedPass:
                newFileRepeated.write("%s\n" % record[0])
            print('File with %i repeated passwords has been successfully created --> "%s"' % (len(userRepeatedPass),fileWithRepeatedPass))

        with open(fileWithUniquePass, 'w') as newFileUnique:
            for record in finalUniqueUsersRecords:
                newFileUnique.write("%s\n" % record[0])
            print('File with %i unique passwords has been successfully created --> "%s' % (len(finalUniqueUsersRecords),fileWithUniquePass))

def printFinalStats():
    print("\n**** Final stats:")

    if os.path.exists(outputFileWithRepeatedCrackedPass):
            with open(outputFileWithRepeatedCrackedPass, 'r') as file:
                passwordsCracked = len(file.readlines())
                print('--> %i/%i repeated passwords were cracked.' % len(userRepeatedPass))
                if passwordsCracked > 0:
                    print('Check the results in "%s".'%(outputFileWithRepeatedCrackedPass))
    else:
        print('--> 0/%i repeated passwords were cracked.' % len(userRepeatedPass))

    if os.path.exists(outputFileWithUniqueCrackedPass):
        with open(outputFileWithUniqueCrackedPass, 'r') as file:
            passwordsCracked = len(file.readlines())
            print('--> %i/%i unique passwords were cracked.' % len(finalUniqueUsersRecords))
            if passwordsCracked > 0:
                print('Check the results in "%s".'%(outputFileWithUniqueCrackedPass))
    else:
        print('--> 0/%i unique passwords were cracked.' % len(finalUniqueUsersRecords))

def crackRepeatedPasswords():
    print("\n**** Cracking the repeated passwords...")

    subprocess.run(["hashcat", "-m", str(hashcatHashMode), "-a", "0",
                                fileWithRepeatedPass, dictionaryList, "-o", outputFileWithRepeatedCrackedPass])
    print("\n")
    if os.path.exists(outputFileWithRepeatedCrackedPass):
        with open(outputFileWithRepeatedCrackedPass, 'r') as file:
            passwordsCracked = len(file.readlines())
            if passwordsCracked > 0:
                print("--> A total of %i repeated passwords have been cracked successfully. Check the results in %s."%(len(file.readlines()),outputFileWithRepeatedCrackedPass))
            else:
                print("--> No repeated passwords were cracked.")
    else:
        print("--> No repeated passwords were cracked.")

def crackUniquePasswords():
        print("\n**** Cracking the unique passwords...")

        subprocess.run(["hashcat", "-m", str(hashcatHashMode), "-a", "0",
                                fileWithUniquePass, dictionaryList, "-o", outputFileWithUniqueCrackedPass])

        print("\n")
        if os.path.exists(outputFileWithUniqueCrackedPass):
            with open(outputFileWithUniqueCrackedPass, 'r') as file:
                passwordsCracked = len(file.readlines())
                if passwordsCracked > 0:
                    print("--> A total of %i passwords have been cracked successfully. Check the results in %s."%(len(file.readlines()),outputFileWithUniqueCrackedPass))
                else:
                    print("--> No unique passwords were cracked.")
        else:
            print("--> No unique passwords were cracked.")

def crackPasswordsManager():
    if len(userRepeatedPass) > 0:
        print('\nFirstly, I will crack the repeated passwords due to a higher probability of them using a default or easy one.')
        if input('If you want to continue please, press Enter. ') == "":
            crackRepeatedPasswords()
            print('\nThere is a total of %i unique passwords in "%s". Please be aware this process can take a long time to complete.' % (len(finalUniqueUsersRecords), fileWithUniquePass))
            if input('If you want to continue please, press Enter. ') == "":
                crackUniquePasswords()
            else:
                exit('Incorrect value, exiting...')
        else:
            exit('Exiting program...')
    else:
        print('No repeated passwords were found. I will crack the list of unique passwords contained in the "%s" file.' % fileWithUniquePass)
        if input('If you want to continue please, press Enter. ') == "":
            crackUniquePasswords()
        else:
            exit('Incorrect value, exiting...')

    printFinalStats()


# open the file in read mode
with open(usersPathFile, newline='') as csvfile:
    
    # creating dictreader object
    file = csv.DictReader(csvfile)

    # iterating over each row and append
    # values to finalUniqueUsersRecords list
    for col in file:
        totalFileRecords += 1
        # Exclude blank passwords records
        if(len(col['user_password']) > 0 and col['user_password'] != '<blank>' and col['user_password'] != ''):
            finalUniqueUsersRecords.append({'password': col['user_password'], 'username': col['user_name']})

    if(len(finalUniqueUsersRecords) > 0):
        print('**** Initial file stats:')
        print(f'Total of records in file: {str(totalFileRecords)}.')
        print(f'Users with empty password: {str(totalFileRecords - len(finalUniqueUsersRecords))}.')
        print(f'--> Final number of records to analise: {str(len(finalUniqueUsersRecords))}.')

        if(getUsersWithSamePassword()):
            print(f'{len(userRepeatedPass)} duplicate passwords have been found!')
            for record in userRepeatedPass:
                print('--> Password [ %s ] is duplicate %i times and used by [ %s ] usernames.' % (
                    record[0], len(record[1]), ", ".join(record[1])))
            hashcatChecker = subprocess.getstatusoutput('hashcat')
            if hashcatChecker[0] < 0:
                print('\nThe file "%s" has been analised succesfully.' % os.path.basename(usersPathFile))
                print('\nYou need to have installed Hashcat for cracking the passwords. Please download it at https://hashcat.net/hashcat and run the program again.')
                exit('Exiting program...')
            crackingChoice = input(
                '\nThe file "%s" has been analised succesfully. Would you like to crack the passwords using Hashcat? (type y/n and press Enter): ' % os.path.basename(usersPathFile))
            if crackingChoice in {"y", "Y", "n", "N"}:
                if crackingChoice in {"y", "Y"}:
                    createFilesForCracking()
                    crackPasswordsManager()
                else:
                    exit('Exiting program...')
            else:
                exit('\nIncorrect value, exiting...')            

        else:
            print('--> No duplicate passwords were found.')

    else:
        print('--> No valid records were found in the file.')
