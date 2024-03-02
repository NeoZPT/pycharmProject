# 學生score管理sys
score_sys = ["小明", 82, "小杰", 94, "阿花", 85 ]
option = True
while option:
    opt = input("請問是否要執行operation?是的話請按1，否則按2")
    if opt == "1":
        operation = input("請輸入operation指令(A)查詢(B)新增(C)刪除(D)修改：").upper()
        if operation == "A":
            name = input("請輸入要查詢的name：")
            if name not in score_sys:
                print("查無此人")
            else:
                place = score_sys.index(name)
                print(f"{name}的score是{score_sys[place+1]}")
        elif operation == "B":
            std_info = input("請輸入要新增的name/score (中間以斜線隔開)：")
            score_sys.extend(std_info.split("/"))
            print("score新增完畢")
            print(f"目前已登錄的學生人數為{int(len(score_sys)/2)}人")
        elif operation == "C":
            name = input("請輸入要刪除的name：")
            name = score_sys.index(name)
            score_sys.pop(name_place)
            score_sys.pop(name_place)
            print(score_sys)
        elif operation == "D":
            name = input("請輸入同學的name：")
            score = input("請輸入分數：")
            name_place = score_sys.index(name)
            score_sys[name_place+1] = score
            print(score_sys)

    else:
        print("謝謝您使用本sys!")
        option = False