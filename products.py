products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = []
	p.append(name)
	p.append(price) # 7-9行可寫成p = [name, price]
	products.append(p) # 7-10行可寫成products.append([name, price])
print(products)
print(products[0][0])

for i in products:
	print(i)
	print(i[0], '的價格是', i[1])