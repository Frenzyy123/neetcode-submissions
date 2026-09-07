from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        freq = [0,0]
        for s in students:
            freq[s] += 1
        while students and freq[sandwiches[0]] > 0:
            if students[0] == sandwiches[0]:
                freq[students[0]] -= 1
                students.popleft()
                sandwiches.popleft()
            else:
                x = students.popleft()
                students.append(x)
        return len(students)