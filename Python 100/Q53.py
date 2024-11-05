# Assuming that we have some email addresses in the "username@companyname.com"
# format, please write program to print the user name of a given email address.
# Both user names and company names are composed of letters only.

def email_split(email):
    name, company = email.split('@')
    print(name)

get_email = input('Please enter an email address: ')
email_split(get_email)