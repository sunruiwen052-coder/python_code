# # While循环
# # 打印十遍"怪兽大学"
# i = 0
# while i < 10:
#     print("怪兽大学")
#     i += 1 #(没有这个会陷入死循环)
# else:
#     print("循环正常结束")    

# # 案例:计算1-100之间所有偶数的累加之和
# # 思考1:如何获取到1-100之间的偶数  num % 2 == 0
# # 思考2:累加运算使用什么运算符 +=
# total = 0
# i = 1
# while i <= 100:
#     if i % 2 == 0: #偶数
#         total += i
#     i += 1
# else:
#     print(f"和为:{total}")       

# total = 0
# i = 1
# while i <= 100:
#     if i % 2 == 1:
#         total += i
#     i += 1    
# else:
#     print(f"和为:{total}")       



