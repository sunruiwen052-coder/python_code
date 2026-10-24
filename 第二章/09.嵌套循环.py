# 打印一个长度为m,款的为n的长方形
# print("*") 或者 print("*",end = "\n"): 自带换行效果,每一次执行都会处处新的一行中
# print("*",end = ""):end表示每一次输出以什么结束,这样写就不会自动换行

# 1.接受键盘的录入,m,n
# m = int(input("请输入长方形的长:"))
# n = int(input("请输入长方形的宽:"))


# # 2.制作长方形
# for a in range(m):
#     print("*",end = "  ")
#     for b in range(n):
#             print()
    

# for a in range(m): # 控制行,外层循环先处理一个元素,等内部循环将这个元素处理完再处理第二个                   
#     for b in range(n):  # 控制列,内层循环处理次数为数据集n里的个数              
#         print("*", end=" ")#属于内层循环的循环体代码           
#     print() #属于外层循环的循环体代码,等内层循环结束运行                          

# for b in range(n): # 控制行
#     for i in range(m): # 控制列
#         print("*",end="  ")
#     print()

# 案例：打印99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j} x {i} = {j * i}",end="\t")
#     print()


# 练习
# 1.根据输入的直角边的的边长，打印等腰直角三角形
# length =int(input("请输入直角边的边长:"))
# for i in range(0,length):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()    

# 2.根据输入的数字，打印对应的数字金字塔
# number =int(input("请输入数字:"))
# for i in range(0,number):
#     for j in range(0,i+1):
#         print(j+1,end=" ")
#     print()

# 3.打印国际象棋棋盘
# for i in range(0,8):
#     for j in range(0,8):
#         if (i + j) % 2 == 0:
#             print("■", end=" ")
#         else:
#             print("□", end=" ")
#     print()

# 打印圣诞树
# n = int(input("请输入高度:"))

# for i in range(n):

#     # 打印空格
#     for j in range(n-1-i):
#         print(" ", end="")

#     # 打印星星
#     for j in range(2*i+1):
#         print("*", end="")

#     # 换行
#     print()


# 关键词:break:只能够出现在循环里,表示结束,跳出循环的含义(break跳出循环时,while后面的else中的代码不会执行)
# continue:只能够出现在循环里,表示中断本次循环(后面的循环不继续了),直接进入下一次新的循环



# 案例:登录操作
# while True: #无限循环的意思,制造循环的条件
#     # 1. 接收输入的用户名和密码
#     username = input("请输入账号:")
#     password = input("请输入密码: ")
#     # 2. 校验:输入的用户名和密码不能为空
#     if username == "" or password == "":
#         print("账户和密码不能为空,请重新输入!")
#         continue
#     # 3. 判断用户名和密码的正确性,执行登录操作
#     if username == "Clara" and password == "122320":
#         print("登陆成功!")
#         break
#     elif username == "sena" and password == "4610520":
#         print("登陆成功!")
#         break      
#     else:
#         print("登录失败,请重新输入!")


# 练习：五次登录机会

# i = 0
# for i in range(5):
#     username = input("请输入账号:")
#     password = int(input("请输入密码:"))
#     if username == "clara" and password == 122320:
#         print("登陆成功！")
#         break 
        
#     elif username == "sena" and password == 4610520:
#         print("登陆成功！")
#         break
        
#     else:
#         print("登录失败!请重新尝试")
# else:
#     print("五次已用完,锁定")       


# 案例:
# 1.系统随机生成一个随机值
# 2.用户根据提示猜数字,并将所猜的数字输入系统
# 3.如果猜错,系统给出猜大或猜小的提示,然后继续输入猜的数字
# 4.如果猜对,系统自动退出,游戏结束

# import random #导入random
# random_num = random.randint(1,100)
# while True:
#     num = int(input("请输入数字:"))
#     if num > random_num:
#         print("输入的数字大了")
#     elif num < random_num:
#         print("输入的数字小了")
#     elif num == random_num:
#         print("恭喜您,猜对了")
#         break
# print("随机生成的数字是:",random_num)    


# 练习
# 1.将1-1000之间(包含1000)所有的5的倍数的数字加起来
# total = 0
# i=1
# while i<=1000:
#     if i % 5 == 0:
#         total += i
#     i += 1
# else:
#     print("total:",total)       

    
# 2.统计字符串"akiwksjakdiklowiqaamvalasdfghjkiokmaoijnca"有多少个a和k
# msg = "akiwksjakdiklowiqaamvalasdfghjkiokmaoijnca"
# num = 0
# for i in msg:
#     if i == "a" or i == "k":
#         num += 1
# else:
#     print(f"一共有{num}个a和k") 


