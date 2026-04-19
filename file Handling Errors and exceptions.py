try:
    file = open("file.txt", "r")
    content = file.read()
    print(content)

finally:
    file.close()
    print("File closed")
