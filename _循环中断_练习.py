import random

# 定义工资
money = 10000


#for循环对员工发放工资
for i in range(1, 21):
    num = random.randint(1, 10)
    if num < 5:
        print(f"员工{i},绩效分{num}，低于5，不发工资，下一位")
        # continue跳过发放
        continue
    # 判断是否有余额
    if money > 0:
        money -= 1000
        print(f"向员工{i}发工资1000元，账户余额还剩下{money}元")
    else:
        print("余额不足，下个月领取吧")
        # breck结束发放
        break










