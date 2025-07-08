with open("notes.txt", "w") as file:
    file.write("Today I started learning file handling in Python.\n")
    file.write("I understood how to write and read files.\n")
    file.write("Feeling more confident with each step!\n")

with open("notes.txt", "r") as file:
    print("Reading from notes.txt:")
    for line in file:
        print(line.strip())  # strip() removes the newline character