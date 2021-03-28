class Solution:
    def defangIPaddr(self, address: str) -> str:
        # https://www.geeksforgeeks.org/defanged-version-of-internet-protocol-address/
        defangIP = str()
        for character in address:
            if character == '.':
                defangIP += '[.]'
            else:
                defangIP += character
        return defangIP
        # return address.replace('.', '[.]')
