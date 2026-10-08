class Solution:
  def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        l = 0
        r = 1
        prev = ''
        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != '>':
                res = max(res,r - l + 1)
                prev = ">"
                r += 1
            elif arr[r - 1] < arr[r] and prev != '<':
                res = max(res,r - l + 1)
                prev = '<'
                r += 1
            elif arr[r - 1] > arr[r] and prev == '>':
                l = r - 1
                r += 1
            elif arr[r - 1] < arr[r] and prev == '<':
                l = r - 1
                r += 1
            elif arr[r - 1] == arr[r]:
                l = r
                r += 1
                prev = "="
        return res

