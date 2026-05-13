class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i, num in enumerate(nums):
            arr.append((num, i))

        arr.sort()

        l, r = 0, len(arr) - 1

        while l < r:

            currSum = arr[l][0] + arr[r][0]

            if currSum > target:
                r -= 1

            elif currSum < target:
                l += 1

            else:
                i1 = arr[l][1]
                i2 = arr[r][1]

                return sorted([i1, i2])