class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProducts: List[int] = []

        prefixProduct = 1 # index included
        prefixProducts.append(prefixProduct)
        for num in nums:
            prefixProduct = num * prefixProduct
            prefixProducts.append(prefixProduct)
        
        # prefixProduct length n + 1: 1, a0, a0a1 ...., a0....an-1

        suffixProducts: Lis[int] = []
        suffixProduct = 1
        suffixProducts.append(suffixProduct)
        for num in reversed(nums):
            suffixProduct = num * suffixProduct
            suffixProducts.append(suffixProduct)
        

        # suffixProduct Lenght n + 1: 1, an-1, an-1an-2,.., an-a.. a0

        result: List[int] = []
        n = len(nums)

        for index in range(n):
            result.append(prefixProducts[index] * suffixProducts[n - index - 1])
        

        return result

