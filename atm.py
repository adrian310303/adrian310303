print("===========ATM============")
print("selamat datang di atm saya")
print("pilih option: ")
print("1. chek uang")
print("2. ambil uang saya")
print("3. tabung uang saya")
print("===========ATM============")

option=int(input("silahkan pilih option : "))

if option==1:
	print("uang kamu berjumlah RP.200.000")
elif option==2:
	print("uang kamu berjunlah RP.200.000, Mau ambil berapa? ")
	print("1. RP.100.000")
	print("2. RP.200.000")
	uang_kamu=2000000
	option2=int(input("option: "))
	if option2==1:
		hasil1=uang_kamu -1000000
		print("uang kamu sekarang berjumlah: ",hasil1)
	elif option2==2:
		hasil2=uang_kamu -2000000
		print("uang kamu sekarang berjumlah: " ,hasil2)


elif option==3:
		uang_kamu=2000000
		print("uang berjumlah RP.200.000")
		option3=int(input("masukan jumlah uang: "))
		hasil3=uang_kamu+option3
		print("uang kamu sekarang berjumlah: " ,hasil3)