from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        suma_students = sum(students)
        students = deque(students)
        sandwiches = deque(sandwiches)
        while True:
            if students[0] == sandwiches[0]:
                suma_students -= students[0]
                students.popleft()
                sandwiches.popleft()
            else:
                student = students.popleft()
                students.append(student)
            if not students:
                return 0
            if suma_students == len(students) and sandwiches[0] == 0:
                return len(students)
            elif suma_students == 0 and sandwiches[0] == 1:
                return len(students)
        