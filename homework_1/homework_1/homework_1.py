class student():
    def __init__(self, name, age, height, average_score):
        self.name = name
        self.age = age
        self.height = height
        self.average_score = average_score

    def search_student(self, name):
        if name == self.name:
            return self
        else:
            return 0

def add_student(students):
    print("학생의 이름을 입력하세요 : ")
    name = input()
    print("학생의 나이를 입력하세요 : ")
    age = int(input())
    print("학생의 키를 입력하세요 : ")
    height = int(input())
    print("학생의 평균 점수를 입력하세요 :")
    average_score = int(input())
    students.append(student(name, age, height, average_score))
    print("학생을 정상적으로 등록했습니다.")
    print("-> 다시 메인 메뉴로")

def del_student(students):
    print("삭제할 학생의 이름을 입력해주세요 : ")
    name = input()
    for x in students:
        search = x.search_student(name)
        if search:
            print("이름 : {0}, 나이 : {1}, 키 : {2}, 평균 점수 : {3}".format(search.name, search.age, search.height, search.average_score))
            print("해당 학생이 맞습니까?(y/n) : ")
            answer = input()
            if answer == 'y':
                print("김철수 학생이 삭제되었습니다.")
                students.remove(search)
                break
            elif answer == 'n':
                break
            else:
                print("오류")
        else:
            print("해당 학생을 찾을 수 없습니다.")
    print("-> 다시 메인 메뉴로")

def print_all_students(students):
    print("----등록되어 있는 학생 목록----")
    for x in students:
        print("이름 : {0}, 나이 : {1}, 키 : {2}, 평균 점수 : {3}".format(x.name, x.age, x.height, x.average_score))
    print("-> 다시 메인 메뉴로")


def find_student(students):
    print("검색할 이름을 입력해주세요 :")
    name = input()
    print("---- {0}으로 검색한 결과입니다----".format(name))
    for x in students:
        search = x.search_student(name)
        if search !=0:
            print("이름 : {0}, 나이 : {1}, 키 : {2}, 평균 점수 : {3}".format(search.name, search.age, search.height, search.average_score))
    print("-> 다시 메인 메뉴로")


def print_option():
    print("----[학생 관리 프로그램]----","1. 학생 추가","2. 학생 삭제","3. 학생 전체 조회","4. 학생 검색",
"5. 종료", end = '\n')
    print("메뉴를 선택하세요 : ")

students = []

n = 0

while(n!=5):
    print_option()
    n = int(input())
    if n == 1:
        add_student(students)
    if n == 2:
        del_student(students)
    if n == 3:
        print_all_students(students)
    if n == 4:
        find_student(students)

print("프로그램을 종료합니다.","-> 프로그램 종료", end = '\n')