"""
# File: receipt.py
# Author: Herendira Gomez
# Class: CSE111 
# Assignment purpose: Call function

"""
from datetime import datetime
import csv, random

def main():
    try:
      index=0
      products = products_dict=read_dictionary("products.csv", index)
      
    #print(products_dict)
      for item in products.items():
        key=item[0]
        value=item[1]
        #lista_prod=value[1]
        #precio=value[2]
      print(" \n\n      WELCOME TO EPICERIE PERE NATURE     ")  
      print("                 Shopping list                  \n")
      lista(products_dict)
      time()


    except (FileNotFoundError, PermissionError) as error:
        print(error)
        print("Please choose a different file.")
    
    except ( KeyError) as error:
        print(f"Error: unknown product ID in the request.csv file")
        print(f"{error} ")
    

def lista(products_dict): 
   
      
       with open("request.csv", "rt") as csv_file:
           next(csv_file)#no tomo en cuenta la primera linea
           reader=csv.reader(csv_file)
           quantite_total=0
           amount_item=0
           for row_list in reader:
            total_item=float
            quantite=float(row_list[1])
            item_number=row_list[0]
            
            item=products_dict[row_list[0]] #busca en el dict, la linea del csv file
            number=row_list[0]
            name=item[1]
            price=float(item[2])
            
            total_item=price*quantite
            print(f'{name}: {quantite:.0f} @ {price} {total_item} ')

            #computing part
            quantite_total=quantite+quantite_total
            amount_item=amount_item+total_item
            tax=amount_item*0.06
            total=amount_item+tax
           print()
           print()
           print(f'Number of Items: {quantite_total:.0f}')
           print(f'Subtotal: {amount_item:.2f}')
           print(f'Sale Tax: {tax:.2f}')
           print(f'Total: {total:.2f}\n\n')
       
           print('Thank you for shopping at EPICERIE PERE NATURE.\n\n')
           

           reponse=input("Do you want to help us filling a short survey? yes/not ")
           if reponse.lower()=="yes":
              survey()

             
           else:
               print("\n\nHave a nice day!!\n\n")    

def survey():
    phone=str
    #current_date=time()
    name=input("What is your name? ")
    phone=input("What is you Phone Number? ")
    satis=input("What is your level of satisfaccion from 1 to 5? ( 1=lower, 5=high) ")
    product=input("What is one product you want and we have not? ")
    comment=input("Any comment? ")
    print("\nThanks for your time!! You will have an extra 10 off in your next visit with this code \n")
    code=str(random.sample(range(10000,20000),1))
    print(f"{code}\n")
   

    with open("survey.txt", "at") as survey_file:
          #I did it in this way because I dont know it didnt work in the other way
          
          survey_file.write(name)
          survey_file.write(phone)
          survey_file.write(satis)
          survey_file.write(product)
          survey_file.write(comment)
          survey_file.write(str(code))
          
          print(f"\nClient Name: {name}", file=survey_file)
          print(f"Phone Number: {phone}", file=survey_file)
          print(f"Satisfaction level:{satis}", file=survey_file)
          print(f"Product Inexist: {product}", file=survey_file)
          print(f"Assigned code: {code}", file=survey_file)

    
   
def read_dictionary(filename, key_column_index):
    dictionary={}
    key_column_index=0
    with open(filename) as csv_file:
        next(csv_file)#no tomo en cuenta la primera linea
        reader=csv.reader(csv_file)
       
        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key]=row_list
          
    
      
    return(dictionary)   



def time():
    ahora=datetime.now()
    print(f"{ahora:%A %b %d %Y, %I:%M %p}\n\n")
    

   

if __name__ == "__main__":
     main()