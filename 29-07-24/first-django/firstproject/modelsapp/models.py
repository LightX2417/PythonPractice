from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

# Create an Employee model in Django having appropriate fields such as Emp_ID, Emp_Name, Age, Dept_ID, Project_ID, Designation, Qualifications, Date_of_joining (Use DateField), etc. Also create a Department and Project model having fields such as Dept_ID, Dept_Name, etc., and Project_ID, Proj_Name, etc. respectively. Establish the correct relationships in the above models using relationship fields in Django. Insert the data of at least 10 employees and demonstrate the following:
# a.	CRUD operations on the data
# b.	Model String representation
# c.	Filtering and Ordering Data
# d.	Chaining Lookups
# e.	Slicing Data
# f.	Image and File Upload
# g.	Validations.


class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.dept_name


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    proj_name = models.CharField(max_length=100)

    def __str__(self):
        return self.proj_name


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    qualifications = models.TextField()
    date_of_joining = models.DateField()
    profile_picture = models.ImageField(
        upload_to="profile_pics/", blank=True, null=True
    )
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)

    def __str__(self):
        return f"{self.emp_name} ({self.designation})"

    def clean(self):
        if self.age < 18:
            raise ValidationError("Age must be 18 or above.")
        if self.qualifications not in [
            "MBA",
            "BSc Computer Science",
            "MSc Data Science",
        ]:
            raise ValidationError("Invalid qualifications.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


# Django ORM operations


def create_sample_data():
    # Create departments
    dept1 = Department.objects.create(dept_name="HR")
    dept2 = Department.objects.create(dept_name="Engineering")

    # Create projects
    proj1 = Project.objects.create(proj_name="Project A")
    proj2 = Project.objects.create(proj_name="Project B")

    # Create employees
    Employee.objects.create(
        emp_name="John Doe",
        age=30,
        dept=dept1,
        project=proj1,
        designation="Manager",
        qualifications="MBA",
        date_of_joining=date(2020, 5, 1),
    )

    Employee.objects.create(
        emp_name="Jane Smith",
        age=25,
        dept=dept2,
        project=proj2,
        designation="Developer",
        qualifications="BSc Computer Science",
        date_of_joining=date(2021, 6, 15),
    )


def demonstrate_operations():
    # CRUD operations
    # Create
    emp = Employee.objects.create(
        emp_name="Alice Brown",
        age=28,
        dept=Department.objects.first(),
        project=Project.objects.first(),
        designation="Analyst",
        qualifications="MSc Data Science",
        date_of_joining=date(2022, 3, 10),
    )


    # Read
    employees = Employee.objects.all()
    specific_employee = Employee.objects.get(emp_id=1)
    print(f"All employees:\n{employees}")
    print(f"Employee id 1:{specific_employee}")

    # Update
    emp.age = 31
    emp.save()

    # Delete
    emp.delete()

    # Filtering and Ordering
    older_employees = Employee.objects.filter(age__gt=30)
    ordered_employees = Employee.objects.order_by("date_of_joining")
    print(f"People older than 30 \n{older_employees}")
    print(f"Order of joining \n{ordered_employees}")

    # Chaining Lookups
    filtered_employees = Employee.objects.filter(
        dept__dept_name="Engineering", date_of_joining__year__gt=2021
    )
    print(f"Engineering Department:\n{filtered_employees}")

    # Slicing Data
    first_five_employees = Employee.objects.all()[:5]
    print(f"First Five Employees:\n{first_five_employees}")

    print("Data operations completed")
