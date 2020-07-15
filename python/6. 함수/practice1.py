# 함수

def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100 # 수수료
    return commission, balance-money-commission
open_account()

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 200)

commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원, 잔액은 {1} 원".format(commission, balance))