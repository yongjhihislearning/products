# 讀取檔案
products = []
with open('products.csv', 'r') as f:
	for line in f:
		if '商品, 價格' in line:
			continue # 繼續，跳到下一回，跳過7-8行，不會跳出迴圈 
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

# 讓使用者輸入
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

# 印出所有購買紀錄
for i in products:
	print(i)
	print(i[0], '的價格是', i[1])

# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'
# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品, 價格\n')
	for i in products:
		f.write(i[0] + ',' + i[1] + '\n')