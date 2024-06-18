# creating truck objects via truck class
class Truck:
    def __init__(self, mileage, address, depart_time, packages=None, capacity=16, speed=18, current_time=None):
        self.capacity = capacity
        self.speed = speed
        self.packages = packages if packages is not None else []
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.time = current_time if current_time is not None else depart_time

    def __repr__(self):
        package_ids = [p for p in self.packages]
        return f"Truck(Capacity: {self.capacity}, Packages: {package_ids})"