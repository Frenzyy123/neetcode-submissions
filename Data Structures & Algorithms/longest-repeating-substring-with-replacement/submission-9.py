class Solution():
  def characterReplacement(self,s: str, k: int) -> int:
    lp = 0
    res = 0
    freq = {}
    most_frequent = 0
    for rp in range(len(s)):
      if s[rp] not in freq:
        freq[s[rp]] = 1
      else:
        freq[s[rp]] += 1
      most_frequent = max(most_frequent,freq[s[rp]])



      if rp - lp + 1 - most_frequent <= k:
        res = max(res, rp - lp + 1)
      else:
        freq[s[lp]] -= 1
        lp += 1

    return res
