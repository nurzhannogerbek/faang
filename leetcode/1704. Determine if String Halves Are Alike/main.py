class Solution:
    def halvesAreAlike(self, original_string: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        first_count = 0
        second_count = 0
        for i in range(len(original_string) // 2):
            if original_string[i] in vowels:
                first_count += 1
        for i in range(len(original_string) // 2, len(original_string)):
            if original_string[i] in vowels:
                second_count += 1
        return first_count == second_count
