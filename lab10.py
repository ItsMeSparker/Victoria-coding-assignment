import doctest
from student import Student

STUDENT_FILE = "/Users/natipumvitayapradit/Downloads/student_data.csv"

def get_students(fileName: str) -> list[Student]:
    """
    This function will read the file and return the list of student information
    """
    fileHandler = open(fileName, 'r')
    result = []
    
    for line in fileHandler:
        lineList = line.strip().split(',')
        newStudt = Student(lineList[0], int(lineList[1]))
        result.append(newStudt)
    
    fileHandler.close()
    return result
    
def get_classlist(StudentList: list[Student]) -> list[str]:
    """
    This function will extract the student list to create another list
    of student id
    """
    result = []
    for student in StudentList:
        ID = student.get_sid()
        result.append(ID)
    return result

def count_above(StudentList: list[Student], Threshold: int) -> int:
    """
    This function will take a student list and a threshold number to counter
    how many student that their grade is higher than those number
    """
    result = 0
    for student in StudentList:
        if student.is_grade_above(Threshold):
            result += 1
    return result
    
def get_average_grade(StudentList: list[Student]) -> float:
    """
    This function will take a student list and will calculate the average
    grade of the entire list
    """
    Sum = 0
    for student in StudentList:
        Sum += student.get_grade() 
    Result = Sum/len(StudentList)
    return Result