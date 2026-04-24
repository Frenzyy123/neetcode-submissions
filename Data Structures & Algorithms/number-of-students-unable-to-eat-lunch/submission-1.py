class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        frequencies_students = {0 : 0,1:0}
        sol = len(students)
        for i in students:
            frequencies_students[i] += 1
        for s in sandwiches:
            if frequencies_students[s] > 0:
                sol -= 1
                frequencies_students[s] -= 1
            else:
                return sol
        return sol
        