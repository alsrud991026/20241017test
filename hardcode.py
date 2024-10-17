# 취약한 코드: 비밀번호가 하드코딩됨
password = "supersecretpassword"

def authenticate(user_input):
    if user_input == password:
        print("Access Granted")
    else:
        print("Access Denied")

user_input = input("Enter password: ")
authenticate(user_input)
