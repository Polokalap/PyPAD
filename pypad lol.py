import os
import random

data = []

def save():
    name = input("File's name: ")
    file_path = f"{name}.txt"
    with open(file_path, "a") as f:
        for line in data:
            f.write(f"{line}\n")
    if os.path.exists(file_path):
        print(f"File '{file_path}' has been created successfully.")
    else:
        print(f"Error: File '{file_path}' was not created.")
    with open(file_path, "r") as f:
        print(f.read())
print("Hewwo welcome to my awesome text editor.")

line = 1
text = ""

while text != "\\.exit":
    text = input(f"{line} > ")
    if text == "\\.save":
        save()
    elif text == "\\.goto":
        g = input("Line: ")
        gint = int(g)

        gint -= 1
        data[gint] = input(f"{g} > ")
    elif text == "\\.text":
        temp = data.copy()
        for line in temp:
            print(f"{line}\n")

        for item in data:
            temp.remove(item)
        print(temp)

    elif text != "\\.exit":
        data.append(text)
        line += 1
