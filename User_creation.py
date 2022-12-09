
import random
from datetime import datetime

file_user = open("users.txt", "a+")
file_user.close()
file_log = open("log.txt", "a+")
file_log.close()

def pass_length(password :str):
    success_pass = False
    if len(password) >= 7:
        success_pass = True
    return success_pass

def pass_special_check(password :str):
    success_pass = False
    if "!" not in password and '@' not in password and ':' not in password and '$' not in password and '?'not in password:
        success_pass = True
    return success_pass

def first_check(password :str):
    if(pass_length(password)) and pass_special_check(password):
        return True
    else:
        return False

def swap_character(password :str):
    first = password[0]
    last = password[-1]
    middle = password[1:-1]
    return last + middle + first

def encrypt(password :str):
    enc = 'Error'
    if first_check(password):
        enc = swap_character(password)
        enc = enc.replace('i', '!')
        enc = enc.replace('a', '@')
        enc = enc.replace('S', '$')
        enc = enc.replace('J', '?')
    return enc

def user_creation():
    user_number1 = random.randint(0, 9)
    user_number2 = random.randint(0, 9)
    user_number3 = random.randint(0, 9)
    user_number4 = random.randint(0, 9)
    
    first = input('enter first name ')
    second = input('enter last name ')
    username = first[0:1] + second[:]
    username = "\n" + username.lower() + str(user_number1) + str(user_number2) + str(user_number3) + str(user_number4) + ":" 
    password = input("Please enter a password for new user ")
    encpassword = encrypt(password)
    if not password == "Error":
        repass = input("Re-enter password ")
        if repass == password:
            file = open("users.txt", "a")
            file.write(username + encpassword)
            file.close()
        else:
            print("fail")        

def user_check():
    check_user = input("Are you an existing user? y/n ")
    if check_user == 'y':
        file = open("users.txt", "r")
        check = input("Please enter your username ")
        for line in file:
            if check == get_user(line):
                file.close()
                return get_user(line)
        file.close()
    if check_user == 'n':
        make_user = input("would you like to make a username? y/n ")
    if make_user == 'y':
        user_creation()
    elif make_user == 'n':
        print("Alright, goodbye")
        exit()
    else:
        print("Bad Input")
        return "Error"
        file.close()
    
def get_user(line:str):
    found = line.find(":")
    user_found = line[:found]
    return user_found

def get_pass(line:str):
    found = line.find(":")
    pass_found = line[found+1:-1]
    return pass_found

def prompt_password():
    file = open("users.txt", "r")
    status = "OK"
    invalid_attempts = 1
    read = file.readlines()
    prompt = input('Please enter your password ')
    prompt = encrypt(prompt)
    while invalid_attempts < 3:
        for line in read:
            if prompt in line:
                invalid_attempts = 99
                return status
                break
        file.close()
        if prompt not in get_pass(line):
            failed = " "
            prompt = input("Invalid password, try again ")
            invalid_attempts += 1
            if invalid_attempts == 99:
                failed = "FAIL"
                return failed
            else:
                print("Please try again later")
            return "FAIL"

def logging(user, status):
    file = open("log.txt", "a")
    now = str(datetime.now())
    file.write(user + ':')
    file.write(status + ':')
    file.write(now)
    file.close()

def main():
    user = user_check()
    status = prompt_password()
    logging(user, status)
main()