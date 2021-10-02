input_money = int(input("투입한 돈: "))
price = int(input("물건값: "))

return_money = int(input_money - price)
print("거스름돈: ", return_money)

coin500s = return_money // 500
return_money = return_money % 500

coin100s = return_money // 100

print("500원 동전 갯수: ", coin500s)
print("100원 동전 갯수: ", coin100s)