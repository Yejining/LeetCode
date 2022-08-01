class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_str = [str(i) for i in digits]
        arr_str = list(str(int(''.join(digits_str)) + 1))
        return [int(i) for i in arr_str]