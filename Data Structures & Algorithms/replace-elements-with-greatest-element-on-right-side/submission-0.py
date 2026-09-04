class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = arr[-1]
        save = None
        for i in range(len(arr) - 1,-1,-1):
            if arr[i] > curr_max:
                save = arr[i]
            arr[i] = curr_max
            if save is not None:
                curr_max = save
        arr[-1] = -1
        return arr