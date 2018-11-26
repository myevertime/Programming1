def displayWelcome():
    print("*" * 45)
    print("* 단위 변환 프로그램에 오신 것을 환영합니다 *")
    print("*" * 45)
    
def displayBye():
    print("*"*42)
    print("*",format("안녕히 가세요","^32"),"*")
    print("*"*42)
    
def inputMenu():
    menu = int(input("<<< Select Menu>>> \n(1) Kg => Pound, (2) Km => Mile (3) 종료: "))
    if menu not in (1,2,3):
        print("올바른 메뉴를 선택하세요")
        menu = int(input("(1) Kg => Pound, (2) Km => Mile (3) 종료: "))
    return menu

def inputValue():
    value = float(input("변환할 값을 입력하세요: "))
    if value < 0 :
        print("음수는 입력할 수 없습니다.")
        value = float(input("변환할 값을 입력하세요: "))
    return value

def displayPound(kg):
    pound = kg * 2.204623
    print(value,"Kg은",format(pound,".1f"),"Pound 입니다.")
    
def displayMile(km):
    mile = km * 0.621
    print(value,"Km는",format(mile,".1f"),"Mile 입니다")

displayWelcome()
Terminated = False
while not Terminated :
    menu = inputMenu()
    if menu == 1 :
        value = inputValue()
        displayPound(value)
    elif menu == 2:
        value = inputValue()
        displayMile(value)
    elif menu == 3:
        Terminated = True
displayBye()
