# creating hashtable data structure with insert and look up methods
class HashTable:
    
    # initializes object with empty list
    def __init__(self, size=40):
        self.size = size
        self.table = [None] * size
    
    # hash function with package id
    def hash_function(self, package_id):
        return package_id % self.size

    # insert function using package id
    def insert(self, package_id, package):
        index = self.hash_function(package_id)
        if self.table[index] is None:
            self.table[index] = []
            
        # Append package to bucket list
        for kv in self.table[index]:
            if kv['package_id'] == package_id:
                kv.update(package)
                return True
        self.table[index].append(package)
        return True

    # look up function using package id
    def lookup(self, package_id):
        index = self.hash_function(package_id)
        if self.table[index] is not None:
            for package in self.table[index]:
                if package['package_id'] == package_id:
                    return package
        return None