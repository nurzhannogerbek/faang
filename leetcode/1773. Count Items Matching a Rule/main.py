from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], rule_key: str, rule_value: str) -> int:
        rules = {
            'type': 0,
            'color': 1,
            'name': 2
        }
        count = 0
        for item in items:
            if item[rules[rule_key]] == rule_value:
                count += 1
        return count
