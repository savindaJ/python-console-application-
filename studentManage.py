# print("[01] studet add"+"\t\t\t"+"[02] student update"+"\n"+"[04] add marks with student"+"\t"+"[04] add marks\n\n")
import os

student_arry = []
student_id = []
marks_array = []


def setHeader(header):
    print("-----------------------------------------------------------------")
    print("|\t\t\t     " + header + "\t\t\t\t|")
    print("-----------------------------------------------------------------\n\n")


def validate(st_id) -> int:
    try:
        student_id.index(st_id)
        return 1
    except:
        return 0


def search_and_getID(name) -> int:
    # print(student_arry.index(name))
    x = student_arry.index(name)
    print(x)
    return x


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# now, to clear the screen


def add_student():
    cls()

    setHeader("add student\b\b\b")

    while True:
        st_id = input("student id ->")
        print("\n")
        x = validate(st_id)

        if x == 0:
            name = input("enter student name ->")
            print("\n")
            student_arry.append(name)
            student_id.append(st_id)
            print(student_arry, student_id)
            go = input("do you want go to main ->\n")
            if go == "yes":
                navigate()
        else:
            print("alrady exsits id !")
            go = input("do you want go to main ->")
            if go == "yes":
                navigate()
                break
            else:
                continue





def search():
    cls()

    print("\t\t\t\t\t=======search Student======\n\n\n")
    y = len(student_arry)
    name = input("enter name hear ->")
    for i in student_arry:
        if i == name:
            print(name + " in arry name !")
            break
        else:
            print("not hear !")

    go = input("do you want go to main ->")
    if go == "yes":
        navigate()
    else:
        print("buyyy !")


def studentUpdate():
    cls()

    print("\t\t\t\t\t=======update Student======\n\n\n")
    name = input("enter student name ->")
    y = search_and_getID(name)
    print("index ->")
    print(y)
    new_name = input("enter new name ->")
    student_arry[y] = new_name
    go = input("do you want go to main (yes or no)-> ")
    if go == "yes":
        navigate()
    else:
        print("buyyy !")


def add_student_withMarks():
    cls()

    print("\t\t\t\t\t=======add Student with marks======\n\n\n")
    name = input("enter name :")
    st_id = input("enter id :")
    prf = input("enter prf_marks :")
    dbms = input("enter dbms_marks :")

    go = input("do you want go to main (yes or no)->  ")
    if go == "yes":
        navigate()
    else:
        print("buyyy !")


def navigate():
    cls()
    setHeader("home")
    print(
        "[01] studet add" + "\t\t\t" + "[02] student update" + "\n" + "[04] add marks with student" + "\t" + "[04] "
                                                                                                             "add "
                                                                                                             "1marks"
                                                                                                             "\n\n")
    option = input("enter your option :")
    if option == "1":
        add_student()
    elif option == "2":
        studentUpdate()
    elif option == "3":
        add_student_withMarks()
    elif option == "4":
        search()


navigate()
