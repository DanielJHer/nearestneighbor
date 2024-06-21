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
            package_notes = package[7]

            # creating package object with data
            package = Package(package_id, package_address, package_city, package_state, package_zip, package_deadline, package_weight, package_status, package_notes)

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

    # clears package list
    truck.packages.clear()

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
    print("2. Show the delivery info of packages by time")
    print("3. Exit")


# main function
def main():

    # creating package hashtable
    package_hashtable = HashTable()

    # loading packages into hashtable
    load_packages("CSV/WGUPS_Package_File.csv", package_hashtable)

    # creating truck objects loaded with packages
    truck1 = Truck(0.0, "4001 South 700 East", time(8, 0), [1, 2, 8, 13, 15, 17, 19, 20, 21, 22, 24, 30, 38, 40])
    truck2 = Truck(0.0, "4001 South 700 East", time(9, 5), [3, 4, 6, 14, 18, 23, 25, 27, 28, 32, 33, 37, 39])
    truck3 = Truck(0.0, "4001 South 700 East", time(10, 40), [5, 7, 9, 10, 11, 12, 16, 26, 29, 31, 34, 35, 36])

    # deliver the packages via truck
    deliver_package(truck1, package_hashtable)
    deliver_package(truck2, package_hashtable)
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

                        # determine which truck the package is on
                        truck_name = "Truck 1" if package_id in truck1.packages else "Truck 2" if package_id in truck2.packages else "Truck 3"

                        # print package info
                        print(f"Package ID: {package.package_id}")
                        print(f"Package Status: {status} at {input_time}")
                        print(f"Address: {package.address}")
                        print(f"City: {package.city}")
                        print(f"State: {package.state}")
                        print(f"ZIP: {package.zip_code}")
                        print(f"Weight: {package.weight}")
                        print(f"Notes: {package.special_notes}")
                        print(f"Delivery Deadline: {package.deadline}")
                        print(f"Delivery Time: {package.delivery_time if package.delivery_time else 'Not delivered yet'}")
                        print(f"Loading Time: {package.departure_time if package.departure_time else 'Not loaded yet'}")
                        print(f"Truck Name: {truck_name}")
                        print("-" * 40)
            except ValueError:
                print("Invalid entry. Please enter time in HH:MM format")

        # exiting the program
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


# calling the main function
if __name__ == "__main__":
    main()