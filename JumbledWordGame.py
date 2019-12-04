# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 17:56:17 2019

@author: Sartaj 

Word Jumble Game.
The computer picks a random word and then "jumbles" it.
The game is played between two players and  player has to guess the original word.
If Guessed word is correct his score will be incremented by one .If not he may leave the game .

"""
import random
def choose():
    words=['rainbow','computer','science','programming','mathamatics','player','condition','reverse','water','board']
    pick=random.choice(words)
    return pick 

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled
def thank(p1n,p2n,p1,p2):
     print(p1n,'Your Score is ',p1)
     print(p2n,'Your Score is ',p2)
     print("Thanks for Playing ")
     print("Have a nice day :) ")
def play():
    p1name=input("Player 1 , Please enter your name : \n ")
    p2name=input("Player 2 , Please enter your name : \n ")
    pp1=0
    pp2=0
    turn=0
    while(1):
        #computer's task 
        picked_word=choose()
        #create the question 
        qn=jumble(picked_word)
        print (qn) 
        # For Player One 
        if turn%2==0:
                print(p1name,"Your Turn , ")
                ans=input("What is on your mind : \n")
                if ans==picked_word:
                    pp1 = pp1+1
                    print("Your score is : " , pp1)
                else:
                    print("Better Luck Next Time , I thought  ",picked_word)
                    c=input("Press 1 to continue and 0 to quit : ")
                    if c==0:
                      thank(p1name,p2name,pp1,pp2 )
                      break
       #player 2 
        else:
                print(p2name,"Your Turn , ")
                ans=input("What is on your mind : \n")
                if ans==picked_word:
                    pp2 = pp2+1
                    print("Your score is : " , pp2)
                else:
                    print("Better Luck Next Time , I thought  ",picked_word)
                    c=input("Press 1 to continue and 0 to quit : ")
                    if c==0:
                        thank(p1name,p2name,pp1,pp2 )
                        break
        turn = turn+1
play()
    
