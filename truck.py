# truck objects via truck class
class Truck:
    def __init__(self, truck_id, capacity=16, speed=18):
        self.truck_id = truck_id
        self.capacity = capacity
        self.speed = speed
        self.packages = []
        
    def load_package(self, package):
        if len(self.packages) < self.capacity:
            self.packages.append(package)
        else:
            print(f"Truck {self.truck_id} is full. Cannot load package {package.package_id}.")

    def __repr__(self):
        return f"Truck({self.truck_id}, Packages: {[p.package_id for p in self.packages]})"