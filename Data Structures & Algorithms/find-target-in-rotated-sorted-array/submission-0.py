class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the pivot
        l, r = 0, len(nums) - 1
        pivot = 0
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[m+1]:
                pivot = m
                break
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        else:
            pivot = l

        def binary_search(l, r):
            while l <= r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return m
            return -1

        #run bs on left half of pivot
        left = binary_search(0, pivot)
        if left == -1:
            return binary_search(pivot + 1, len(nums)-1)
        return left

        # if no ans then run bs on right half of pivot