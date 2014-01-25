# For solving http://www.pythonchallenge.com/pc/def/map.html
import string

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

abc = [ x for x in string.ascii_lowercase][::-1]

print s
x = 0
for c in abc:
	if (c in s) and (x<20):
		s = s.replace(c,abc[x+2])
		print c + " - " + s
	x = x + 1