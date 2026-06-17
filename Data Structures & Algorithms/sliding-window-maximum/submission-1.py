from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque()
        output = []
        iterator = 0
        k_iter = 0
        while iterator < len(nums):
            while iterator < len(nums) and k_iter < k:
                while que and nums[iterator] > nums[que[-1]]:
                    que.pop()
                que.append(iterator)
                iterator += 1
                k_iter += 1
            k_iter -= 1
            output.append(nums[que[0]])
            if len(que) == k  or iterator - que[0] == k:
                que.popleft()
        return output
                