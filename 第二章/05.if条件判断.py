# if语句基本格式
# 如果高考分数超过六百八,就去上北大
# score = 695
# if score > 680: #条件后要加:
#     print("恭喜你被北大录取")
#     print("也恭喜你即将踏入精彩的校园生活")

# 案例:结合前面学习的输入输出及if条件判断的知识,实现b站的登录功能(正确的账号密码为12345678,88888888)
# # 正确的账号和密码
# ok_account = "12345678"
# ok_password = "12345678"

# # 接收用户的输入的账号和密码
# account = input("请输入b站账号:")
# password = input("请输入b站密码:")

# # 判断账号和密码是否全部正确,如果都正确,则登录成功,进入B站首页
# if account == ok_account and password == ok_password:
#     print("登录成功")
#     print("进入B站首页")

# # 判定账号和密码是否有错误的,如果有任何一个错误,则登录失败,提示错误信息
# if account != ok_account or password != ok_password:
#     print("登录失败")
#     print("账号或密码错误!")
# # 繁琐,效率不高,因为不是成功就是失败,没有第三种情况,第二个不写也没问题,顶多不显示,但也登录不进去


# if语句进阶
# if...else...语句
# 案例:结合前面学习的输入输出及if条件判断的知识,实现b站的登录功能(正确的账号密码为12345678,88888888)
# 正确的账号和密码
# ok_account = "12345678"
# ok_password = "12345678"

# # 接收用户的输入的账号和密码
# account = input("请输入b站账号:")
# password = input("请输入b站密码:")

# # 判断账号和密码是否全部正确,如果都正确,则登录成功,进入B站首页
# if account == ok_account and password == ok_password:
#     print("登录成功")
#     print("进入B站首页")
# else:
#     print("登录失败")
#     print("账号或密码错误!")


# 案例:根据用户输入的年份,判断这一年是闰年还是平年
  # 非整百年份,且能被4整除的年份是闰年
  # 整百年份(如1900年,2000年)必须能被400整除才是闰年
# year = int(input("请输入年份:"))

# # 非整百年份,且能被4整;整百年份必须能被400整除
# if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")



# # 作业1:根据用户输入的数字,判断该数字是奇数还是偶数
# num = int(input("请输入数字:"))
# if num % 2 == 0:
#     print(f"{num}是偶数")
# else:
#     print(f"{num}是奇数")

# # 作业2:根据用户输入的年龄,判断该用户是否已经成年(>=18,成年;否则未成年)
# year = int(input("请输入年龄:"))
# if year >= 18:
#     print("您已成年")
# else:
#     print("您未成年")

# # 作业3:根据用户输入的数字,判断该数字是正数还是负数(不考虑0)
# num = int(input("请输入数字:"))
# if num > 0:
#     print(f"{num}是正数")
# else:
#     print(f"{num}是负数")

# # 作业4:根据用户输入的考试分数,判断该分数是否及格了(大于等于60就是及格了)
# score = int(input("请输入分数:"))
# if score >= 60:
#     print(f"{score}是及格")
# else:
#     print(f"{score}是不及格")

# # if...elif...else语句
# # 作业3考虑哦0
# num = int(input("请输入数字:"))
# if num > 0:
#     print(f"{num}是正数")
# elif num < 0:
#     print(f"{num}是负数")
# else:
#     print(f"{num}是0")

# # 案例
# # 1.根据输入用户名,密码进行登录系统
# # 用户名密码为sena/122320或者Clara/320621或者srw/12345678则输出登陆成功
# # 否则就提示用户名或密码错误
# name = input("请输入用户名:")
# password = input("请输入密码:")
# if name == "sena" and password == "122320":
#     print("登陆成功1")
# elif name == "Clara" and password == "320621":
#     print("登陆成功2")
# elif name == "srw" and password == "12345678":
#     print("登录成功3") 
# else:
#     print("用户名或密码错误")

# 案例:三角形类型判断:灯具输入的三个变得边长(正整数),判断是等边三角形,等腰三角形,普通三角形,还是不能构成三角形
#       构成三角形的条件:两边之和大于第三边
#                       三角形判定规则:
#                       三个边都相等:等边三角形
#                       两个边相等:等腰三角形
#                       三个边都不相等:普通三角形

# # 1.接收输入的三个边长
# a = int(input("请输入第一个边的边长:"))
# b = int(input("请输入第二个边的边长:"))
# c = int(input("请输入第三个边的边长:"))

# # 2.判断三角形的类型---pass #是一个空语句,起到一个与占位的作用
# if a+b>c and a+c>b and b+c>a:#可以构成三角形
#     if a==b and b==c:
#          print(f"{a}{b}{c}这三个边长构成等边三角形")
#     elif a==b or a==c or b==c:
#          print(f"{a}{b}{c}这三个边长构成等腰三角形")     
#     else:
#           print(f"{a}{b}{c}这三个边长构成普通三角形")     
# else:
#     print(f"{a}{b}{c}这三个边长不能构成三角形")


# 练习:根据输入的用电量,计算电费
# 阶梯电价规则:
#第一档:2880度以下,0.4883元每度
#第二档:2880-4800,0.5383元每度
#第三档:4800度以上,0.7883元每度

# elect = int(input("请输入用电量:"))
# if elect <= 2880:
#     print(f"电费为:{elect}*0.4883=",elect * 0.4883)
# elif 2880<elect<4880:
#     print(f"电费为:2880*0.4883+(elect-2880)*0.5383=",2880*0.4883+(elect-2880)*0.5383)
# elif elect>=4880:
#     print(f"电费为:2880*0.4883+1920*0.5383+(elect-4880)*0.7883=",2880*0.4883+1920*0.5383+(elect-4880)*0.788)         