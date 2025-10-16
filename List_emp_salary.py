employees = ['David C.', 'Sean S.', 'Shaun A.', 'Devin S.', 'Chastin S.', 'John D.', 'Mallorie V.', 'Erica S.', 'Lisa V.', 'Austin G.']

salary_list = [50000, 505000, 51000, 51500, 52000, 52500, 53000, 53500, 54000, 54500]

sublist1 = employees[:5]
sublist2 = employees[5:]

print('Sublist 1:', sublist1)
print('Sublist 2:', sublist2)

new_emp = input('Enter name of new Employee: ')

def new_employee():
    sublist2.append(new_emp)
    print(sublist2)

new_employee()

def remove_employee():
    sublist1.remove('Sean S.')
    print('Revised sublist 1 after removal: ', sublist1)

remove_employee()

merge_list = sublist1 + sublist2

print('This is the lists merged: ' + str(merge_list))

def salary_raise():
    for i in range(len(employees)):
        upd_salary = (4 / 100) * salary_list[i] + salary_list[i]
        print(employees[i], 'earns', upd_salary)

salary_raise()
    
