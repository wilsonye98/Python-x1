# Assuming that we have some email addresses in the "username@companyname.com"
# format, please write program to print the company name of a given email address.
# Both user names and company names are composed of letters only.

def company_split(email):
    name, company = email.split('@')
    company_name, web = company.split('.')
    print(company_name)

get_email = input('Please enter an email address: ')
company_split(get_email)