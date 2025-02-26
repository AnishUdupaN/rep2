employee = {
    'name': input('Enter employee name: '),
    'employee id': int(input('Enter employee Id: ')),
    'basic salary': float(input('Enter employee salary: ')),
    'allowances': float(input('Enter employee allowances: ')),
    'bonus percentage': float(input('Enter employee bonus percentage: '))
}

monthly_gross_salary = employee['basic salary'] + employee['allowances']
annual_gross_salary = monthly_gross_salary * 12 + (employee['bonus percentage'] / 100 * (monthly_gross_salary * 12))
employee['monthly gross salary'] = monthly_gross_salary
employee['annual gross salary'] = annual_gross_salary

print('\nEmployee details are:')
print('-' * 50)

for key, value in employee.items():
    print(f'{key.title():<20} = {value}')

print('-' * 50)
