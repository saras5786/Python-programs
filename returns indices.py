class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# This part runs only in IDLE
if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    target = int(input("Enter target: "))
    
    obj = Solution()
    print("Indices:", obj.twoSum(nums, target))
