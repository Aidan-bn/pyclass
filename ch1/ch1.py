# Task:
# • Declare variables for an instructor’s name, the number of students in a Python class,
# and the course name.
# • Print them using a formatted string.
# Expected Output Example:
# The instructor is Alex, there are 30 students in the Python class!

class Instructor:
  def instructor_information (self, name, number_of_students):
    self.name = name 
    self.number_of_students = number_of_students
    self._printed_sentense()

  def _printed_sentense(self):
    print(f"`he instructor is {self.name}, there are {self.number_of_students} students in the Python class!`")

# create an object
instructor = Instructor()

# Instatiate the class
instructor.instructor_information("Alex", 40)

