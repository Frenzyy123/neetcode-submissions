class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_number = len(position)
        save_speeds = {position[i] : speed[i] for i in range(len(position))}
        position.sort()
        times = []
        for i in range(len(position)):
            times.append((target - position[i])/save_speeds[position[i]])
        for i in range(len(times) - 1,0,-1):
            if  times[i] >= times[i - 1]:
                fleet_number -= 1
                times[i - 1] = times[i]
        return fleet_number