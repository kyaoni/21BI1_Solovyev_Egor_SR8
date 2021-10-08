b=''
d=''
try:
	a=int(input('Введите десятичное число '))
except ValueError:
	print('Ошибка ввода ')
	exit()
else:
	try:
		n=int(input('Введите систему счисления, в которую хотите перевести число (двоичную или восьмеричную) '))
	except ValueError:
		print('Ошибка ввода')
		exit()
	else:
		if (n==8) or (n==2):
			def eight():
				global a, d
				if n==8:
					while a>0:
						d=str(a%8)+d
						a=a//9
					print(d)
			def two():
				global a, b
				if n==2:
						while a>0:
							b=str(a%2)+b
							a=a//2
						print(b)
			if n==2:
				two()
			if n==8:
				eight()
		else:
			print('Введено неверное значение для системы счисления ')