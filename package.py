# creating packages objects via pacakge class

class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, special_notes, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes
        self.status = status
        self.is_delivered = False

    def __repr__(self):
        return (f"Package({self.package_id}, {self.address}, {self.city}, {self.state}, {self.zip_code}, "
                f"{self.deadline}, {self.weight}, {self.special_notes}, {self.status})")