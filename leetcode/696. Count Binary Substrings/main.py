import itertools


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [len(list(grp)) for _, grp in itertools.groupby(s)]
        return sum(min(a, b) for a, b in zip(groups[:-1], groups[1:]))
