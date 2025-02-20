class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        seen = set()
        res = 0

        for num in nums:
            base_ten_num = 0
            for i, bit in enumerate(num[::-1]):
                if bit == '1':
                    base_ten_num += 2**i
            seen.add(base_ten_num)
        
        for found in seen:
            if res == found:
                res += 1
        
        res_bits = bin(res)[2:]
        return "0"*(n-len(res_bits)) + res_bits
