# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

#
# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
#
#
# # 按间距中的绿色按钮以运行脚本。
# if __name__ == '__main__':
#     print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

# age = int(input("请输入你的年龄："))
# vip = int(input("请输入你的vip等级"))
#
# if age >= 18:
#     print("你已成年，购票需20元")
#     if vip > 3:
#         print(f"你是尊贵的vip{vip},可以免费游玩")
#     else:
#         print("sorry,你需要补票，20元")
# else:
#     print("你未成年，欢迎你小朋友")

# i = 0
# while i < 100:
#     i += 1
#     print(f"这是测试，这是第{i}次")

# zfc = "itheima is a brand of itcast"
# sz = 0
# for i in zfc:
#     if i == "a":
#         sz += 1
# print(f"itheima is a brand of itcast共有{sz}个a")

# num = 0
# for x in range(88):
#     if x%2 == 0:
#         num +=1
# print(f"共有{num}个偶数")
#


# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(f"{j} * {i} = {j * i}\t", end='')
#         j += 1
#     i += 1
#     print()


#
# i = 1
# for z in range(1, 10):
#     p = 1
#     if z <= i:
#         print(f"{z} * {i} = {z*i}\t", end='')
#     i += 1
#     print()
#

# for a in range(1, 10):
#     for c in range(1, 10):
#         if a >= c:
#             print(f"{a} * {c} = {a*c}\t", end='')
#     print()
#

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i} * {j} = {i * j}\t", end='')
    print()

