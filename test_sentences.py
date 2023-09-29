"""
# File: test_sentences.py
# Author: Herendira Gomez
# Class: CSE111 
# Assignment purpose: Testing functions 

"""
from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adjective

import pytest


def test_get_determiner():
   
    single_determiners = ["A", "One", "The"]
    for _ in range(4):
       word = get_determiner(1)
       assert word in single_determiners

   

    plural_determiners = ["Some", "Many", "The"]
    for _ in range(4):
       word = get_determiner(2)
       assert word in plural_determiners
    
def test_get_noun():
    words = ["boy", "girl", "cat", "dog", "bird", "house"]
    for _ in range(7):
         noun= get_noun(1)
         assert noun in words

    words=[ "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]   
    for _ in range(11):
        nouns = get_noun(2)
        assert nouns in words
    

def test_get_verb():

    #tense=["past" , "present", "future"]
    for _ in range(4):
        tiempo = get_verb(1)

        

        if tiempo=="past":
           past = ["drank", "ate", "grew", "laughed", "thought",
                    "ran", "slept", "talked", "walked", "wrote"]  

           for _ in range(11):
              verbo =get_verb(1)
              assert verbo in past

        if tiempo=="future":
            future = ["will drink", "will eat", "will grow", "will laugh",
                      "will think", "will run", "will sleep", "will talk",
                      "will walk", "will write"]  
            for _ in range(11):
              verbo =get_verb(1)  
              assert verbo in future

        if tiempo == "present":
            present_1 = ["drinks", "eats", "grows", "laughs", "thinks",
                         "runs", "sleeps", "talks", "walks", "writes"] 
            for _ in range(11):
              verbo =get_verb(1)  
              assert verbo in present_1




    
        tiempo = get_verb(2)
        
        if tiempo=="past":
           past = ["drank", "ate", "grew", "laughed", "thought",
                    "ran", "slept", "talked", "walked", "wrote"]   
           for _ in range(11):
              verbo=get_verb(2)
              assert verbo in past

        if tiempo=="future":
            future = ["will drink", "will eat", "will grow", "will laugh",
                      "will think", "will run", "will sleep", "will talk",
                      "will walk", "will write"]  
            for _ in range(11):
              verbo=get_verb(2)  
              assert verbo in future

        if tiempo=="present":
           present = ["drink", "eat", "grow", "laugh", "think",
                      "run", "sleep", "talk", "walk", "write"] 
           for _ in range(11):  
              verbo=get_verb(2)       
              assert verbo in present
       
def test_get_preposition():
    prepo =[ "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(31):
        prep = get_preposition()
        assert prep in prepo
    

def test_get_prepositional_phrase():
    
        frase=[" the car.", "the evening.", "my home.", "the park.", "the work.", "my hand.",
                 "one child."]
        for _ in range(8):
            prep_phrase= get_prepositional_phrase(1)
            assert prep_phrase in frase

        frases=["many cars.", " many rabbits.", "a lot of dogs.", "some cats"]
        for _ in range(5):
             prep_phrase= get_prepositional_phrase(2)
             assert prep_phrase in frases

          

def test_get_adjective():
    
    adj_list = ["beautiful", "happy", "tall", "suspicious", "big", "small"]
    for _ in range(7):
        adj= get_adjective(1)
        assert adj in adj_list
       
   
    adjs_list=[ "beautifuls", "happies", "talls", "braves", "handsomes"] 
    for _ in range(6):
        adj= get_adjective(2)
        assert adj in adjs_list
        
    

      
             
    

pytest.main(["-v", "--tb=line", "-rN", __file__])