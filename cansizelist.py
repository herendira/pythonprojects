import math
def main(): #Strenght 3
   
    cans = [
        ["#1 Picnic", 6.83, 10.16, 0.28],
        ["#1 Tall", 7.78, 11.91, 0.43],
        ["#2", 8.73, 11.59, 0.45],
        ["#2.5", 10.32, 11.91, 0.61],
        ["#3 Cylinder", 10.79, 17.78, 0.86],
        ["#5", 13.02, 14.29, 0.83],
        ["#6Z", 5.4, 8.89, 0.22],
        ["#8Z short", 6.83, 7.62, 0.26],
        ["#10", 15.72, 17.78, 1.53],
        ["#211", 6.83, 12.38, 0.34],
        ["#300", 7.62, 11.27, 0.38],
        ["#303", 8.1, 11.11, 0.42]
    ]

    for line in range(len(cans)):
        listas=cans[line]
        

        for line in range(len(listas)):
            name=listas[0]
            radius_cm=listas[1]
            height_cm=listas[2]
            cost_dl=listas[3]
            costo=(compute_cost_efficiency(cost_dl,radius_cm,height_cm))
        print(costo)
            # for line in range(lista2):
            #     print(line)
                # linea1=lista2[0]
                # linea2=lista2[1]
                # print(linea1)
   

            #max(storage(radius_cm,height_cm))
        #print(costo,name)
        #print(stor, name)
        # costo1=-1
        # stor1=-1
        
        # name_cost=None
        # name_stor=None
           
        # if costo>costo1:
        #    costo1=costo
        #    name_cost=name
        #    print(name_cost)
        # else:
        #     print(costo, name_cost)
        # #      if stor>stor1:
        #    stor1=stor
        #         name_stor=name

    # print(f"The cheapest is: {costo1:.2f} and the biggest storage is:{name_cost}")
    # # print(f"Name: {name}, Cost ${costo:.2f}, Capacity: {stor:.2f} ml")
            


        
    #print("Best can size in cost efficiency:", max(storage(radius_cm,height_cm)))  
        
      

        
def compute_cost_efficiency(cost_dl,radius_cm,height_cm):
    return (compute_volume(radius_cm,height_cm)/compute_surface_area(radius_cm,height_cm))/cost_dl
    


def compute_volume(radius_cm,height_cm):
     return 3.141692*(radius_cm**2)*height_cm
    
def compute_surface_area(radius_cm,height_cm):
    return 6.283384*radius_cm*(radius_cm + height_cm)

def storage(radius_cm,height_cm):  
    return compute_volume(radius_cm,height_cm)/compute_surface_area(radius_cm,height_cm)
    
main()  
      