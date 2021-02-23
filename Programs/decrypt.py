# msg = "Pm ol ohk hufaopun jvumpkluaphs av zhf ol dyval pa pu jpwoly aoha pz if zv johunpun aol vykly vm aol slaalyz vm aol hswohila aoha uva h dvyk jvbsk il thkl vba"
# msg ="Kh jg jcf cpavjkpi eqphkfgpvkcn vq uca jg ytqvg kv kp ekrjgt vjcv ku da uq ejcpikpi vjg qtfgt qh vjg ngvvgtu qh vjg cnrjcdgv vjcv pqv c yqtf eqwnf dg ocfg qwv"
msg = 'Kxvtja Kjv'
letters = [chr(b) for b in range(ord('a'), (ord('z')+1))]
print(letters)
greater = []
smaller = []
moreStr = ''
# for i in range(10):
# 	print(i)
# 	moreStr = ''
# 	lessStr = ''
# for letter in msg:
# 	if letter == '\x19':
# 		print("ok")
	
# 	greater.append((letters[ord(letter)%len(letters)]))
# 	smaller.append(str(chr(ord(letter)-7)))
	

# lessStr = ''.join(smaller)
# moreStr = ''.join(greater)
# # lessStr.replace('<0x19>','j')

print('HELOOOOO!')
	# for letter in msg:
	# 	smaller.append(str(chr(ord(letter)-i)))
	# print('HELOOOOO!')

	# print(moreStr)
# print(smaller)
# print(greater)

def decrypt(msg,offset):
	shift = 7-offset
	msg = msg.split(" ")

	dec = r""
	for eachWord in msg:
		for eachChar in eachWord:
			if eachChar.isupper():
				eachChar = eachChar.lower()
				newL = (letters[(ord(eachChar)+shift)%len(letters)])
				newL = newL.capitalize()
				dec += newL
			else:

				# newL = chr(ord(eachChar)-shift)
				(ord(eachChar)-shift)%len(letters)
				newL = (letters[(ord(eachChar)+shift)%len(letters)])
				dec += newL
		dec += " "
	print(dec)

def autodecrypt(msg):

	for eachWord in msg:
		for eachChar in eachWord:
			pass

decrypt(msg,9)