import csv


# def main():
   
#     name="1 Picnic"
#     radius_cm=6.83
#     height_cm=10.16
#     cost_dl=0.28
#     storage_efficiency=compute_volume(radius_cm,height_cm)/compute_surface_area(radius_cm,height_cm)
#     #print(f"{name}: {storage_efficiency:.2f}")
#     storage(name,radius_cm,height_cm)#strength 1
#     print(f"{name}: {storage_efficiency:.2f} cost: ${compute_cost_efficiency(cost_dl,radius_cm,height_cm):.2f}")


#     name="1 Tall"
#     radius_cm=7.78
#     height_cm=11.91
#     cost_dl=0.43
#     storage_efficiency=compute_volume(radius_cm,height_cm)/compute_surface_area(radius_cm,height_cm)
#     #compute_cost_efficiency(cost_dl,radius_cm,height_cm)#strength 2 reponse 10
#     print(f"{name}: {storage_efficiency:.2f} cost: ${compute_cost_efficiency(cost_dl,radius_cm,height_cm):.2f}")

   
#     name="2"
#     radius_cm=8.73
#     height_cm=11.59
#     cost_dl=0.45
#     storage_efficiency=compute_volume(radius_cm,height_cm)/compute_surface_area(radius_cm,height_cm)
#     print(f"{name}: {storage_efficiency:.2f}")
#     print(f"{name}: {storage_efficiency:.2f} cost: ${compute_cost_efficiency(cost_dl,radius_cm,height_cm):.2f}")

#     name="2.5"
#     radius_cm=10.32
#     height_cm=11.91
#     cost_dl=0.61
#     storage_efficiency=compute_volume(radius_cm,height_cm)/compute_surface_area(radius_cm,height_cm)
#     print(f"{name}: {storage_efficiency:.2f}")
#     print(f"{name}: {storage_efficiency:.2f} cost: ${compute_cost_efficiency(cost_dl,radius_cm,height_cm):.2f}")

#     name="3 Cylinder"
#     radius_cm=10.79
#     height_cm=17.78
#     cost_dl=0.86
#     storage_efficiency=compute_volume(radius_cm,height_cm)/compute_surface_area(radius_cm,height_cm)
#     print(f"{name}: {storage_efficiency:.2f}")
#     print(f"{name}: {storage_efficiency:.2f} cost: ${compute_cost_efficiency(cost_dl,radius_cm,height_cm):.2f}")

#     name="5"
#     radius_cm=13.02
#     height_cm=14.29
#     cost_dl=0.83
#     storage_efficiency=compute_volume(radius_cm,height_cm)/compute_surface_area(radius_cm,height_cm)
#     print(f"{name}: {storage_efficiency:.2f}")
#     print(f"{name}: {storage_efficiency:.2f} cost: ${compute_cost_efficiency(cost_dl,radius_cm,height_cm):.2f}")

#     name="6Z"
#     radius_cm=5.40
#     height_cm=8.89
#     cost_dl=0.22
#     storage_efficiency=compute_volume(radius_cm,height_cm)/compute_surface_area(radius_cm,height_cm)
#     print(f"{name}: {storage_efficiency:.2f}")
#     print(f"{name}: {storage_efficiency:.2f} cost: ${compute_cost_efficiency(cost_dl,radius_cm,height_cm):.2f}")

#     name="8Z short"
#     radius_cm=6.83
#     height_cm=7.62
#     cost_dl=0.26
#     storage_efficiency=compute_volume(radius_cm,height_cm)/compute_surface_area(radius_cm,height_cm)
#     print(f"{name}: {storage_efficiency:.2f}")
#     print(f"{name}: {storage_efficiency:.2f} cost: ${compute_cost_efficiency(cost_dl,radius_cm,height_cm):.2f}")

#     name="10"
#     radius_cm=15.72
#     height_cm=17.78
#     cost_dl=1.53
#     storage_efficiency=compute_volume(radius_cm,height_cm)/compute_surface_area(radius_cm,height_cm)
#     print(f"{name}: {storage_efficiency:.2f}")
#     print(f"{name}: {storage_efficiency:.2f} cost: ${compute_cost_efficiency(cost_dl,radius_cm,height_cm):.2f}")

#     name="211"
#     radius_cm=6.83
#     height_cm=12.38
#     cost_dl=0.34
#     storage_efficiency=compute_volume(radius_cm,height_cm)/compute_surface_area(radius_cm,height_cm)
#     print(f"{name}: {storage_efficiency:.2f}")
#     print(f"{name}: {storage_efficiency:.2f} cost: ${compute_cost_efficiency(cost_dl,radius_cm,height_cm):.2f}")

#     name="300"
#     radius_cm=7.62
#     height_cm=11.27
#     cost_dl=0.38
#     storage_efficiency=compute_volume(radius_cm,height_cm)/compute_surface_area(radius_cm,height_cm)
#     print(f"{name}: {storage_efficiency:.2f}")
#     print(f"{name}: {storage_efficiency:.2f} cost: ${compute_cost_efficiency(cost_dl,radius_cm,height_cm):.2f}")

#     name="303"
#     radius_cm=8.10
#     height_cm=11.11
#     cost_dl=0.42
#     storage_efficiency=compute_volume(radius_cm,height_cm)/compute_surface_area(radius_cm,height_cm)
#     print(f"{name}: {storage_efficiency:.2f}")
#     print(f"{name}: {storage_efficiency:.2f} cost: ${compute_cost_efficiency(cost_dl,radius_cm,height_cm):.2f}")



# def compute_cost_efficiency(cost_dl,radius_cm,height_cm):
#     return (compute_volume(radius_cm,height_cm)/compute_surface_area(radius_cm,height_cm))/cost_dl
    


# def compute_volume(radius_cm,height_cm):
#      return 3.141692*(radius_cm**2)*height_cm
    
# def compute_surface_area(radius_cm,height_cm):
#     return 6.283384*radius_cm*(radius_cm + height_cm)

# def storage(name,radius_cm,height_cm):  
#     storage_efficiency=compute_volume(radius_cm,height_cm)/compute_surface_area(radius_cm,height_cm)
#     print(f"{name}: {storage_efficiency:.2f}")

# main()

# with open("products.csv") as csv_file:
#         next(csv_file)#no tomo en cuenta la primera linea
#         reader=csv.reader(csv_file)
#         dictionary={}
#         for row_list in reader:
#             key = row_list[0]
#             dictionary[key]=row_list
#         print(dictionary)

students = {
    "10-450-1203": "Jorge Soares",
    "75-421-2310": "Abdul Ali",
    "07-103-5621": "Michelle Davis"
}
students["81-298-9238"] = "Sama Patel"
print(students)
n= len(students)
print(n)
#cosmic space villains
        
