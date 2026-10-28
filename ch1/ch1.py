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

'''
  Task:
  • Swap the values of students_morning = 15 and students_evening = 25
  without using an extra variable.
  Expected Output:
  Before Swap: Morning Batch = 15, Evening Batch = 25
  After Swap: Morning Batch = 25, Evening Batch = 15
'''
class Swapnumbers():
  def before_swap(self):
    self.num1 = 15
    self.num2 = 25
    self._swapped()
    self._swapped_second()

  def _swapped(self):
    print(f"`Before Swap: Morning Batch {self.num1}, Evening Batch {self.num2}`")

  def _swapped_second(self):
    self.num1, self.num2 = self.num2, self.num1
    print (f'`After Swap: Morning Batch {self.num1}, Evening Batch {self.num2}`')

swapnumbers = Swapnumbers()
swapnumbers.before_swap()

'''
  Task:
  • Assign values to three variables representing the number of Python, Java, and AI
  stu-dents in a single line.
  Expected Output:
  Python = 25, Java = 18, AI = 12
'''
class SingleLine:
  def single_line(self):
    self.python, self.java, self.AI = 25, 18, 12
    print(f"The values in a single line are {self.python}, {self.java}, and {self.AI}")

single = SingleLine()
single.single_line()

'''
  Task:
  • Declare different types of variables: an integer (age), a float (course rating), and a
  string (course name).
  • Use type() to check their data types.
  Expected Output:
  21 is of type <class 'int'>
  4.9 is of type <class 'float'>
  Python Programming is of type <class 'str'>
'''

class CheckType:
  def check_type(self):
    self.age = 21
    self.course_rate = 4.9
    self.course_name = "Python Programming"
    print(f"The variable types are: Age is type {type(self.age)}, course_rate is {type(self.course_rate)}, and course name is {type(self.course_name)}")

check_varible = CheckType()
check_varible.check_type()

'''
    Task:
  • Declare three separate string variables: instructor, academy name, and slogan.
  • Concatenate them to form a full sentence.
  • Print the combined string.
  Expected Output:
  The instructor at Lkhibra Academy says: "Learning Python is fun!"
'''

def concatination():
  instructor, academy_name, slogan = "Learning", "Python", "fun"
  print(f'The instructor at Lkhibra Academy says: "{instructor} {academy_name} is {slogan}"')

concatination()