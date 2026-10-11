class Solution:
  def trap(self, height: List[int]) -> int:
      lp = 0
      rp = 0
      water = 0
      new_arr = []
      while rp < len(height):
          while rp < len(height) - 1 and height[rp] <= height[rp + 1]:
              rp += 1
          lp = rp
          rp += 1
          while rp < len(height)  and height[lp] > height[rp]:
            rp += 1
          if rp == len(height):
            for i in range(rp - 1,lp - 1,-1):
              new_arr.append(height[i])
          else:
            smaller = min(height[lp],height[rp])
            water += (rp - lp - 1) * smaller
            for i in range(lp + 1,rp):
                water -= height[i]

      if new_arr:
        new_lp = 0
        new_rp = 0
        while new_rp < len(new_arr):
          while new_rp < len(new_arr) - 1 and new_arr[new_rp] < new_arr[new_rp + 1]:
              new_rp += 1
          new_lp = new_rp
          new_rp += 1
          while new_rp < len(new_arr) and new_arr[new_lp] > new_arr[new_rp]:
              new_rp += 1
          if new_rp == len(new_arr):
            return water
          else:
              smaller = min(new_arr[new_lp],new_arr[new_rp])
              water += (new_rp - new_lp - 1) * smaller
              for i in range(new_lp + 1,new_rp):
                  water -= new_arr[i]

      return water
