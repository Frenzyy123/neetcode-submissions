class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_len = 1
        left = 0
        
        for right in range(1, len(arr)):
            # 1. Compare current element with previous
            # If they are equal, the window is ruined. Reset to 'right'.
            if arr[right] == arr[right - 1]:
                left = right
            
            # 2. Check the "turbulence" condition
            # If we are at the second element, or if the current comparison 
            # is NOT different from the previous comparison, we shrink the window.
            elif right > 1:
                # This check ensures the signs alternate:
                # (a > b < c) OR (a < b > c)
                # Mathematically: (arr[i-2] - arr[i-1]) * (arr[i-1] - arr[i]) < 0
                is_turbulent = (arr[right-2] > arr[right-1] < arr[right]) or \
                               (arr[right-2] < arr[right-1] > arr[right])
                
                if not is_turbulent:
                    # Pattern broke! The new window starts at the previous element.
                    left = right - 1
            
            # Update the max length found so far
            max_len = max(max_len, right - left + 1)
            
        return max_len