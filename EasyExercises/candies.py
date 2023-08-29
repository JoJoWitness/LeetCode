class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        result =[]
        for item in candies:
            result.append(item+extraCandies >=maxCandies )
        return result