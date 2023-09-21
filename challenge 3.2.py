class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa
def sort_students(student_list):
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students
students = [
Student ("sujitha","22UCS29",9.3),
Student ("janci","22UCS07",9.4),
Student ("sindhuja","22UCS27",9.2),
Student ("priya","22UCS21",9.1) 
]
sorted_students = sort_students(students)
for student in sorted_students:
  print("name:{},roll Number:{},CGPA:{}".format(student.name,
student.roll_number,
             student.cgpa))