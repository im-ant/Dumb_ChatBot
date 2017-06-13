#!/usr/bin/python

####################
# Note to self:
#	- Since there was no specification on worting the input list (e.g. by frequency),
#		the inputted fles are simply split and put into lists for reading
#
#
# 
#
###################
import sys
import random


################################# FILE INPUT METHODS #################################

#Method to read a file and return a list of (unprocessed) words
def read_file (filename):
    #Initiate master list to contain all the words in this file
	words = []
    #open the file
	try:
		f = open(filename, 'r')
	except IOError:
		return None
	
    #loop through each line of the file
	for line in f:
		#replace all other sentence-enders with periods
		line2 = line.replace('?','.')
		line3 = line2.replace('!','.')
		#replace all the hyphens with spaces (for later splitting)
		line_edited = line3.replace('-',' ')

		
        #Split each line by periods to get sentences
		sentences = line_edited.split('.')
        #Loop through each sentence
		for sen in sentences:
			#join all alphabetic characters and space, then split by spaces
			w_list=''.join(c for c in sen if c.isalpha() or c.isspace()).split()
			#If the list isn't empty, append to the master list
			if len(w_list)>0:
				words.append(w_list)
			
    #close the file
	f.close()
	
    #return the list
	return words

#Input a list and output a list with all items made lowercase
def make_lower(input_list):
    #Initiate output file
    output_list=[]
    #loop through each lines of the input file
    for line in input_list[:]:
        #Initiate a list for each line
        lower_line=[]
        #loop through each word of each line
        for word in line[:]:
            #make each word lowercase and append to output file
            lower_line.append(word.lower())
        #Append the list of words in the line to the master output list
        output_list.append(lower_line)
    #return output file
    return output_list
    

################################# CHATTING METHODS #################################

#Get the last word the user inputted (in lowercase)
def get_lower_last_word(in_str):
	#replace all the hyphens with spaces (for splitting)
	edited_str = in_str.replace('-',' ')
	#join all alphabetic characters and space, then split by spaces
	w_list=''.join(c for c in edited_str if c.isalpha() or c.isspace()).split()
	#Return the last item in the word list in lowercase
	return (w_list[len(w_list)-1]).lower()

#Get a random word from the language
def get_rand_word (lang):
	#Randomely shuffle the language
	ran_lang = lang
	random.shuffle(ran_lang)
	#Get a random word from the first (random) sentence
	n = random.randint(0, len(ran_lang[0])-1)
	return ran_lang[0][n]

#Initiate the first word of the response
def get_first_word(word, lang):
	#Randomely shuffle the language to provide dynamic response
	ran_lang = lang
	random.shuffle(ran_lang)
	#Loop through each sentence
	for sen in ran_lang:
		#See if the sentence contains the word
		if word in sen:
			#If so, get the index of the word
			i = sen.index(word)
			#Return the word at the next index (if possible)
			try:
				next_word = sen[i+1]
				return next_word
			except IndexError:
				continue
	#At this point, the first word is not found - generate random word
	return get_rand_word(lang)

#Get the next word of the resposne
def get_next_word (word, lang):
	#Randomely shuffle the language to provide dynamic response
	ran_lang = lang
	random.shuffle(ran_lang)
	#Loop through each sentence
	for sen in ran_lang:
		#See if the sentence contains the word
		if word in sen:
			#If so, get the index of the word
			i = sen.index(word)
			#Return the word at the next index (if possible)
			try:
				next_word = sen[i+1]
				return next_word
			except IndexError:
				return None
				
#Process the response to be in a proper format
def process_response(w_list):
	#Capitalize the first word
	res = w_list[0].capitalize()
	#Loop through and add on each subsequent words (if ther are more)
	if len(w_list)>1:
		for i in range(1, len(w_list)):
			res = res+" "+w_list[i]
	#Return whild adding period
	return "Received: "+res+"."


#Method that intakes a word and assemble a response by the computer
def generate_response(in_word, lower_lang):
	#A list to store the response
	res_list = []
	#Initiate the first word of the response
	res_list.append(get_first_word(in_word, lower_lang))
	#Limit the length of the response and begin subsequent generation
	while len(res_list) < 20:
		#find the next word based on the last word of the response
		next_word = get_next_word(res_list[len(res_list)-1], lower_lang)
		#If the next word is not found, terminate loop
		if next_word == None:
			break
		#Else if the next word is not null, append to response
		else:
			res_list.append(next_word)
	#Post-process the response to be proper
	return process_response(res_list)


#The infinite loop for the chat
def chat_loop(lower_lang):
	#Put the infinite loop in a try block
	try:
		#Actual infinite loop
		while True:
			user_input = raw_input("Send: ")
			word = get_lower_last_word(user_input)
			print generate_response(word, lower_lang)
	
	#Catch EOFError (^D) to terminate the loop
	except EOFError:
		print
		print "Session terminated by user."
		return 0


#main method
def main():
    #check for input arguments
	if len(sys.argv) < 2:
		print "[Error] Requires at least 1 argument"
		return 0
	#Create a list to hold all the word (each sub-list contain all words in a sentence)
	raw_lang = []
	#Read each file to obtain the list of words
	for i in range(1, len(sys.argv)):
    	#Store all words from a file
		curr_raw_words = read_file(sys.argv[i])
		#Error check the file
		if (curr_raw_words == None):
			print "[Error] File empty or not found:"+str(argv[i])
			return 0
		#If the file is good, append to the raw masterlist
		for sen in curr_raw_words:
			raw_lang.append(sen)
    #Make the list of words lowercase
	lower_lang = make_lower(raw_lang)
	
    #Initiate chat 
	chat_loop(lower_lang)

main()

