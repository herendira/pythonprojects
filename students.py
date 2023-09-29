"""
# File: students.py
# Author: Herendira Gomez
# Class: CSE111 
# Assignment purpose: open files

"""
import csv


def main():
   
    students_dict = read_dictionary("students.csv")
    #print(students_list)
    # for stu in students_list:
    #     tel=stu["id"]
    #     name=stu["name"]
    #     print(tel, name)
    print(students_dict)

    students=input("I Number: ")
    student=students.replace('-','',)
    print(student)
    s_a=len(student)
    print(s_a)



    if student in students_dict:
           s_a == len(students_dict[student])
           name= students_dict[student]
           print(name)
           
    else:
           if  s_a < 9:
               print("Invalid I-Number: too few digits")
           elif  s_a > 9:
                print("Invalid I-Number: too many digits") 
                
     
           else:
            print("Invalid I-Number")  
            

      
   
    



def read_dictionary(filename):

    student_id = []
    student_name=[]
    student_dict={}
     
    with open(filename) as csv_file:
        next(csv_file)#no tomo en cuenta la primera linea
        reader=csv.reader(csv_file)
        
        for row_list in reader:
            
            tel=row_list[0]
            
            name=row_list[1]
            #print(tel, name)
            student_id.append(tel)
            student_name.append(name)

            #student_list.append({"id":tel, "name":name})
            student_dict=dict(zip(student_id, student_name))
        #print(student_dict)
        

        return student_dict   
           
        

           
        

    

    
    
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """

if __name__ == "__main__":
     main()
   