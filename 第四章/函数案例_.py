

money = 50000000
name = None

name = input("请输入你的姓名：")
def query(show_money):
    if show_money:
        print("--------查询余额----------")
    print(f"{name},您好，你的账户余额剩余: {money}元")

def saving(num):
    global money
    money += num
    print("--------存款----------")
    print(f"您好，你存款{num}元成功。")
    query(False)

def get_money(num):
    print("--------取款----------")
    global money
    if num > money:
        print(f"对不起，余额不足，你的账户余额只剩下{money}元，")
    else:
        money -= num
        print(f"{name}，你好，你取款{num}元成功。")
        query(False)

def main():
    print("--------主菜单----------")
    print(f"{name}，你好，欢迎来到xx取款机：")
    print("查询余额 [请输入1]")
    print("存款    [请输入2]")
    print("取款    [请输入3]")
    print("退出    [请输入4]")
    return input("请选择你的操作：")

while True:
    key_ipnut = main()
    if key_ipnut == "1":
        query(True)
        continue
    elif key_ipnut == "2":
        num = int(input("你需要存多少钱？ 请输入："))
        saving(num)
        continue
    elif key_ipnut == "3":
        num = int(input("你需要取多少钱？请输入："))
        get_money(num)
        continue
    else:
        print("程序结束")
        break




















