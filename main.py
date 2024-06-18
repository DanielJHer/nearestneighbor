# Student ID: 011118163

import csv
from package import Package
from truck import Truck

# loading the package data into hash table by parsing the csv file
def load_package_data(csv_file):

    # creating empty hash table
    package_data = {}

    # parsing csv file
    with open(csv_file, mode='r', encoding='utf-8-sig') as file:  
        csv_reader = csv.reader(file, delimiter=',')

        #Skip the header row
        headers = next(csv_reader)  

        # looping through csv fields and creating package object
        for row in csv_reader:
            try:
                package_id = int(row[0])
                address = row[1]
                city = row[2]
                state = row[3]
                zip_code = row[4]
                deadline = row[5]
                weight = float(row[6])
                special_notes = row[7]
                status = row[8]
                
                package = Package(package_id, address, city, state, zip_code, deadline, weight, special_notes, status)
                package_data[package_id] = package

            except ValueError as e:
                print(f"Error processing row: {row}, Error: {e}")

    return package_data

# testing and printing
csv_file = 'CSV/WGUPS_Package_File.csv'  

package_data = load_package_data(csv_file)
for package_id, package in package_data.items():
    print(f"Package ID: {package_id}, Details: {package}")