# # type(..) 获取指定的字面量或变量的类型
# print("Hello")
# print(type("Hello"))

# print(10)
# print(type(10))

# print(3.14)
# print(type(3.14))

# print(type(True))
# print(type(False))
# print(type(None))

# num = 5.0
# print(num)
# print(type(num)) #变量本身是没有类型的，变量所存储的数据是有类型的


# # isinstance(数据，指定类型)--->bool值--->判定数据是否是指定的类型，如果是：True,否则：False
# num = -100
# print(isinstance(num, int)) #True
# print(isinstance(num, float)) #False
# print(isinstance(num, bool)) #False
# print(isinstance(num, str)) #False
# print(isinstance(num, type(None))) #False

# print(isinstance(False,int)) #True
# print(isinstance(0,bool)) #False
# # bool属于int，True和False是整形，属于整数 


# # 字符串
# # 定义字符串的三种方式
# s1 = "Hello" # 双引号定义
# s2 = 'Python' # 单引号定义
# s3 = """ 
# Hello:
#     学习Python中
#     加油加油 ~
# """ #三引号定义 (多行字符串)

# print(s1)
# print(s2)
# print(s3)

# print(type(s1))
# print(type(s2))
# print(type(s3))

# #定义字符串 ---> It's very  good
# # 转义字符\' \" \n \t
# msg = 'It\'s very  good'
# print(msg)

# msg2= "It's very  good"
# print(msg)

# msg3 = "Hello 的意思是\"你好\""
# print(msg3)

# msg4 = 'Hello 的意思是"你好"'
# print(msg4)

# print("\t不仅要学习内容还要输出内容!\n\t加油加油~") # \n 换行 \t  按了tab缩进

# # 字符串拼接
# s1 = "人生苦短" "我用Python" ", OK" # +省略了,这样不如直接弄成一整个字符串
# print(s1)

# msg1 = "人生苦短" 
# msg2 = "我用Python"
# print("龟叔说: " + msg1 + "," + msg2)

# # 案例
# s1 = "今年20岁"
# s2 = "正在自学Python"
# s3 = "希望这项技能在未来能帮到我"
# print("大家好,我叫孙睿雯" + s1 + "," + s2+ "," + s3)

# # 答案--->str(int型数字)--->将int类型的数字转为字符串
# name = "孙睿雯"
# age = 20 #或者直接写"20"
# hobby = "Python"
# print("大家好,我是" + name + "," + "今年" +str(age) + "," + "我的兴趣爱好是" + hobby)



# # 字符串格式化--->  方式一: %s 占位符
# name = "孙睿雯"
# age = 20 
# hobby = "Python"
# print("大家好,我是 %s, 今年 %s 岁,我的兴趣爱好是 %s" %(name, age, hobby))

# 方式二:f"内容{变量名/表达式}内容"  推荐!!!
name = "孙睿雯"
age = 20 
hobby = "Python"
print(f"大家好,我是{name},今年{age}岁,我的兴趣爱好是{hobby}")