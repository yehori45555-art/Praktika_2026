    1 def create_raiting(students: list) -> list:
    2     n = len(students)
    3 
    4     for i in range(n):
    5         max_index = 1
    6 
    7         for j in range(i + 1, n):
    8             if students[j][1] > students[max_index][1]:
    9                 max_index = j
   10 
   11         students[i], students[max_index] = students[max_index], students[i      ]
   12     return students
   13 
   14 
   15 students = [
   16     ("Іван", 85),
   17     ("Дамір", 100),
   18     ("Олександр", 78),
   19     ("Артем", 50),
   20     ("Софія", 88)
   21 ]
