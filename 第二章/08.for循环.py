# for循环
# 遍历输入的字符串
# msg = "Hello-Claude"
# for i in msg: #i 表示遍历出来的元素 ; msg 表示需要遍历的数据
#     print(i)
# else:
#     print("结束")

# msg = input("请输入要遍历的字符串:")
# for o in msg: #o 表示遍历出来的元素(是变量) ; msg 表示需要遍历的数据
#     print(f"元素:{o}")
# else:
#     print("遍历结束!")

# 案例
# 1.计算1-100之间所有奇数之和
# 思考:如何获得1-100之间的数据集(range语句)
# total = 0
# for i in range(1,101,2): #简化版本
#     total += i
# else:
#     print(f"和为:{total}")       

# # 2.计算100-500之间所有3的倍数的数字之和
# total = 0
# for i in range(100,501):
#     if i % 3 ==0:
#         total += i
# else:
#     print(f"和为:{total}")


# # 答案
# total = 0
# for i in range(1,101):
#     if i % 2 == 1:
#         total += i
# print("1-100之间的奇数累加之和: ", total)  