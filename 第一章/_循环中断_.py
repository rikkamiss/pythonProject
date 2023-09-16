
## continue关键字 (中断所在循环的当次执行，直接进入下次)
## continue 临时中断

# 演示循环中断语句 continue
# for i in range(1, 6):
#     print("语句1")
#     continue # 跳过本次循环
#     print("语句2")
#

# 演示continue的嵌套应用
# for i in range(1, 6):
#     print("语句1")
#     for j in range(1, 6):
#         print("语句2")
#         continue
#         print("语句3")
#
#     print("语句4")
#

###############################
## break关键字 (直接结束所在循环)
## break 永久中断

# 演示循环中断语句break
# for i in range(1, 101):
#     print("语句1")
#     break # 直接中断循环
#     print("语句2")
#
# print("语句3")
#

# 演示break的嵌套应用
# for i in range(1, 10):
#     print("语句1") # 输出’语句1‘
#     for j in range(1, 100):
#         print("语句2") # 输出’语句2‘
#         break # 中断for循环j 直接输出下个for循环l
#         print("语句3")
#         for l in range(1, 500):
#             print("语句4") # 输出’语句4‘
#             break #中断for循环l 直接输出’语句6‘
#             print("语句5")
#     print("语句6")









































































