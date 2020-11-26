import numpy as np
words=["apple","jeep","monkey","dummy","computer","table","television","journey"]

word=np.random.choice(words)
hang_man=['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']
j=0
guesses=''
chances=7
flag=0
while chances>0:
    fail=0
    
    for char in word:
        
        if char in guesses:
            print(char,end=" ")
            
        else:
            print("_",end=" ")
            fail=fail+1
        
    if fail==0:
        print("You Won!!!!")
    guess=input("\nGuess a letter..")
    guesses+=guess
    if guess not in word:
        chances -=1
        print(hang_man[j])
        j=j+1
        
        print("\nWrong:(")
    print("You have ",chances,"chances left")
    if chances==0:
        print("\nYou Lose :(")
    
