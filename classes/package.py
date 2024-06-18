# creating packages objects via package class

class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None

    def __repr__(self):
        return (f"Package({self.package_id}, {self.address}, {self.city}, {self.state}, {self.zip_code}, "
                f"{self.deadline}, {self.weight}, {self.status})")
    
    # updating status method comparing times
    def update_status(self, convert_timedelta):
        if self.delivery_time < convert_timedelta:
            self.status = "delivered"
        elif self.departure_time > convert_timedelta:
            self.status = "en route"
        else:
            self.status = "at hub"