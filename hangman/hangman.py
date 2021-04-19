import random
import json

data=list((json.load(open("data.json"))).keys())
def hangman():
    valid="abcdefghijklmnopqrstuvwxyz"
    flag=1
    while(flag==1):
        flag=0
        word=random.choice(data)
        word=word.lower()
        for letter in word:
            if letter not in valid:
                flag=1
    guessmade=''
    turns =10
    while len(word)>0:
        main=''
        for letter in word:
            if letter in guessmade:
                main+=letter
            else:
                main+='_'

        if main==word:
            print("You win",main)
            break


        print("Guess the word:" , main)
        guess = input()


        while guess not in valid:
            guess=input("Enter valid lowercase character ")

        while guess in guessmade:
            guess=input("Enter new character ")


        if guess in word:
            guessmade+=guess
        else:
            turns-=1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose",word)
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break


name=input("Enter your name ")
print("Hello %s"%name)
print("--------------------------")
print("You have 10 attempts in total")
hangman()
