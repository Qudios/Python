from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("Key.Key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    file = open("Key.Key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("Type your Master Password? ")
key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print(f"User: {user}, Password: {fer.decrypt(password.encode()).decode()}")


def add():
    name = input("Name: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Like to Make New Password or See Existing ones (view, add, q (quit))?").lower()
    if mode == "view":
        view()
    elif mode == "q":
        break
    elif mode == "add":
        add()
    else:
        print("Bad Input Go BAck")
        continue
