from num_easy import easy
from num_diffcult import diffcult
print("-----欢迎来到导航系统")
print("1-----猜数字（简单）")
print("2-----猜数字（困难）")
num = int(input("请选择"))
if num == 1:
    easy()
if num == 2:
    diffcult()