def count_string_chars(string):
	count = 0
	pre_char = ''
	last_index = 0
	for char in string:
		if char == pre_char:
			continue
		else:
			for char_index in range(last_index, len(string)):
				if char == string[char_index]:
					count += 1
				else:
					print(char+":"+str(count)+' times')
					count = 0
					last_index = char_index
					break
				if char_index == len(string)-1:
					print(char+":"+str(count)+' times')
		pre_char = char