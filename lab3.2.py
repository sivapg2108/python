N = 10
with open("file.txt", "a") as file:  # the a opens it in append mode
    for i in range(N):
        line = next(file).strip()
        print(line)