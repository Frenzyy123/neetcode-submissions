class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    sums = {0:1}
    suma = 0
    subs = 0
    for i in nums:
        suma += i
        if suma - k in sums:
            subs += sums[suma - k]
        if suma in sums:
            sums[suma] += 1
        else:
            sums[suma] = 1
    return subs

