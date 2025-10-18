email = input("Please input Email to Check: ")

if len(email)>6:
    if email[0].isalpha :
        if ("@" in email) and (email.count("@") == 1):
            pass
        else:
            print("Wrong Format")
    else:
        print("first should be capital")
else:
    print("Length should be greater than 6 digits")