# # 列表操作
# # 定义列表
# s = [11,22,33,56,67,"a","hello",True]

# print(type(s))

# #访问列表元素
# # 获取
# print(s[0]) #正向索引,从0开始
# print(s[-8]) #反向索引,从-1开始

# print(s[7])
# print(s[-1]) 

# # 修改
# s[6] = "abc"
# print(s)

# # 如果指定的索引超出范围将会报错
# # s[10] = "qq"
# # print(s)

# # 删除
# del s[6]
# print(s)

# # 遍历(验证该列表元素有序)
# for item in s:
#     print(item)




# # 列表list-切片
# # 定义列表
# s = ["a","b","c","d","e","f","g","h","i","j"]

# # 切片操作  s[开始索引:结束索引:步长]
# print(s[0:5:1])
# print(type(s[0:5:1]))
# print(s[:5])

# print(s[0:5:2])
# print(s[0:-2:1])


# # 列表的常用方法

# # 列表定义
# s = [11,22,33,44,99,88,77,66]
# print(s)

# # append  #在列表尾部追加元素
# s.append(55)
# print(s)

# # insert  #在指定索引前，插入该元素
# s.insert(4,55)
# print(s)

# # remove  #移除列表中第一个匹配到的值
# s.remove(55)
# print(s)

# # pop  #删除列表中指定索引位置的元素（如果未指定索引，则默认删最后一个元素）
# s.pop(7)
# print(s)

# s.pop()
# print(s)

# # sort  #对列表进行排序（列表数据类型一致，才可以进行排序）
# s.sort()
# print(s)

# # reverse  #反转列表元素
# s.reverse()
# print(s)

# # 案例：将用户输入的10个数字，存储到一个列表里，并将列表中的式子进行排序，输出其中最小值，最大值和平均值

# # 定义列表
# num_list = []

# # 将用户输入的10个数字存储到列表里(已知次数的循环用for)
# for i in range(10):
#     num = int(input("请输入一个有效数字："))
#     num_list.append(num)

# print("数字列表:",num_list)

# # 排序
# num_list.sort()
# print("排序后的列表:",num_list)


# # 输出最大值，最小值和平均值
# print("最小值：",num_list[0])
# print("最大值：",num_list[-1])
# print("平均值：",sum(num_list)/len(num_list))

# print("最小值：",min(num_list))
# print("最小值：",max(num_list))


# # 合并两个列表的元素，并对合并后的列表进行去重处理
# # 定义列表
# num_list1 = [1,2,3,4,5,67,89,0]
# num_list2 = [9,0,584,332,271,71,1,25,67,8]

# # 合并列表
# for num in num_list2:
#     num_list1.append(num)

# print("合并后的列表:",num_list1)

# # 去重处理
# new_list = []
# for num in num_list1:
#     # 判断new_list里是否存在num元素,如果不存在,再添加
#     if num not in new_list: # 判断元素是否存在于列表中,如果存在,返回True,不存在,返回False
#         new_list.append(num)

# print("去重后的列表:",new_list)

# # 合并列表简化版1
# # 解包:将列表这一类容器解开成一个一个独立的元素 *
# # 组包:将多个值合并到一个容器
# num_list = [*num_list1,*num_list2]

# # 合并列表简化版2
# num_list = num_list1 + num_list2


# # 1.生成1-20的平方列表---->range(1,21)
# # 方式一:
# num_list = []
# for i in range(1,21):
#     num_list.append(i**2)
# print(num_list)

# # 方式二:列表推导式--->按规则快速生成列表--->语法格式[要插入列表的值 for i in 序列/列表]
# new_list = [i**2 for i in range(1,21)]
# print(new_list)


# # 2.从如下数字列表中提取所有偶数,并计算其平方,组成一个新的列表
# num_list = [11,22,33,44,555,66,45,77,33,109,108]
# # 列表推导式--->按规则快速生成列表--->语法格式[要插入列表的值 for i in 序列/列表 if 条件]
# new_list = [i**2 for i in num_list if i % 2 ==0]
# print(new_list)




# 练习
# 1.将如下多个列表合并为一个列表,并去除重复元素,排好序(升序)后输出到控制台
list1 = ['q','w','e','t','y','u','i','a','s','d','f','g']
list2 = ['c','d','g','h','l','t','e']
list3 = ['z','x','v','v','b','n','t']

# 合并处理
new_list = list1 + list2 + list3
# 去重处理
list = []
for i in new_list:
    if i not in list:
        list.append(i)
list.sort()
print(list)



# 2.将如下列表能被3或5整除的元素提出来,并获取这些数字对应的平方,组成一个新的列表
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
new_list = [i**2 for i in list1 if i % 3 == 0 or i % 5 == 0]
print(new_list)



# 3.将如下列表中的正数提出来,封装为一个新的列表
list = [11,2,31,4,-5,17,45,32,-11,-98,76,-30,-17]
new_list = [i for i in list if i > 0]
print(new_list)