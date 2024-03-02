import random
import string

option = True
print("新增一行程式碼")

while option:
    text = input("是否要產生密碼?要請輸入1，否則輸入2")
    if text == "1":
        letters = string.ascii_letters
        nums = string.digits
        compound = list(letters + nums)
        random.shuffle(compound)       #shuffle=洗牌的意思
        length = int(input("請輸入你要幾位數:"))
        pwd = "".join(compound[:length])
        print(f"你的密碼是:{pwd}")
    else:
        print("程式結束")
        option = False



