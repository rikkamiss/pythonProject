# import random
#
# l = random.Random(36, 36)
#
#
# print(l.random())

import random # 导入 random 模块
x = random.uniform(36.5, 41) # 生成一个 [36.5, 41] 之间的随机小数，并赋值给 x
def add(y):
    if y <= 37.5:
        print("你的体温是%.1f,可以入内" % y)
    else:
        print(f"你的体温是%.1f，需要隔离" % x)  # 打印出 x 的值
add(x)


# import random # 导入 random 模块
# x = random.random() # 生成一个 [0,1) 之间的随机小数，并赋值给 x
# print(x) # 打印出 x 的值


# import random
# r = random.Random(0) # 创建一个随机数生成器的实例，使用 0,1 作为种子值
# print(r.random()) # 生成第一个随机小数
# print(r.random()) # 生成第二个随机小数
# print(r.random()) # 生成第三个随机小数


#
#
# for i in range(1, 10):
#     num = random.randint(1, 20)
#
#
#     # 定义函数add
#     def add(x, y):  # x是形式参数
#         reuse = x + y
#         print(f"这是随机数{x} + {y} = {reuse}")
#
#
#     add(num, i)  # num是实际参数









