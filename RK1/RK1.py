from operator import itemgetter
from tokenize import group

class Group:
    def __init__(self, id, name, rating):   # Constructor
        self.id = id
        self.name = name
        self.rating = rating # 0 - 100

class Course:
    def __init__(self, name, id):   # Constructor
        self.name = name
        self.id = id

# more to more
class GroupCourse:
    def __init__(self, group_id, course_id):   # Constructor
        self.group_id = group_id
        self.course_id = course_id

group = [
    Group(1, "RT5-31B", 56.67),
    Group(2, "IU5-31B", 31.42),
    Group(3, "RK6-41B", 78.89),
    Group(4, "E9-21B", 99.99),
    Group(5, "MT2-11B", 3.14),
]

course = [
    Course("Math Course", 1),
    Course("Physics Course", 2),
    Course("Data Models", 3),
    Course("Python", 4),
    Course("Internet Technologies Course", 5),
]

group_course = [
    GroupCourse(1, 1),
    GroupCourse(1, 3),
    GroupCourse(2, 2),
    GroupCourse(2, 3),
    GroupCourse(3, 1),
    GroupCourse(3, 2),
    GroupCourse(4, 1),
    GroupCourse(4, 3),
    GroupCourse(5, 2),
    GroupCourse(5, 3),
]

# «Course» и «Group» связаны соотношением один-ко-многим.
# Выведите список всех Course, у которых в названии присутствует слово «Course»,
# и список Group.

def Task1 ():
    result = []
    for i in course:
        mid_result = []
        if "Course" in i.name:
            mid_result.append(i.name)
            for j in group_course:
                if j.group_id == i.id:
                    for k in group:
                        if k.id == j.course_id:
                            mid_result.append(k.name)
            result.append(mid_result)
    return result

# «Course» и «Group» связаны соотношением один-ко-многим.
# Выведите список Course со средним рейтингом (rating) Group
# в каждом Course, отсортированный по среднему значению.

def Task2 ():
    result = []
    for i in course:
        mid_result = []
        mid_result.append(i.name)
        sum = 0
        count = 0
        for j in group_course:
            if j.group_id == i.id:
                for k in group:
                    if k.id == j.course_id:
                        sum += k.rating
                        count += 1
        mid_result.append(sum / count)
        result.append(mid_result)
    result = sorted(result, key=itemgetter(1), reverse=False)
    return result

# «Course» и «Group» связаны соотношением многие-ко-многим.
# Выведите список всех Course,
# у которых название начинается с буквы «P»,
# и список Group.

def Task3 ():
    result = []
    for i in course:
        mid_result = []
        if "P" == i.name[0]:
            mid_result.append(i.name)
            for j in group_course:
                if j.group_id == i.id:
                    for k in group:
                        if k.id == j.course_id:
                            mid_result.append(k.name)
            result.append(mid_result)
    return result


def main() :
    print("\nTask 1:", Task1())

    print("\nTask 2:", Task2())

    print("\nTask 3:", Task3())

if __name__ == "__main__":
    main()