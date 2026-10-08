class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_len = 1
        left = 0
        
        for right in range(1, len(arr)):
            if arr[right] == arr[right - 1]:
                left = right
            
            elif right > 1:
                is_turbulent = (arr[right-2] > arr[right-1] < arr[right]) or \
                               (arr[right-2] < arr[right-1] > arr[right])
                
                if not is_turbulent:
                    left = right - 1
            
            max_len = max(max_len, right - left + 1)
            
        return max_len