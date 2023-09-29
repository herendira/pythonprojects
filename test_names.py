"""
# File: given_name.py
# Author: Herendira Gomez
# Class: CSE111 
# Assignment purpose: Testing functions 

"""
from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Carlos Gerardo", "Gonzales") == "Gonzales;Carlos Gerardo"
    assert make_full_name("Zak-Niktee", "Gomez Herrera") == "Gomez Herrera;Zak-Niktee"
    assert make_full_name("Nao", "Ishi") == "Ishi;Nao"
#Combines a person’s given name and family name into one string with the family name first

def test_extract_family_name():
    assert extract_family_name("Gonzales;Carlos Gerardo") == "Gonzales"
    assert extract_family_name("Gomez Herrera;Zak-Niktee") == "Gomez Herrera"
    assert extract_family_name("Ishi;Nao") == "Ishi"

def test_extract_given_name():
    assert extract_given_name("Gonzales;Carlos Gerardo") == "Carlos Gerardo"
    assert extract_given_name("Gomez Herrera;Zak-Niktee") == "Zak-Niktee"
    assert extract_given_name("Ishi;Nao") == "Nao"    


# def test_extract_given_name():
# #Extracts a person’s given name from his full name
pytest.main(["-v", "--tb=line", "-rN", __file__])