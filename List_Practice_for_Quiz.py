
colors = ["blue", "teal", "magenta", "red", "black"]
print(colors[0], ",", colors[2], ",", colors[4])
colors.append("brown")
print(colors)
print()
paychecks = [45, 60, 80, 200]
sum = 0
for i in range(len(paychecks)):
    sum += paychecks[i]
print("sum", sum)
print()
foods = []
user = int (input("How many types of food do you want?"))
for i in range(user):
    choice = input("What food do you want?")
    foods.append(choice)
print()
print(foods)
print()
print()




