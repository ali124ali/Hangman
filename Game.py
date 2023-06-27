from attachment import  hanging_status #,rand_word
import os
import requests
import ast
import time

# ------------------------------ Game's Code Body ---------------------------------

class Hangman:
    point_list = {}

    def __init__(self, name, lvl):
        self.name = name
        self.__points = 0
        self.__guess_count = 0
        self.wrong_letters = set()
        self.correct_letters = set()
        self.status = False

        self.add_player()

        word = requests.get(f'https://random-word-api.vercel.app/api?words=1&length={lvl}')
        while word.status_code != 200:
            word = requests.get(f'https://random-word-api.vercel.app/api?words=1&length={lvl}')
            print('Wait Please ...')
            time.sleep(1)
        word = ast.literal_eval(word.text)

        self.word = word[0].strip()

    # ------------------------------  Play Section ---------------------------------

    def guess(self):

        print(f"Hi {self.name}.\n{'_ ' * len(self.word)}\n")

        while True:
            user_guess = input("Please Guess: ").strip()

            if len(user_guess) > 1:
                if user_guess == self.word:
                    print('Congratulation :)')
                    print(f'Answer Was "{self.word}".')
                    self.status = True
                    self.check_point()
                    break
                else:
                    self.guess_counter()
                    print(hanging_status(self.__guess_count))
                    print(f'You Have {self.guess_left()} more chances !')
            else:
                if user_guess in self.word:
                    self.correct_letters.update(user_guess)

                    result = ''.join([i if i in self.correct_letters else '_ ' for i in self.word])

                    if result == self.word:
                        os.system('clear')
                        print('Congratulation :)')
                        print(f'Answer Was "{self.word}".')
                        self.status = True
                        self.check_point()
                        break
                    else:
                        print(result)

                
                else:
                    self.wrong_letters.update(user_guess)
                    self.guess_counter()
                    os.system('clear')
                    result = ''.join([i if i in self.correct_letters else '_ ' for i in self.word])
                    print(result)
                    print(hanging_status(self.__guess_count))
                    print(f'You Have {self.guess_left()} more chances !')

                    if  self.guess_left() == 0:
                        
                        print(f'Answer Was "{self.word}".')
                        print('Hangman !!! :(\n')
                        break

                print(f"Your Wrong Guesses: ({', '.join(self.wrong_letters)})")


    def guess_left(self):
        return 6 - self.__guess_count
    
    def guess_counter(self):
        self.__guess_count += 1

    def add_player(self):
        if self.name not in Hangman.point_list.keys():
            Hangman.point_list.update({self.name:0})
        
    def check_point(self):
        if self.status:
            Hangman.point_list[self.name] += 1

# ------------------------------ Game Settings ---------------------------------

class Settings:
    def __init__(self):
        name = input('Enter Your Name: ').strip()
        while name == '':
            print("Name Can't Be Empty !")
            name = input('Enter Your Name: ').strip()

        os.system('clear')
        lvl = input('Select Game Level:\n\nEasy-(3 Chars) --> e\nMedium-(5 Chars) --> m\nHard-(7 Chars) --> h\nSelect: ')
        if lvl == 'e':
            player = Hangman(name, 3)
        
        elif lvl == 'm' or lvl not in 'emh':
            player = Hangman(name, 5)
        
        elif lvl == 'h':
            player = Hangman(name, 7)

        os.system('clear')
        player.guess()
        

# ------------------------------ Main Menu ---------------------------------

if __name__ == '__main__':
    os.system('clear')
    print('\n>>>>>>>> Welcome To Hangman :) <<<<<<<<<')

    while True:
        option = input('\nPlease select an option.\n\nStart Game --> s\nResults --> r\nExit --> x\nYour Choice: ')

        # ----------------- Select Player -------------------
        if option == 's':
            os.system('clear')
            Settings()

        # ----------------- Show Results ---------------------
        elif option == 'r':
            os.system('clear')
            result = Hangman.point_list
            if result != {}:
                result = sorted(Hangman.point_list.items(), key = lambda x : x[1], reverse=True)
                print(f"\nGame Resuts:\n({len(result)}) person(s) played this game.")
                for k, v in result:
                    print(f"\n>>>>>>>> ({k}) guesses ({v}) word(s)")
            else:
                
                print('\n>>>>>>>> There is no result yet !!! <<<<<<<<<\n')

        elif option == 'x':
            os.system('clear')
            print('\n>>>>>>>> Thanks For Playing Our Game. <<<<<<<<\n\
              \n\t\tBy "Ali Dehkhodaei"')
            break