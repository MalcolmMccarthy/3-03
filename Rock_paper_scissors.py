# created by malcolm mccarthy
# in october 2017
# for ISC3U
# program plays rock paper scissors 
import ui
from numpy import random

ROCK = 1
PAPER = 2
SCISSORS = 3
# computer picks either rock, paper or scissors
computer_pick = random.randint(1, 3)

def rock_button(sender):
   
    if computer_pick == 1:
        view['answer_label'].text = "Tie!"
 
    elif computer_pick == 2:
        view['answer_label'].text = "Paper!  You lose!"
	  
    elif computer_pick == 3:
        view ['answer_label'].yext = "Scissors! You win!"
        
def paper_button(sender):
    
    if computer_pick == 1:
        view['answer_label'].text = "Rock! You win!"
   
    elif computer_pick == 2:
        view['answer_label'].text = "Tie!"
    
    elif computer_pick == 3:
        view['answer_label'].text = "Scissors! You lose!"
        
def scissors_button(sender):
     
    if computer_pick == 1:
            view['answer_label'].text = "Rock! You lose!"
    	
    elif computer_pick == 2:
            view['answer_label'].text = "Paper! You win!"
    	
    elif computer_pick == 3:
            view['answer_label'].text = "Tie!"
        
view = ui.load_view()
view.present('sheet')
