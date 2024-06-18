# Student ID: 011118163

import csv
from datetime import datetime, time, timedelta

from classes.HashTable import HashTable
from classes.package import Package
from classes.truck import Truck


# creating package objects then loading into hashtable
def load_packages(file, hashtable):

    # parsing CSV file
    with open(file) as package_info:
        package_data = csv.reader(package_info)

        # skip the header row
        next(package_data)  

        # loop through package data
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


# retrieving address from CSV file
def retrieve_address(address):

    # parsing through CSV file
    with open("CSV/WGUPS_Addresses.csv", encoding='utf-8-sig') as csvfile_addresses:
        CSV_Addresses = csv.reader(csvfile_addresses)
        CSV_Addresses = list(CSV_Addresses)

    # appending addresses to list
    for row in CSV_Addresses:
        if address in row[2]:
            return int(row[0])


# calcuating distance between addresses
def calculating_distance(x, y):

    #parsing through CSV file
    with open("CSV/WGUPS_Distances.csv", encoding='utf-8-sig') as csvfile_distances:
        CSV_Distances = csv.reader(csvfile_distances)
        CSV_Distances = list(CSV_Distances)

    # calculating distances
    try:
        distance = CSV_Distances[x][y]
        if distance == '':
            distance = CSV_Distances[y][x]
        return float(distance)
    
    # error exception
    except IndexError:
        return float('inf')
    except ValueError:
        return float('inf')
    

# main algorithmn 
def deliver_package(truck, package_hashtable):

    # create empty list of undelivered
    undelivered = []

    # loop through packages and append to list
    for package_id in truck.packages:
        package = package_hashtable.lookup(package_id)
        if package:
            undelivered.append(package)
        else:
            print(f"Package ID {package_id} not found in hash table")

    while len(undelivered) > 0:
        # initializing address and package variables
        next_address_distance = float('inf')
        next_package = None

        # looping through undelivered and adding nearest package to truck packages
        for package in undelivered:
            current_address_index = retrieve_address(truck.address)
            package_address_index = retrieve_address(package.address)
            if current_address_index is not None and package_address_index is not None:
                distance = calculating_distance(current_address_index, package_address_index)
                if distance < next_address_distance:
                    next_address_distance = distance
                    next_package = package

        if next_package:

            # adds next package to truck package list
            truck.packages.append(next_package.package_id)

            # removes package from undelivered list
            undelivered.remove(next_package)

            # adds mileage to truck object
            truck.mileage += next_address_distance

            # updates truck's address attribute
            truck.address = next_package.address

            # Converts truck time to datetime for arithmetic
            truck_datetime = datetime.combine(datetime.today(), truck.time) + timedelta(hours=next_address_distance / truck.speed)

            # Updates truck time for delivery
            truck.time = truck_datetime.time()

            # Updates package delivery and departure time with truck object
            next_package.delivery_time = truck.time
            next_package.departure_time = truck.depart_time

# function to print the total mileage of all trucks
def print_total_mileage(truck1, truck2, truck3):
    print(f"Total mileage for truck1: {truck1.mileage}")
    print(f"Total mileage for truck2: {truck2.mileage}")
    print(f"Total mileage for truck3: {truck3.mileage}")
    print(f"Total mileage for all trucks: {truck1.mileage + truck2.mileage + truck3.mileage}")


# function for UI menu
def print_menu():
    print("\nMain Menu:")
    print("1. Show the total mileage traveled by all trucks")
    print("2. Show the delivery statuses of packages by time")
    print("3. Show the delivery times of all packages")
    print("4. Exit")


# main function
def main():

    # creating package hashtable
    package_hashtable = HashTable()

    # loading packages into hashtable
    load_packages("CSV/WGUPS_Package_File.csv", package_hashtable)

    # creating truck objects loaded with packages
    truck1 = Truck(0.0, "4001 South 700 East", time(8, 0), [25, 10, 19, 36, 1, 40, 11, 28, 20, 34, 3, 2, 21])
    truck2 = Truck(0.0, "4001 South 700 East", time(8, 0), [15, 35, 22, 26, 16, 17, 7, 38, 14, 30, 31, 9, 18])
    truck3 = Truck(0.0, "4001 South 700 East", time(10, 20), [32, 24, 8, 13, 6, 27, 23, 12, 33, 5, 29, 37, 4])

    # deliver the packages via truck
    deliver_package(truck1, package_hashtable)
    deliver_package(truck2, package_hashtable)

    # deliver with only two drivers at a time
    truck3.depart_time = min(truck1.depart_time, truck2.depart_time)
    deliver_package(truck3, package_hashtable)

    while True:

        # printing the welcome message UI menu
        print_menu()
        choice = input("Enter your choice: ")

        # printing total mileage for all trucks
        if choice == '1':
            print_total_mileage(truck1, truck2, truck3)

        # printing delivery status of packages
        elif choice == '2':
            time_input = input("Enter time to check package status (HH:MM): ")
            try:
                input_time = datetime.strptime(time_input, "%H:%M").time()

                # combine all packages from all trucks
                all_packages = truck1.packages + truck2.packages + truck3.packages

                # loop through packages
                for package_id in all_packages:

                    # lookup each package by ID
                    package = package_hashtable.lookup(package_id)
                    if package:
                        # check the delivery status based on input time
                        if package.delivery_time <= input_time:
                            status = "Delivered"
                        else:
                            status = "At hub" if package.departure_time > input_time else "En route"
                        print(f"Package {package.package_id} : {status} at {input_time}")
            except ValueError:
                print("Invalid entry. Please enter time in HH:MM format")

        elif choice == '3':

            print("All packages and their delivery times:")
            # combine all packages from all trucks
            all_packages = truck1.packages + truck2.packages + truck3.packages

            # loop through packages
            for package_id in all_packages:
                # lookup each package by ID
                package = package_hashtable.lookup(package_id)
                # print all packages + delivery times
                if package:
                    print(f"Package {package.package_id}: Delivery Time: {package.delivery_time}")

        # exiting the program
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


# calling the main function
if __name__ == "__main__":
    main()