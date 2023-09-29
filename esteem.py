"""
# File: esteem.py
# Author: Herendira Gomez
# Class: CSE111 
# Assignment purpose: Functions 

"""
def main():

  print("This program is an implementation of the Rosenberg")
  print("Self-Esteem Scale. This program will show you ten")
  print("statements that you could possibly apply to yourself.")
  print("Please rate how much you agree with each of the")
  print("statements by responding with one of these four letters:")

  print("D means you strongly disagree with the statement.")
  print("d means you disagree with the statement.")
  print("a means you agree with the statement.")
  print("A means you strongly agree with the statement.")

  print("1. I feel that I am a person of worth, at least on an equal plane with others.")
  reponse1 = input("Enter D, d, a, or A: ") 
  print("2. I feel that I have a number of good qualities.")
  reponse2 = input("Enter D, d, a, or A: ")
  print("3. All in all, I am inclined to feel that I am a failure.")
  reponse3 = input("Enter D, d, a, or A: ")
  print("4. I am able to do things as well as most other people.")
  reponse4 = input("Enter D, d, a, or A: ")
  print("5. I feel I do not have much to be proud of.")
  reponse5 = input("Enter D, d, a, or A: ")
  print("6. I take a positive attitude toward myself.")
  reponse6 = input("Enter D, d, a, or A: ")
  print("7. On the whole, I am satisfied with myself.")
  reponse7 = input("Enter D, d, a, or A: ")
  print("8. I wish I could have more respect for myself.")
  reponse8 = input("Enter D, d, a, or A: ")
  print("9. I certainly feel useless at times.")
  reponse9 = input("Enter D, d, a, or A: ")
  print("10. At times I think I am no good at all.")
  reponse10 = input("Enter D, d, a, or A:  ")
  
  score1=(positive(reponse1, reponse2, reponse4, reponse6, reponse7))
  score2=(negative(reponse3, reponse5, reponse8, reponse9, reponse10))
  score=score1+score2
  
  self_esteem(score)

 
   
def positive(reponse1, reponse2, reponse4, reponse6, reponse7):
    """Strongly Disagree	0
       Disagree	1
       Agree	2
       Strongly Agree	3
    """
    score=0
    if reponse1=="A":
        score=score+3
    if reponse1=="a":
        score=score+2
    if reponse1=="d":
        score=score+1
    if reponse1=="D":
        score=score+0      
    
    if reponse2=="A":
           score=score+3
    if reponse2=="a":
           score=score+2
    if reponse2=="d":
           score=score+1
    if reponse2=="D":
           score=score+0  
    
    if reponse4=="A":
            score=score+3
    if reponse4=="a":
            score=score+2
    if reponse4=="d":
            score=score+1
    if reponse4=="D":
            score=score+0  
        
    if reponse6=="A":
                   score=score+3
    if reponse6=="a":
                   score=score+2
    if reponse6=="d":
                   score=score+1
    if reponse6=="D":
                   score=score+0
                
    if reponse7=="A":
                       score=score+3
    if reponse7=="a":
                       score=score+2
    if reponse7=="d":
                       score=score+1
    if reponse7=="D":
                       score=score+0     
    
    return score

def negative(reponse3, reponse5, reponse8, reponse9, reponse10):
    """Strongly Disagree	3
       Disagree	2
       Agree	1
       Strongly Agree	0
    """
    score=0
    if reponse3=="A":
        score=score+3
    if reponse3=="a":
        score=score+2
    if reponse3=="d":
        score=score+1
    if reponse3=="D":
        score=score+0      
    
    if reponse5=="A":
           score=score+3
    if reponse5=="a":
           score=score+2
    if reponse5=="d":
           score=score+1
    if reponse5=="D":
           score=score+0  
    
    if reponse8=="A":
        score=score+3
    if reponse8=="a":
       score=score+2
    if reponse8=="d":
        score=score+1
    if reponse8=="D":
        score=score+0  
    
    if reponse9=="A":
        score=score+3
    if reponse9=="a":
        score=score+2
    if reponse9=="d":
        score=score+1
    if reponse9=="D":
        score=score+0
            
    if reponse10=="A":
        score=score+3
    if reponse10=="a":
        score=score+2
    if reponse10=="d":
        score=score+1
    if reponse10=="D":
        score=score+0     
    
    return score

def self_esteem(score):
    if score>=16:
        print(f"Your score is: {score}\n You have not a problematic low self-esteem")
    else:
         score<=15
         print(f"Your score is: {score}\n Score below 15 may indicate problematic low self-esteem.")    

main()         