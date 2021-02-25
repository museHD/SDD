# msg = 'Vncqxm rw fqrlq njlq unccna rw cqn yujrwcngc rb anyujlnm kh j unccna bxvn orgnm wdvkna xo yxbrcrxwb mxfw cqn juyqjknc. Cqn vncqxm rb wjvnm jocna Sdurdb Ljnbja, fqx dbnm rc rw qrb yarejcn lxaanbyxwmnwln.'
msg = """Fgdzqp uf gb etagxp za hmxxqk oageuz tq. Ebqmwuzs zgyqdage mew pup taddunxq bmowmsqe eqf. Metmyqp tqdeqxr tme puefmzf omz efgpuqp yde. Xqp ftqdqradq ufe yuppxqfaz bqdbqfgmx rgxruxxqp bdahueuaz rdmzwzqee. Eymxx tq pdmiz mrfqd myazs qhqdk ftdqq za. Mxx tmhuzs ngf kag qpimdp sqzuge ftagst dqymdw azq. 

Mpyudmfuaz iq egddagzpqp baeeqeeuaz rdqcgqzfxk tq. Dqymdwmnxk pup uzodqmeuzs aoomeuazmx faa ufe purruogxfk rmd qebqoumxxk. Wzaiz fuxqp ngf eaddk vak nmxxe. Nqp egppqz ymzzqd uzpqqp rmf zai rqqnxk. Rmoq pa iuft uz zqqp ar iurq bmup ftmf nq. Za yq mbbxmgpqp ad rmhagdufq pmetiaape ftqdqradq gb puefdgefe qjbxmuzqp. 
"""
letters = [chr(b) for b in range(ord('a'), (ord('z')+1))]


print(letters)
greater = []
smaller = []
moreStr = ''
import matplotlib.pyplot as plt

def decrypt(msg,offset):
	shift = 7-offset
	msg = msg.split(" ")

	dec = r""
	for eachWord in msg:
		for eachChar in eachWord:
			if eachChar.lower() in letters:
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
			else:
				dec += eachChar
		dec += " "
	return dec

def autodecrypt(msg):

	# /give @p minecraft:diamond_sword{Enchantments:[{id:sharpness,lvl:2000}]}
	freq = []
	for eachL in letters:
		letterCount = msg.count(eachL)
		freq.append(letterCount)

	highestIndex = freq.index(max(freq))
	shift = highestIndex-4
	print(decrypt(msg,shift))
	# print()
	# print(letters[highestIndex])
	# plt.plot(letters,freq)
	# plt.show()


# decrypt(msg,9)
autodecrypt(msg)