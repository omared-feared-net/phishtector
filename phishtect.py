import string
import random
ask = num = input("URL: ")
forge = ["blacklist.txt", "black2.txt"]
f = open(forge ,"rb")
blacklists = f.read()
if ask == '.'.join(random.sample(string.ascii_lowercase,5)) + "." + ''.join(random.sample(string.ascii_lowercase,5)) or blacklists:
 print("Phishing detected")
else:
     print("URL SAFE!")
 
