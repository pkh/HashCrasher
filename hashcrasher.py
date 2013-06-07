#!/usr/bin/python

#
#	hashcrasher.py
#	Created by pkh on 2013-06-07
#
#	Specify hash with the '-t' flag
#	Supported hashes:
#		MD5		 = 100
#		SHA1     = 200
#		SHA224   = 300
#		SHA256   = 400
#		SHA384   = 500
#		SHA512   = 600
# 
#

import sys
import getopt
import hashlib

VERSION_NUM = "0.0.1"



# -----------------------------
# usage
#
# Print out usage (help) info to terminal
# ----------------------------- 
def usage():
	print "hashcrasher.py " + VERSION_NUM
	print ""
	print "Usage: $ python hashcrasher.py -t <hash type> -i <hashfile>"
	print "Optional: -o <outputfile>"
	print ""
	print "Sorry, at this early stage, hashcrasher does not yet support hashes with salt."
	print ""

	print "========"
	print "Options"
	print "========"
	print ""

	print "* Available Hash Types:"
	print "\t100 = MD5"
	print "\t200 = SHA1"
	print "\t300 = SHA224"
	print "\t400 = SHA256"
	print "\t500 = SHA384"
	print "\t600 = SHA512"
	print ""

	print "======"
	print "Notes"
	print "======"
	print ""

	print "* Example Usage:"
	print "\tYou have a file of MD5 hashes called \'myfile.txt\' and you want the results printed to your terminal window:"
	print "\t$ python hashcrasher.py -t 100 -i myfile.txt"
	print ""

	sys.exit()



# -----------------------------
# start_cracking
#
# Attempts to decipher the given hash by repeatedly guessing
# 
# -----------------------------
def start_cracking(inFile, outFile, hashType):

	# Perform checks on input data
	# check to make sure we've chosen a hash to use
	if hashType == '':
		print "You must select a hash type using the -t flag"
		usage()
		return

	# Check for output file
	usingOutputFile = True
	if outFile == '':
		usingOutputFile = False
	else: 
		usingOutputFile = True

	
	# Start your engines and get rollin
	fileObj = open(inFile, 'r')

	foundHashes = []

	for line in fileObj:
		line = line.rstrip()

		for x in range(999999):
			hashed_num = str(x)
			if hashType == '100':	# MD5
				guess = hashlib.md5(hashed_num)
			elif hashType == '200': # SHA1
				guess = hashlib.sha1(hashed_num)
			elif hashType == '300': # SHA 224
				guess = hashlib.sha224(hashed_num)
			elif hashType == '400': # SHA 256
				guess = hashlib.sha256(hashed_num)
			elif hashType == '500': # SHA 384
				guess = hashlib.sha384(hashed_num)
			elif hashType == '600': # SHA 512
				guess = hashlib.sha512(hashed_num)
			else: 
				guess = ''



			if line in guess.hexdigest():
				foundString = guess.hexdigest() + ":" + str(x)
				foundHashes.append(foundString)
				break


	fileObj.close()

	# depending on user's preference, either dump found hashes
	# out to terminal window or write to the specified output file
	if usingOutputFile == False: # print to the terminal window
		if len(foundHashes) > 0:
			print "Found:"
			for fh in foundHashes:
				print fh
			print ""
		else: 
			print "No hashes found."

	else:						# print to the specified output file
		if len(foundHashes) > 0:
			outf = open(outFile, 'w')
			for fh in foundHashes:
				outf.write(fh + "\n")
			print "Wrote found hashes out to file: " + outf.name
			print ""
			outf.close()
		else :
			print "No hashes found."			


	

	

# -----------------------------
# MAIN
#
# -----------------------------
def main(argv):
	
	inputfile = ''
	outputfile = ''
	hashType = ''

	try:
		opts, args = getopt.getopt(argv, "ht:i:o:", ["hashtype=","ifile=", "ofile="])

	except getopt.GetoptError:
		usage()
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			usage()
		elif opt == '--help':
			usage()
		elif opt in ("-t", "--hashtype"):
			hashType = arg
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg

	if inputfile == '':
		usage()

	print "HashCrasher.py -- version " + VERSION_NUM
	print "Currently supports hash types: MD5, SHA1, SHA224, SHA256, SHA384, SHA512"
	print "HashCrasher is currently limited to hashes of 1-6 characters using a keyspace of [0-9]"
	print "For help, please use the -h (or --help) flag"
	print ""

	# start it up
	start_cracking(inputfile, outputfile, hashType)



if __name__ == "__main__":
	main(sys.argv[1:])