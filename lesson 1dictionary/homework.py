username_password={
    "abby1":"6458399",
    "honey":"224413",
    "sweat!":"99835",
    "qween":"0018735",
    "cassy34":"767593",
    "sandy4":"228867",
    "daisy":"838934",
    "frogy":"8656434",
    "bossbaby":"165543",
    "blaze":"534668"

}
username=input("your username")
password=input("your password")
if username not in username_password:
    print("you are not a valid user of this system")
else:
    if username_password[username]==password:
        print("you are a valid user of this system")
    else:
        print("incorrect password")
