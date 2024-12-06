n = int(input())
count = 0

phone_dict = {}

while count < n:
    user_phone = input().split(' ')
    phone_dict[user_phone[0]] = user_phone[1]
    count += 1

while True:
    try:
        get_user = input()
        if get_user in phone_dict:
            print(f"{get_user}={phone_dict[get_user]}")
        else:
            print('Not found')
    except:
        break

