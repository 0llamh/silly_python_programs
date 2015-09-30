pyg = 'ay'							#pyglatin suffix

word = raw_input('Enter a word:')	#user prompt
word = word.lower()					#creates lowercase copy
word_length= len(word)				#length variable

first = word[0]						#snatches first letter

if len(word) > 0 and word.isalpha():
    new_word = word[1:word_length] + first + pyg
    #creates the new pyglatin word concatenating
	#the word without the first letter, the first letter, and suffix
	print new_word
else:
    print 'empty'