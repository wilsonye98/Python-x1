import re

password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,12}$'

password_list = []
successful_passwords = []

while True:
    password = input('Password: ')
    if password:
        password_list.append(password)
    else:
        break

for password in password_list:
    if re.search(password_regex, password):
        successful_passwords.append(password)

print(successful_passwords)
