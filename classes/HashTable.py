# creating hashtable data structure with insert and look up methods
class HashTable:
    def __init__(self, size=40):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, item):
        hash_key = self.hash_function(key)
        bucket = self.table[hash_key]
        key_exists = False
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = (key, item)
        else:
            bucket.append((key, item))

    def lookup(self, key):
        hash_key = self.hash_function(key)
        bucket = self.table[hash_key]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def get_all_items(self):
        items = []
        for bucket in self.table:
            items.extend(bucket)
        return items