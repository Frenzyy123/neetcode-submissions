class Solution:
  def characterReplacement(self,s: str, k: int) -> int:
    lp = 0
    res = 0
    freq = {}
    for rp in range(len(s)):
      if s[rp] not in freq:
        freq[s[rp]] = 1
      else:
        freq[s[rp]] += 1

      most_frequent = 0
      for char in freq:
        if freq[char] > most_frequent:
          most_frequent = freq[char]

      if rp - lp + 1 - most_frequent <= k:
        res = max(res, rp - lp + 1)
      else:
        freq[s[lp]] -= 1
        lp += 1

    return res