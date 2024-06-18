# Student ID: 011118163

import csv
import datetime
from classes.HashTable import HashTable
from classes.package import Package
from classes.truck import Truck

# parsing CSV files and entering into lists
with open("CSV/WGUPS_Packages.csv") as csvfile_packages:
    CSV_Packages = csv.reader(csvfile_packages)
    CSV_Packages = list(CSV_Packages)

with open("CSV/WGUPS_Addresses.csv") as csvfile_addresses:
    CSV_Addresses = csv.reader(csvfile_addresses)
    CSV_Addresses = list(CSV_Addresses)

with open("CSV/WGUPS_Distances.csv") as csvfile_distances:
    CSV_Distances = csv.reader(csvfile_distances)
    CSV_Distances = list(CSV_Distances)

# creating package objects from CSV file then loading into hash table
def load_packages(file, hashtable):
    with open(file) as package_info:
        package_data = csv.reader(package_info)
        for package in package_data:
            package_id = int(package[0])
            package_address = package[1]
            package_city = package[2]
            package_state = package[3]
            package_zip = package[4]
            package_deadline = package[5]
            package_weight = package[6]
            package_status= "at hub"

            # creating package object with data
            package = Package(package_id, package_address, package_city, package_state, package_zip, package_deadline, package_weight, package_status)

            # inserting package data into hash table
            hashtable.insert(package_id, package)


# retrieving address from string of address
def retrieve_address(address):
    for row in CSV_Addresses:
        if address in row[2]:
            return int(row[0])

# calcuating distance between addresses
def calculating_distance(x,y):
    distance = CSV_Distances[x][y]
    if distance == '':
        distance = CSV_Distances[y][x]

    return float(distance) 

# creating package hashtable
package_hashtable = HashTable()

# loading packages into hashtable
load_packages("CSV/WGUPS_Package_File", package_hashtable)

# creating truck objects and loading with packages
truck1 = Truck.Truck(0.0, "4001 South 700 East", datetime.timedelta(hours=8), [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40]) 
                     
truck2 = Truck.Truck(0.0, "4001 South 700 East", datetime.timedelta(hours=10, minutes=20), [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39])

truck3 = Truck.Truck(0.0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5), [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33])

# delievering packages on trucks
def deliver_package(truck):




# def print_menu():
#     print("\nMain Menu:")
#     print("1. Show the status of all packages loaded onto each truck by time")
#     print("2. Show the total mileage traveled by all trucks")
#     print("3. Show the status of a single package by time")
#     print("4. Show the status of all packages by a specific time")
#     print("5. Exit")

# def main():

#     while True:
#         print_menu()
#         choice = input("Enter your choice: ")
#         if choice == '1':
#             handle_print_all_statuses_by_time()
#         elif choice == '2':
#             handle_total_mileage()
#         elif choice == '3':
#             handle_single_package_status()
#         elif choice == '4':
#             handle_print_all_statuses_by_time()
#         elif choice == '5' or choice.lower() == 'exit':
#             print("Exiting the program.")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()   