ls = ["Anoop", "Vibhav", 1, 5, 420, "Karan", "Harshit", 69, "Pranav", 420, "Vibhav", "Harshit", 420, 69 , 420, "Pranav"]


str_ls = []

for element in ls:
    str_ls.append(str(element))

print(str_ls)

for element in str_ls:
    count = str_ls.count(element)
    if count > 1 :
        for i in range(1, count):
            str_ls.remove(element)

print(str_ls )