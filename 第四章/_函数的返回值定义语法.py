

# # 定义函数
# def add(a, b):
#     result = a + b
#     return result # 通过返回值，将结果返回给调用者
#
# r = add(5, 6) # 函数的返回值可以用变量接受
# print(r)
#

# def name(age):
#     """
#
#     :param age: 定义函数
#     :return: 返回空白None
#     """
#     if age > 18:
#         return "yes"
#     else:
#         return None
#
# result = name(16)
# if not result:
#     print("未成年")

# 定义函数fun_a
# def fun_a():
#     print("---1---")
#
# # 定义函数fun_b
# def fun_b():
#     print("---2---")
#     # 函数嵌套fun_a
#     fun_a()
#     print("---3---")
#
# # 调用函数
# fun_b()

# num = 200 # 全局变量
#
# def num_a():
#     print(f"num_a: {num}")
#
# def num_b():
#     print(f"num_b: {num}")
#
# num_a()
# num_b()
# print(num)


# num = 200 # 全局变量

# def num_a():
#     print(f"num_a: {num}")
#
# def num_b():
#     num = 500 # 局部变量
#     print(f"num_b: {num}")
#
# num_a()
# num_b()
# print(num)

# num = 200 # 全局变量
#
# def num_a():
#     print(f"num_a: {num}")
#
# def num_b():
#     global num # global 关键字声明num是全局变量
#     num = 500
#     print(f"num_b: {num}")
#
# num_a()
# num_b()
# print(num)