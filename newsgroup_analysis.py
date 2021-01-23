#import pandas as pd
import glob
import pickle


#builds a set of all possible characters for domain
def build_domain_set():
	d_set = set()
	#0-9
	for k in range(48,58):
		d_set.add(chr(k))
	#A-Z
	for k in range(65,91):
		d_set.add(chr(k))
	#a-z
	for k in range(97,123):
		d_set.add(chr(k))
	#'-', '.'
	for k in range(45,47):
		d_set.add(chr(k))
	return d_set

#builds a set of all possible characters for personal
def build_personal_set():
	p_set = build_domain_set()
	#'!'
	p_set.add(chr(33))
	#'/'
	p_set.add(chr(47))
	#'='
	p_set.add(chr(61))
	#'?'
	p_set.add(chr(63))
	#'#', "$", '%', '&', single quote
	for k in range(35,40):
		p_set.add(chr(k))
	#'*', '+'
	for k in range(42,44):
		p_set.add(chr(k))
	#'^', '_'
	for k in range(94,96):
		p_set.add(chr(k))
	#'{', '}', '|', '~'
	for k in range(123,127):
		p_set.add(chr(k))
	return p_set

#checks if the personal is valid
def valid_personal(personal):
	is_valid = True
	personal_set = build_personal_set()
	if len(personal) > 64:
		is_valid = False
	if personal[0] == '.' or personal[len(personal) - 1] == '.':
		is_valid = False
	if '..' in personal:
		is_valid = False
	for character in personal:
		if not (character in personal_set):
			is_valid = False
	return is_valid

#checks if the domain is valid
def valid_domain(domain):
	is_valid = True
	domain_set = build_domain_set()
	if len(domain) > 253:
		is_valid = False
	# elif not ('.' in domain):
	# 	is_valid = False
	elif domain[0] == '.' or domain[len(domain) - 1] == '.':
		is_valid = False
	elif '..' in domain:
		is_valid = False
	for character in domain:
		if not (character in domain_set):
			is_valid = False
	return is_valid

#check_email_validity(email) returns true if it is a valid email, false if not. Emails are in the format personal@domain
def check_email_validity(email):
	#checks if email is missing personal, domain, '@', '.' in domain, or if it contains multiple '@'
	is_valid = True
	if '@' in email:
		personal_domain_list = email.split('@')
		personal = personal_domain_list[0]
		domain = personal_domain_list[1]
		
		if len(personal_domain_list) > 2 or personal == '' or domain == '':
			is_valid = False

		if(is_valid):
			personal_is_valid = valid_personal(personal)
			domain_is_valid = valid_domain(domain)
			is_valid = personal_is_valid and domain_is_valid

	else:
		is_valid = False

	return is_valid



#builds a set of all possible characters for a word
def build_word_set():
	w_set = set()
	#0-9
	for k in range(48,58):
		w_set.add(chr(k))
	#A-Z
	for k in range(65,91):
		w_set.add(chr(k))
	#a-z
	for k in range(97,123):
		w_set.add(chr(k))
	return w_set

#removes special characters
def remove_special_characters(word) -> str:
	word_set = build_word_set()
	new_word = ''
	for char in word:
		if char in word_set:
			new_word = new_word + char
	return new_word

#checks if a word is already present in the the word_counts dictionary and increments the value by 1
def add_word_to_dict(word, word_counts):
	if word in word_counts:
		word_counts[word] += 1
	else:
		word_counts[word] = 1
	return word_counts

#returns a tuple containing a list of email addresses and a dictionary of word counts for the file
def process_newsgroup_file(filepath, word_counts):
	emails_list = []
	with open(filepath, encoding='windows-1252') as current_file:
		for line in current_file:
			line_list =  line.split()
			for word in line_list:
				if check_email_validity(word):
					emails_list.append(word)
					continue
				word = remove_special_characters(word)
				add_word_to_dict(word, word_counts)
	return(emails_list, word_counts)




def process_newsgroup_topic(dir_file_path):
	word_list = {}
	emails_list = []
	
	files = glob.glob(dir_file_path)
	#print(files)
	for new_file in files:
		#print(new_file)
		(emails_list_temp, word_list) = process_newsgroup_file(new_file, word_list)
		emails_list.extend(emails_list_temp)
	with open('sci.crypt.emails.txt', 'w') as f:
		for email in emails_list:
			f.write('%s\n' % email)
	with open('sci.crypt.wordcounts.txt', 'wb') as g:
		pickle.dump(word_list, g)

	#return(emails_list, word_list)

	





if __name__ == '__main__':
	process_newsgroup_topic("/Users/stacey/Documents/DATA515/20_newsgroups/sci.crypt/*")
	





	#  word_counts = {}
	#  (emails_list,word_counts) = process_newsgroup_file('/Users/stacey/Downloads/20_newsgroups/sci.crypt/15400', word_counts)
	#  print(emails_list)
	#  with open('sci.crypt.emails.txt', 'w') as f:
	# 	 for email in emails_list:
	# 		 f.write('%s\n' % email)





