# Dumb_ChatBot
A dumb but entertaining chat bot I made for class

How it works is it takes as input some piece(s) of literature (see the reference_texts folder) to initiate its "list of words".

For your input sentence, it takes the last words and tries to match that word to something in its internal list of words. If a match is found, it will spit out the next word in its internal list, then repeat that process until either a period is encountered or the maximum length of word is achieved.

If there are multiple words / possible responses, it picks one at random.

## Running the dumb bot
1. Download `chat_bot.py` and (optional) the reference texts
2. Run from the command line via `python chat_bot.py [reference_file(s)]`
  - Note that it has to be ran using Python 2
  - It can take multiple reference files, it'll just initiate them all
3. Have fun chatting!
4. Exit using `ctrl + c`
