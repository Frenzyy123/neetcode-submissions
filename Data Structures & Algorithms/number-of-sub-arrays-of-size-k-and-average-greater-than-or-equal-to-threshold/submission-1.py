class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr_sum = 0
        lp = 0
        rp = 0
        output = 0
        for rp in range(len(arr)):
            curr_sum += arr[rp]
            if rp - lp + 1 == k:
                if curr_sum / k >= threshold:
                    output += 1
                curr_sum -= arr[lp]
                lp += 1
        return output
