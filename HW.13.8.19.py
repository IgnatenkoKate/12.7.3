tickets = int(input('Введите количество билетов '))
age = int(input('Введите свой возраст '))
if age < 10 or tickets < 1:
    print('Некорректный ввод, попробуйте еще раз')
elif age < 18:
    print('Сумма к оплате=', 0, 'руб.', 'Вы проходите на конференцию бесплатно')
elif 18 <= age < 25 and tickets > 3:
    print('Сумма к оплате =', round(tickets * 990 * 0.90), 'руб.', 'Применена cкидка 10%')
elif 18 <= age < 25 and tickets < 3:
    print('Сумма к оплате=', round(tickets * 990), 'руб.')
elif age >= 25 and tickets > 3:
    print('Сумма к оплате =', round(tickets * 1390 * 0.90), 'руб.', 'Применена cкидка 10%')
elif age >= 25 and tickets < 3:
    print('Сумма к оплате =', round(tickets * 1390), 'руб.')
