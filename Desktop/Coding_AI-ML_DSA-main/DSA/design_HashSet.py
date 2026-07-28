class MyHashSet:

    def __init__(self):
        self.size= 1000
        self.bucket =[[] for _ in range(self.size)]
        
    def _hash(self,key: int):
        return key % self.size
        

    def add(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.bucket[index]
        
        if key not in bucket:
            bucket.append(key)
        

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.bucket[index]
        
        if key in bucket:
            bucket.remove(key)
        

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        bucket = self.buckets[index]
        
        return key in bucket
    
'''APPROACH - 

We start off by creating 1000 buckets (empty list in an array)
Apply hash function -  key % 1000 gives buckt index 0-999
find bucket using hash and perfrom add, remove etc

'''
        