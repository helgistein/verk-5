def get_emails():
    emails = []
    i = ""
    while i != "q":
        i = input("Email address: ")
        emails.append(i)
    return emails[:-1]

def get_names_and_domains(emails):
    names_and_dom = []
    for x in emails:
        splitted = tuple(x.split("@"))
        names_and_dom.append(splitted)
    return names_and_dom

        





# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)
