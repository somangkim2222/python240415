class Person:
    def __init__(self, id, name):
        self.id = id  # 객체의 고유한 ID
        self.name = name  # 객체의 이름
    
    def printInfo(self):
        print("ID:", self.id)  # ID 출력
        print("Name:", self.name)  # 이름 출력


class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)  # 부모 클래스의 생성자 호출
        self.title = title  # 매니저의 직책
    
    def printInfo(self):
        super().printInfo()  # 부모 클래스의 printInfo() 메서드 호출
        print("Title:", self.title)  # 직책 출력


class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)  # 부모 클래스의 생성자 호출
        self.skill = skill  # 직원의 기술
    
    def printInfo(self):
        super().printInfo()  # 부모 클래스의 printInfo() 메서드 호출
        print("Skill:", self.skill)  # 기술 출력


# 테스트 코드
if __name__ == "__main__":
    # Person 클래스 테스트
    print("Person 클래스 테스트:")
    person1 = Person(1, "Alice")  # ID가 1이고 이름이 Alice인 Person 객체 생성
    person1.printInfo()  # 정보 출력
    print()

    # Manager 클래스 테스트
    print("Manager 클래스 테스트:")
    manager1 = Manager(2, "Bob", "Senior Manager")  # ID가 2이고 이름이 Bob인 매니저 객체 생성
    manager1.printInfo()  # 정보 출력
    print()

    # Employee 클래스 테스트
    print("Employee 클래스 테스트:")
    employee1 = Employee(3, "Charlie", "Python Developer")  # ID가 3이고 이름이 Charlie인 직원 객체 생성
    employee1.printInfo()  # 정보 출력
    print()

    # 추가된 테스트 코드
    print("추가된 테스트 코드:")
    manager2 = Manager(4, "David", "Project Manager")  # ID가 4이고 이름이 David인 매니저 객체 생성
    manager2.printInfo()  # 정보 출력
    print()

    employee2 = Employee(5, "Eve", "Data Analyst")  # ID가 5이고 이름이 Eve인 직원 객체 생성
    employee2.printInfo()  # 정보 출력
    print()

    person2 = Person(6, "Frank")  # ID가 6이고 이름이 Frank인 Person 객체 생성
    person2.printInfo()  # 정보 출력
    print()

    manager3 = Manager(7, "Grace", "Engineering Manager")  # ID가 7이고 이름이 Grace인 매니저 객체 생성
    manager3.printInfo()  # 정보 출력
    print()

    employee3 = Employee(8, "Henry", "Software Engineer")  # ID가 8이고 이름이 Henry인 직원 객체 생성
    employee3.printInfo()  # 정보 출력
    print()

    person3 = Person(9, "Ivy")  # ID가 9이고 이름이 Ivy인 Person 객체 생성
    person3.printInfo()  # 정보 출력
    print()

    manager4 = Manager(10, "Jack", "Product Manager")  # ID가 10이고 이름이 Jack인 매니저 객체 생성
    manager4.printInfo()  # 정보 출력
