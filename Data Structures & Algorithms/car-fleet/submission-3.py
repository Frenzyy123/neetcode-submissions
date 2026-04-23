class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        pos_and_speed = []
        for i in range(len(position)):
            pos_and_speed.append([position[i],speed[i]])
        pos_and_speed.sort(reverse = True)
        number_of_fleets = len(pos_and_speed)
        for i in range(len(pos_and_speed) - 1):
            if pos_and_speed[i][0] > pos_and_speed[i + 1][0] and pos_and_speed[i][1] >= pos_and_speed[i + 1][1]:
                continue
            number_of_steps_to_reach_target_first = (target - pos_and_speed[i][0]) / pos_and_speed[i][1]
            number_of_steps_to_reach_target_second = (target - pos_and_speed[i + 1][0]) / pos_and_speed[i + 1][1]
            if number_of_steps_to_reach_target_second <= number_of_steps_to_reach_target_first:
                number_of_fleets -= 1
                pos_and_speed[i + 1][0] = pos_and_speed[i][0]
                pos_and_speed[i + 1][1] = pos_and_speed[i][1]
        return number_of_fleets