class Person:
    def __init__(self, id, name):
        # Person 클래스의 생성자입니다. id와 name을 입력받아 객체를 초기화합니다.
        self.id = id
        self.name = name

    def printInfo(self):
        # 객체의 정보를 출력하는 메서드입니다.
        print("ID:", self.id)
        print("Name:", self.name)


class Manager(Person):
    def __init__(self, id, name, title):
        # Manager 클래스의 생성자입니다. id, name, title을 입력받아 객체를 초기화합니다.
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        # Manager 객체의 정보를 출력하는 메서드입니다.
        super().printInfo()  # Person 클래스의 printInfo() 메서드를 호출하여 기본 정보를 출력합니다.
        print("Title:", self.title)  # Manager 객체의 title 정보를 출력합니다.


class Employee(Person):
    def __init__(self, id, name, skill):
        # Employee 클래스의 생성자입니다. id, name, skill을 입력받아 객체를 초기화합니다.
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        # Employee 객체의 정보를 출력하는 메서드입니다.
        super().printInfo()  # Person 클래스의 printInfo() 메서드를 호출하여 기본 정보를 출력합니다.
        print("Skill:", self.skill)  # Employee 객체의 skill 정보를 출력합니다.


# 테스트 코드
def test_classes():
    # Person 클래스 테스트
    person1 = Person(1, "John Doe")
    print("Person Info:")
    person1.printInfo()
    print()

    # Manager 클래스 테스트
    manager1 = Manager(2, "Jane Smith", "Senior Manager")
    print("Manager Info:")
    manager1.printInfo()
    print()

    # Employee 클래스 테스트
    employee1 = Employee(3, "Alice Johnson", "Python Developer")
    print("Employee Info:")
    employee1.printInfo()
    print()

    # 추가 테스트
    # Person 클래스를 상속받는데, Manager와 Employee 클래스가 Person 클래스의 메서드를 사용할 수 있는지 확인해야 해
    # Manager 클래스가 Person 클래스의 printInfo() 메서드를 사용할 수 있는지 테스트
    print("Manager using Person method:")
    manager1.printInfo()
    print()

    # Employee 클래스가 Person 클래스의 printInfo() 메서드를 사용할 수 있는지 테스트
    print("Employee using Person method:")
    employee1.printInfo()
    print()

    # Manager 클래스의 printInfo() 메서드에 title 변수 출력이 추가되었는지 테스트
    print("Manager using Manager method:")
    manager1.printInfo()
    print()

    # Employee 클래스의 printInfo() 메서드에 skill 변수 출력이 추가되었는지 테스트
    print("Employee using Employee method:")
    employee1.printInfo()
    print()

    # 다른 제목과 기술을 가진 다른 인스턴스를 사용하여 클래스를 테스트할 수도 있어
    manager2 = Manager(4, "Bob Brown", "Project Manager")
    print("Another Manager Info:")
    manager2.printInfo()
    print()

    employee2 = Employee(5, "Eva White", "Java Developer")
    print("Another Employee Info:")
    employee2.printInfo()
    print()


# 테스트 실행
test_classes()
