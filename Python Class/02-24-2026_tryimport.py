try:
    with open("february.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file doesn't exists, please create it!")