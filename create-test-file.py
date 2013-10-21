#!/usr/bin/python

#
#	create-test-file.py
#	Created by pkh on 2013-10-21
#
#	Hash type options:
#	
#
#
#
#

import random
import hashlib
import sys
import getopt

NUM_ENTRIES = 0
HASH_TYPE = 0

# -------------------------------------
# Print welcome text to terminal 
print "Welcome to create-test-file.py"
print "How many hashes would you like in your file?"
NUM_ENTRIES = int(raw_input())

print "Please enter the corresponding code for the hash type you would like:"
print "\t100 = MD5\n\t200 = SHA1\n\t300 = SHA224\n\t400 = SHA256\n\t500 = SHA384\n\t600 = SHA512"
HASH_TYPE = int(raw_input())

print ""


print "Creating file with " + str(NUM_ENTRIES) + " items."

numbers = []
hashes = []

# -------------------------------
# Create 6 digit numbers for testing

for x in range(NUM_ENTRIES):
	num = random.randint(0, 999999)
	numlst = list(str(num))

	lengthen = False

	while len(numlst) < 6:
		lengthen = True
		numlst.append("0")

	numlstString = ''.join(numlst)

	# print numlstString
	numbers.append(numlstString)

	# if lengthen == True:
	# 	numlst.append(" *")

	# print ''.join(numlst)



# -------------------------------
# Write all data to files

hashfile = open("hash-file.txt", 'w')
	
for numStr in numbers:
	if HASH_TYPE == 100:
		numHashObj = hashlib.md5(numStr)	
	elif HASH_TYPE == 200:
		numHashObj = hashlib.sha1(numStr)
	elif HASH_TYPE == 300: 
		numHashObj = hashlib.sha224(numStr)
	elif HASH_TYPE == 400:
		numHashObj = hashlib.sha256(numStr)
	elif HASH_TYPE == 500:
		numHashObj = hashlib.sha384(numStr)
	elif HASH_TYPE == 600:
		numHashObj = hashlib.sha512(numStr)

	numHashStr = numHashObj.hexdigest()
	hashfile.write(numHashStr + "\n")
	hashes.append(numHashStr)

hashfile.close()
print "Wrote " + str(NUM_ENTRIES) + " hashes to file: hash-file.txt"
	


keyfile = open("key-file.txt", 'w')

for x in xrange(len(numbers)):
	concattedStr = hashes[x] + ":" + numbers[x] + "\n"
	keyfile.write(concattedStr)

keyfile.close()
print "Wrote " + str(NUM_ENTRIES) + " hashes:keys to file: key-file.txt"
			

