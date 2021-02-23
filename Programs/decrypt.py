msg = "Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba."
letters = [chr(b) for b in range(ord('a'), (ord('z')+1))]
print(letters)
greater = []
smaller = []
moreStr = ''
# for i in range(10):
# 	print(i)
# 	moreStr = ''
# 	lessStr = ''
for letter in msg:
	
	greater.append((letters[ord(letter)%len(letters)]))
	smaller.append(str(chr(ord(letter)-7)))


lessStr = ''.join(smaller)
moreStr = ''.join(greater)
lessStr.replace('<0x19>','j')

print('HELOOOOO!')
	# for letter in msg:
	# 	smaller.append(str(chr(ord(letter)-i)))
	# print('HELOOOOO!')

	# print(moreStr)
print(lessStr)
print(moreStr)
