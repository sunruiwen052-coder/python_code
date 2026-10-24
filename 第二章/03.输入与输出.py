# 获取键盘上输入的数据 -- input(...)
name = input("请输入您的姓名: ")
age = input("请输入您的年龄: ")
print(f"您的姓名是:{name},年龄为:{age}")


# 案例:银行卡ATM取款
password = input("请输入您的银行卡密码:")
amount = input("请输入您的取款金额:")
money = 10000
print(f"余额:{money} - {amount} ")
# 错误原因:所有键盘输入的数据都是字符串类型,这里amount"取出的金额"就是字符串,money是int,不能相减,所以要转换

# 答案
# 总金额
total = 10000

# 1.输入密码
password = input("请输入您的银行卡密码:")
print(f"密码正确,{password}")

# 2.输入取款金额
num = input("请输入您的取款金额:")


# 3.计算余额并输出 --->amount转为 int 类型 ---> int(..)
print(f"取款后银行卡余额为: {total - int(num)}")


# 练习
num1 = input("输入第一个数字:")
num2 = input("输入第二个数字:")
print(f"相加的和:{int(num1) + int(num2)}")