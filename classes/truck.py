# creating truck objects via truck class
class Truck:
    def __init__(self, mileage, address, depart_time, capacity=16, speed=18, packages=None):
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.capacity = capacity
        self.speed = speed
        # Initialize with provided list or as an empty list
        self.packages = packages if packages is not None else []  
        
    def __repr__(self):
        # Assuming each package in self.packages has a package_id attribute
        package_ids = [p['package_id'] for p in self.packages]
        return f"Truck(Capacity: {self.capacity}, Packages: {package_ids})"