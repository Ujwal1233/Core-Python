class Solution:
    def to_upper(self, str):
        result = ""
        for char in str:
            if 'a' <= char <= 'z':
                result += chr(ord(char) - 32)
            else:
                result += char
        return result
