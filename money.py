usd = 57
euro = 60

money = int(input("Введите сумму,которую вы хотите обменять"))
currency = int(input("Укажите код валюты (Евро - 401,Доллар США - 400): "))

if currency == 400:
    cache = round(money/usd, 2)
    print("Валюта:Доллары США")
elif currency == 401:
    cache = round (money/euro, 2)
    print("Валюта:Евро")
else:
    cache = 0
    print("Неизвестная валюта")
print("К получени:", cache)

