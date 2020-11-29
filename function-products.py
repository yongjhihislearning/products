import os # operating system作業系統
# 讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品, 價格' in line:
				continue # 繼續，跳到下一回，跳過7-8行，不會跳出迴圈 
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

# 讓使用者輸入
def user_input(products):
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
	return products

# 印出所有購買紀錄
def print_products(products):
	for i in products:
		print(i[0], '的價格是', i[1])

# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品, 價格\n')
		for i in products:
			f.write(i[0] + ',' + str(i[1]) + '\n')
def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # 檢查檔案在不在
		print('yeah! 找到檔案了!')
		products = read_file(filename)
	else:
		print('找不到檔案......')
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)
main()