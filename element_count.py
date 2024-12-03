ls = ["Anoop", "Vibhav", 1, 5, 420, "Karan", "Harshit", 69, 420, "Vibhav", "Harshit"]

str_ls = []

for element in ls:
    str_ls.append(str(element))

choice = input("Enter the element you want to search for: ")

print(f"'{choice}'", "occured",str_ls.count(choice), "time(s)")