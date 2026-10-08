
"""Example of a has-a relationship in Python.

This program demonstrates composition. A Department object has a Teacher
object inside it, and the Teacher's method is called through the department.
"""


class Teacher:
    """Represent a teacher with a name."""

    def __init__(self, name):
        """Initialize the teacher with a name."""
        self.name = name

    def teach(self):
        """Print that the teacher is teaching."""
        print(f"{self.name} is teaching")


class Dept:
    """Represent a department that has a teacher."""

    def __init__(self, teacher):
        """Store the Teacher object in the department."""
        self.teacher = teacher


# Create a Teacher object.
teacher1 = Teacher("Ram")

# Create a Department object and give it the Teacher object.
dept = Dept(teacher1)

# Access the Teacher object through the Department and call its method.
dept.teacher.teach()
