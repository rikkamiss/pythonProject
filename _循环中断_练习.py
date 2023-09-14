import random

money = 10000

for i in range(1, 21):
    num = random.randint(1, 10)
    if num < 5:
        print(f"员工{i},绩效分{num}，低于5，不发工资，下一位")
        continue
    if money > 0:
        money -= 1000
        print(f"向员工{i}发工资1000元，账户余额还剩下{money}元")
    else:
        print("余额不足，下个月领取吧")
        break










