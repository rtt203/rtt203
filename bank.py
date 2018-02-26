import credit

def main():
    rate = int(input('Введите процентную ставку:'))
    money = int(input('Введите сумму:'))
    period = int(input('Введите период счёта в месяцах:'))

    result=credit.calculate_income(rate,money,period)
    print("Параметры счёта :\n ", "Сумма: ", money, "\n", "Ставка: ", rate, "\n", "Период :", period,
          "Сумма на счёте в конце периода: ", result)

if __name__ == '__main__':
    main()