email = input("Please input Email to Check: ")

if len(email)>6:
    if email[0].isalpha :
        if ("@" in email) and (email.count("@") == 1):
            if (email[-3] == '.') ^ (email[-4] == '.'):
                for i in email:
                    if i == ' ':
                        print("Cant hold whitespace character")
                        break
                    elif i == i.isupper:
                        print("Wrong format")
                    else:
                        
            else:
                print("Wrong Format")
        else:
            print("Wrong Format")
    else:
        print("first should be capital")
else:
    print("Length should be greater than 6 digits")