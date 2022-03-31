cotdol = float(input("Cotação do Dólar: R$ "))
qtddol = float(input("Quantidade a ser comprada: US$ "))

convdol = cotdol * qtddol

print ("Você precisa de R${} para comprar US${} ".format(convdol, qtddol))
