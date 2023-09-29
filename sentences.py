"""
# File: sentences.py
# Author: Herendira Gomez
# Class: CSE111 
# Assignment purpose: Call function

"""
import random

def main():

     for i in range(1,7):
        
        quantity = random.randint(1,2)
   
        cap_word = get_determiner(quantity)
   
        noun = get_noun(quantity)
    
        verbo = get_verb(quantity)

        preposition = get_preposition()

        frase = get_prepositional_phrase(quantity)

        adj = get_adjective(quantity)

        print(cap_word,adj, noun, verbo, preposition, frase)


    

def get_determiner(quantity):
   
    
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    cap_word=word.capitalize()
    return cap_word
    
def get_noun(quantity):
    
    
    if quantity==1:
       words = ["boy", "girl", "cat", "dog", "bird", "house"]
       word = random.choice(words)
    else:
        quantity==2
        words=[ "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]   
        word = random.choice(words)
    return word
    
def get_verb(quantity):
    
    tense=["past" , "present", "future"]
    times=random.choice(tense)

    if times=="past" and (quantity==1 or 2):
        past = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
        verb=random.choice(past)

    

    elif times=="future" and (quantity==1 or 2):
        future = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
        verb=random.choice(future) 

    elif times=="present" and quantity==1:
        present_1 = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"] 
        verb=random.choice(present_1) 

    elif times=="present"and quantity==2:
        present = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"] 
        verb=random.choice(present)   

    return verb

    
def get_preposition():
    
    prepo =[ "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    preposition =  random.choice(prepo)  
    return preposition

def get_prepositional_phrase(quantity):
    if quantity == 1:
        frase=[" the car.", "the evening.", "my home.", "the park.", "the work.", "my hand.",
                 "one child."]
        phrase = random.choice(frase)
    if quantity == 2:
        frases=["many cars.", " many rabbits.", "a lot of dogs.", "some cats"]
        phrase = random.choice(frases)
    return phrase   
   
def get_adjective (quantity):
    if quantity==1:
       adj_list = ["beautiful", "happy", "tall", "suspicious", "big", "small"]
       adjetive = random.choice(adj_list)
    else:
        quantity==2
        adjs_list=[ "beautifuls", "happies", "talls", "braves", "handsomes"]   
        adjetive = random.choice(adjs_list)
    return adjetive

main()
    


