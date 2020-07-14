# For
print("list for")
for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))

print("range(5) for")
for wait_range in range(5):
    print("대기번호 : {0}".format(wait_range))

print("range(1, 6) for")
for wait_range in range(1, 6):
    print("대기번호 : {0}".format(wait_range))


starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    # print("손님 : {}".format(customer))
    print(f"손님 : {customer}")