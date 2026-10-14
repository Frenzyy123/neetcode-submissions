class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    suma  = 0
    subs = {0 : 1}
    res = 0
    for n in nums:
      suma += n
      if suma - k in subs:
          res += subs[suma - k]
      if suma in subs:
          subs[suma] += 1
      else:
          subs[suma] = 1

    return res

