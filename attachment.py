# words = ['baboon', 'badger', 'bear', 'beaver', 'camel','clam', 'cobra', 'cougar', \
#     'coyote', 'crow', 'deer','donkey', 'duck', 'eagle', 'ferret','frog', 'goat', 'goose', \
#     'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt', 'otter', \
#     'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram','raven', 'rhino', \
#     'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan',\
#     'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'zebra']

hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
from random import choice

def rand_word():
	return choice(words)

def hanging_status(status):
	return hangman[status]

