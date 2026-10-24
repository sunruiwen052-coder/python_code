# # match...case 模式匹配:工作安排
# day = input("请输入星期几(1到7):")

# match day:
#     case "1":
#         print("周一:工作会议日")
#     case "2":
#         print("周二:学习培训日")
#     case "3":
#         print("周三:培训开发日") 
#     case "4":
#         print("周四:代码审查日")          
#     case "5":
#         print("周五:总结规划日")   
#     case "6" | "7":
#         print("周末:休息放松")  
#     case _:
#         print("输入有误!!!")       

# # 案例:简易计算器
# # 制作一个计算器,可以实现+ - * / 运算/用户输入需要运算的的两个数以及运算符之后,就可以进行计算
# num1 = float(input("请输入第一个数:"))
# num2 = float(input("请输入第二个数:"))
# oper = input("请输入运算符:")

# match oper:
#     case "+":
#         print(f"{num1}+{num2} = {num1 + num2}")
#     case "-":
#         print(f"{num1}-{num2} = {num1 - num2}")
#     case "*":
#         print(f"{num1}*{num2} = {num1 * num2}")  
#     case "/" if num2 != 0:
#         print(f"{num1}/{num2} = {num1 / num2}")
#     case _:
#         print("无法运行!!!")


# 作业:制作一个游戏角色移动控制系统,根据玩家输入的不同指令,控制游戏角色执行相应的动作(输出控制台)
# 具体规则:
# 玩家输入
# 上/w/W  下/s/S  左/a/A/  右/d/D/  跳/" "(空格)  攻击/j/J  退出/esc/ESC
# 对应动作
# 向上移动 向下移动 向左移动 向右移动  跳跃          发动攻击   退出游戏

move = input("请输入指令:")

match move:
    case "上" | "w" | "W":
        print("向上移动")
    case "下" | "s" | "S":
        print("向下移动")
    case "左" | "a" | "A":
        print("向左移动")
    case "右" | "d" | "D":
        print("向右移动")
    case "跳" | " " :
        print("跳跃")
    case "攻击" | "j" | "J":
        print("发动攻击")
    case "退出" | "esc" | "ESC":
        print("退出游戏")
    case _:
        print("操作失败")    
        