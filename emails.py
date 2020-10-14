try:
    emailaddress = input("Enter your email address : ").strip()
    user = emailaddress[:emailaddress.index("@")]
    domain = emailaddress[emailaddress.index("@")+1:]
    print("You user name is : {} and domain : {}".format(user, domain))
except ValueError:
    print("Please enter the full email address ")