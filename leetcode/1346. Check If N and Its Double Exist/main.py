class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hash_table = {}
        for i in arr:
            if hash_table.get(i + i):
                return True
            if i%2 == 0 and hash_table.get(i // 2):
                return True
            hash_table[i] = True
        return False
