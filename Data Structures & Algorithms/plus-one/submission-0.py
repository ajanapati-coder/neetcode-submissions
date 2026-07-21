class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_version = ""

        for digit in digits:
            str_version += str(digit)

        number = int(str_version) + 1

        new_str = str(number)

        result = [int(char) for char in list(new_str)]

        return result