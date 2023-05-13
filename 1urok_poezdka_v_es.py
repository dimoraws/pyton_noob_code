residence_cost = 200
exchange_rate_ruble = 80

print('Курс рубля:', exchange_rate_ruble, 'рублей = 1 Евро')

residence_limit = 90
shengen_constaint = 180

first_time_arriving = 5
first_time_leave = 17

second_time_arriving = 25
second_time_leave = 50

third_time_arriving = 75
third_time_leave = 112

# total_time_in_es = (first_time_leave - first_time_arriving + 1) + (second_time_leave - second_time_arriving + 1) + (third_time_leave - third_time_arriving + 1)

total_time_in_es = first_time_leave - first_time_arriving + 1
total_time_in_es += second_time_leave - second_time_arriving + 1
total_time_in_es += third_time_leave - third_time_arriving + 1

total_expenses = residence_cost * total_time_in_es


print('Потратим:', total_expenses, 'Евро')

total_expenses_ruble = total_expenses*exchange_rate_ruble

print('Потратим:', total_expenses_ruble, 'Рублей')
print('-------------------------------------------')

print('Дней в Евросоюзе:', total_time_in_es)

if total_time_in_es == 77:
    print('Поездака в Италию в подарок!!!')

if total_time_in_es > residence_limit:
    # На сколько дней превышен
    residence_fault = shengen_constaint - total_time_in_es
    print('Лимит пребывания в Евросоюзе, превышен на:', residence_fault)
    print('Пожалуйста выберите другие даты')
else:
    print('Не волнуйтесь, вы успеваете побывать в ЕС')

month_accumulate_salary = 5
oleg_salary = [1000, 1200, 1000, 1120, 700]
olga_salary = [900, 1100, 1300, 600]
oleg_budget = sum(oleg_salary)
olga_average_salary = sum(olga_salary)/len(olga_salary)
olga_budget = olga_average_salary * month_accumulate_salary

common_budget = (oleg_budget + oleg_budget)

if common_budget > total_expenses:
    print('Ура, едем!!!')
else:
    print('Бюджета не хватит :(')