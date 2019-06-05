list1 = [0, 1, 2]
list2 = [3, 4, 5]
list3 = ["Yuko", "Ren", "Yushi", "Esteban"]
list4 = [0, 1, 2, 3, 4, 5, 6, 7]


total = list1 + list2
total_new = []
total_name = []
total_esteban = []

total_n_name = []

total_even = []
total_odd = []

for i in total:
    num = i + 3
    total_new.append(num)

for i in list3:
    name = i + "-san"
    total_name.append(name)

for i in list3:
    if i == "Esteban":
        new_name = i + "-san"
    else:
        new_name = i
    total_esteban.append(new_name)

for i in list4:
    if i % 2 == 0:
        total_even.append(i)
    else:
        total_odd.append(i)
    
    
#Homework by 6/7 Friday

#Pick up names if you find an 'n' inside the name and create new list and print
#Divide the list4 into even and odd lists

print(total)
print(total_new)
print(total_name)
print(total_esteban)

print(total_n_name)

print(total_even)
print(total_odd)