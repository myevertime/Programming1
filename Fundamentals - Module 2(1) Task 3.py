#Fundamentals - Module 2(1) Task3 / Paint Stock


def color_func(color_find, paint_colors = ["red", "yellow", "green", "blue", "black"]):
    for color in paint_colors :
        if color_find.lower() == color.lower() :
            return "found"
        else :
            pass
    return "not found"
        
color_request = input("enter a color: ")

print(color_func(color_request))

# else : pass로 쓰는 이유 : color이 하나 하나 값을 받는 거라
# pass하지 않고 "not found"로 return값으로 함수를 끝내게 된다면
# 뒷 리스트 속성들은 확인하지 않기 때문이다.


# Task 4 / Foot Bones Quiz

def foot_bones_quiz(bone_search, foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform","intermediate cuneiform", "medial cuneiform"]) :
    total = ""
    for foot_bone in foot_bones :
        if bone_search.lower() == foot_bone.lower() :
            total += bone_search
            print(total)
            foot_bones.remove(bone_search)
            return "correct"
        else :
            pass

    return "incorrect"

search = input("Enter a bone to search: ")
print(foot_bones_quiz(search))

search2 = input("Enter a bone to search: ")
print(foot_bones_quiz(search2))
