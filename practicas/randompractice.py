import random

for i in range(0,5):
    print(round(random.uniform(0,10)))
    
wordslist = ["boy", "girl", "cat", "dog", "bird", "house"]
print(wordslist)    
for i in wordslist:
    lista=random.choice(wordslist)
wordslist.append(lista)
print(wordslist)

        