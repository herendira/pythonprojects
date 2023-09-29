print("1. I feel that I am a person of worth, at least on an equal plane with others.")
reponse1 = input("Enter D, d, a, or A: ") 
print("2. I feel that I have a number of good qualities.")
reponse2 = input("Enter D, d, a, or A: ")
print("3. All in all, I am inclined to feel that I am a failure.")
reponse3 = input("Enter D, d, a, or A: ")
total=1
if reponse1=="A":
   total=total+3

if reponse1=="a":
    total=total+2
if reponse1=="d":
     total=total+1
if reponse1=="D":
     total=total+0 
if reponse2=="A":
    total=total+3
if reponse2=="a":
    total=total+2
if reponse2=="d":
     total=total+1
if reponse2=="D":
     total=total+0       

print(total)     