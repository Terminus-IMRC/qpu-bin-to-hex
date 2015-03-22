#!/usr/bin/env python3
import sys

linenum=0
while True:
	try:
		s=input()
	except EOFError:
		break

	linenum+=1

	mn=s.find(";")
	if mn!=-1:
		s=s[:mn]
	mn=s.find("//")
	if mn!=-1:
		s=s[:mn]
	s=s.replace(" ", "")
	s=s.replace("\t", "")
	s=s.replace(",", "")

	if s=="":
		continue

	corestrlen=len(s)
	if corestrlen!=64:
		sys.exit("%s: %d: error: input string core size is not 64 but %d"%(sys.argv[0], linenum, corestrlen))

	b=int(s, 2)
	if b>0xffffffffffffffff:
		sys.exit("%s: %d: error: input value is out of 64-bit unsigned integer range"%(sys.argv[0], linenum))

	print("0x%08x, 0x%08x,"%(b&0x00000000ffffffff,(b&0xffffffff00000000)>>32))
