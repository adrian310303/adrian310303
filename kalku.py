while (True):
	print("========kalkulator==========")
	print("1. penambahan")
	print("2. pengurangan")
	print("3. perkalian")
	print("4.pembagian")
	print("5. keluar")
	print("=========adrian===========")
	
	j = int(input("masukan pilihan anda: "))
	
	if j ==1:
		a = int(input("masukan angka1: "))
		b = int(input("masukan angka2: "))
		c = a + b		
		print(a, "+" , b,"=" ,c)
		print("")
	elif j==2:
		a = int(input("masukan angka1: "))
		b = int(input("masukan angka2: "))
		c = a - b		
		print(a, "-" , b,"=" ,c)
		print("")
	elif j==3:
		a = int(input("masukan angka1: "))
		b = int(input("masukan angka2: "))
		c = a * b		
		print(a, "x" , b,"=" ,c)
		print("")
	elif j==4:
		a = int(input("masukan angka1: "))
		b = int(input("masukan angka2: "))
		c = a / b		
		print(a, ":" , b,"=" ,c)
		print("")
	else:
		break
print("bye bye")