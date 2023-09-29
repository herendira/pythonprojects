"""
# File: random_numbers.py
# Author: Herendira Gomez
# Class: CSE111 
# Assignment purpose: Call function

"""
import random

def main():
   wordslist = ["boy", "girl", "cat", "dog", "bird"]
   


   numbers = [16.2, 75.1, 52.3]
   
   print(numbers)
   append_random_numbers(numbers)
   print(numbers)
   append_random_numbers(numbers,5)
   print(f"{numbers}")
   append_random_words(wordslist, 1)
   print(wordslist)

def append_random_numbers(numbers_list, quantity=1):
    for i in range (quantity):
        quant=round((random.uniform(0,100)),1)
        
        numbers_list.append(quant)
    return numbers_list
        
     
def append_random_words(words_list, quantity=1):
    #words_list = ["boy", "girl", "cat", "dog", "bird"]
    #print(words_list)    
    for i in range(quantity):
      lista=random.choice(words_list)
      words_list.append(lista)
    return words_list
    
     

main()     
