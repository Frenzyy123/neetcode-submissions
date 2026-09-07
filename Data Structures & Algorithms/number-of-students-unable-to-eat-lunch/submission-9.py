class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stud_counter = len(students)
        freq = {0:0,1:0}
        for s in students:
            freq[s] += 1

        for san in sandwiches:
            if freq[san] == 0:
                break
            else:
                freq[san] -= 1
                stud_counter -= 1
        return stud_counter