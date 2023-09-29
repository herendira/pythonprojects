"""
# File: nature.py
# Author: Herendira Gomez
# Class: CSE111 
# Assignment purpose: Functions 

"""
def main():
    print("Disagree strongly 1")
    print("Disagree little   2")
    print("Neither agree     3")
    print("Agree a little    4")
    print("Agree Strongly    5")

    r1 = int(input("My ideal vacation spot would be a remote, wilderness area. "))
    r2 = int(input("I always think about how my actions affect the environment. "))
    r3 = int(input("My connection to nature and the environment is a part of my spirituality. "))
    r4 = int(input("I take notice of wildlife wherever I am. "))
    r5 = int(input("My relationship to nature is an important part of who I am. "))
    r6 = int(input("I feel very connected to all living things and the earth. "))

    total=score(r1,r2,r3,r4,r5,r6)

    print(f"Your score is: {total}")
    print("The lowest possible score is 21.")
    print("The highest possible score is 105.")

def score(r1,r2,r3,r4,r5,r6):
    total=(r1+r2+r3+r4+r5+r6)
    return total

main()