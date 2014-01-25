# For solving http://www.pythonchallenge.com/pc/def/map.html
import string

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

abc = string.ascii_lowercase
# deal with the wrap around
abc = abc + "ab"
#abc = [ x for x in abc]
print abc

new_phrase = ""
print s
x = 0
for c in s:
	if c in abc:
		replace_c_with = abc[abc.index(c)+2]
		new_phrase = new_phrase + replace_c_with
		print s[x] + " to " + replace_c_with
		#s = s.replace(s[x],replace_c_with)
	else:
		print c + " to " + c
		new_phrase = new_phrase + c
	
	x = x + 1
print new_phrase