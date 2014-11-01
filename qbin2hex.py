#!/usr/bin/env python3
import sys

while True:
	try:
		s=input()
	except EOFError:
		break

	mn=s.find(";")
	if mn!=-1:
		s=s[:mn]
	mn=s.find("//")
	if mn!=-1:
		s=s[:mn]
	s=s.replace(" ", "")
	s=s.replace(",", "")

	if s=="":
		continue

	corestrlen=len(s)
	if corestrlen!=64:
		sys.exit("%s: error: input string core size is not 64 but %d"%(sys.argv[0], corestrlen))

	b=int(s, 2)
	if b>0xffffffffffffffff:
		sys.exit("%s: error: input value is out of 64-bit unsigned integer range"%sys.argv[0])

	print("0x%08x, 0x%08x,"%((b&0xffffffff00000000)>>32, b&0x00000000ffffffff))
