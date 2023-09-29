import csv
from datetime import datetime
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
BLACK = '\033[30m'

# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    students_list=read_compound_list("pupils.csv")
    print(RED+"LIST OF STUDENTS")
    print_list(students_list)
    print()
    #print(students_list)
    #for student in students_list:
        #print(student)
    #print()
   # print()
    #lista=sorted(students_list, key=students_list[BIRTHDATE_INDEX])  
    #print(lista)  
    # dob1=[]
    # for row in students_list:
    #     dob=row[BIRTHDATE_INDEX]
    #     sn=row[SURNAME_INDEX]
    #     gn=row[GIVEN_NAME_INDEX]
    #     dob1.append(dob)
    #     dob1.append(sn)
    #     dob1.append(gn)
    #print(dob1)
    #for i in dob1:
        #print(i)
   
    
    #students_list.sort()#en orden alfabetico los nombre estan

    #print(students_list)
    #ln=sorted(dob1)
    #print(ln)
    #for row in ln:
        #print(row)
    GIVEN_NAME_INDEX = 0
    SURNAME_INDEX = 1    
    BIRTHDATE_INDEX = 2   
    combine_names = lambda student_list: \
        f"{student_list[GIVEN_NAME_INDEX]}, {student_list[SURNAME_INDEX]}"
    old_young=lambda student:student[BIRTHDATE_INDEX]
    alfab=lambda student:student[GIVEN_NAME_INDEX]
    # Sort the list by the combined key of surname, given_name.
    #sorted_list = sorted(students_list, key=combine_names)
    sorted_list = sorted(students_list, key=old_young)
    sorted_list2=sorted(sorted_list, reverse=True)#de z a a
    sor_alf=sorted(students_list,key=alfab)
    print()
    print(WHITE+"STUDENTS BY ALFABETICAL ORDER")
    print_list(sor_alf)
    print()
    print(GREEN+"STUDENTS BY YEAR OF BIRTH")
    print_list(sorted_list)
    sorted_list3=month_day(students_list)
    print()
    print(MAGENTA+"LIST OF STUDENTS BY MONTH OF BIRTH")
    print_list(sorted_list3)

    # Print the list.
    #for stu in sorted_list:
        #print(stu)
def month_day(students_list):
    
    # Define a nested function that extracts
    # a student's birthdate without the year.
    def extract_month_and_day(student):
        birthdate_string = student[BIRTHDATE_INDEX]
        month_and_day = birthdate_string[5:]
        return month_and_day

    # Call the sorted function to sort the list
    # of students by their birth month and day.
    sorted_list = sorted(students_list, key=extract_month_and_day)

    # Return the sorted list.
    return sorted_list
# def month_day(students_list):
#     dob=students_list[BIRTHDATE_INDEX]   
#     dm=dob[5:] 
#     sorted_list3=sorted(students_list, key=dm)
#     return sorted_list3
   


  

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)
            
    return compound_list

def print_list(compound_list):

    for row in compound_list:
        print(row)



if __name__ == "__main__":
    main()
