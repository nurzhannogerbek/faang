class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        words_count = len(words)
        total_spaces_count = 0
        for letter in text:
            if letter == ' ':
                total_spaces_count += 1
        if words_count == 1:
            return words[0] + ' ' * total_spaces_count
        else:
            inner_spaces_count = total_spaces_count // (words_count - 1)  # Целочисленное деление.
            right_spaces_count = total_spaces_count % (words_count - 1)  # Остаток от деления.
            return (' ' * inner_spaces_count).join(words) + ' ' * right_spaces_count
