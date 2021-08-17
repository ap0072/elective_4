# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


def fun_applycaesarcipher(msg, shift):
	s=""
	for i in msg:
		if i.islower():
			if (ord(i)+shift)<97:
				di=97-(ord(i)+shift)
				s=s+chr(122-(di-1))
				

			elif (ord(i)+shift)>122:
				di=(ord(i)+shift)-122
				s=s+chr(96+(di))
			else:
				s=s+chr(ord(i)+shift)
		
		elif i==" ":
			s=s+" "
	
		else:
			if (ord(i)+shift)<65:
				di=65-(ord(i)+shift)
				s=s+chr(90-(di-1))
			
			elif (ord(i)+shift)>90:
				di=(ord(i)+shift)-90
				s=s+chr(64+(di))

			else:
				s=s+chr(ord(i)+shift)

	return s



#print(new1("A"))
#print(fun_applycaesarcipher("We Attack At Dawn", 1))
#print(fun_applycaesarcipher("ABCDXYZ", -3))
#"XYZAUVW"))
#print(fun_applycaesarcipher("zodiac", -2))
#print(fun_applycaesarcipher("ABCDXYZ", 3))
#"DEFGABC"))
#print(fun_applycaesarcipher("abcdxyz", -3))
#"xyzauvw"))
#print(fun_applycaesarcipher("abcdxyz", 3))
#"defgabc"))


