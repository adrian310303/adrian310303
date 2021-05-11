nama_pertama = "Esta"
nama_kedua = "kayla Rianti"
nama_ketiga = "Al'farhad"

nama_lengkap = nama_pertama + " " + nama_kedua + " " + nama_ketiga

print(nama_lengkap)

panjang = len(nama_lengkap)

print("panjang dari " + nama_lengkap + " =" + str(panjang))


d = "d"
status = d in nama_lengkap
print("apakah " + d + " ada di " + nama_lengkap + ", " + str(status))

D= "D"
status = D in nama_lengkap
print("apakah " + D + " ada di " + nama_lengkap + ", " + str(status))

x = "x"
status = x not in nama_lengkap
print("apakah " + x + " tidak ada di " + nama_lengkap + ", " + str(status))

print("index ke-0 : " + nama_lengkap[0]) # dimulai dari 0
print("index ke-6 : " + nama_lengkap[6]) # index bebas
print("index ke-(-1) : " + nama_lengkap[-1]) # indexing dari dibelakang
print("index ke-[6,8) : " + nama_lengkap[6:8]) # dimulai dari index 6 sampai sebelum 8
print("index ke-[0,2,4,6,8] : " + nama_lengkap[0:10:2]) # diambil index 0,2,4,6,8

print("nilai terkecil : " + min(nama_lengkap))

print("nilai terbesar : " + max(nama_lengkap))


ascii_code = ord("y")
print("ASCII number dari y : " + str(ascii_code))
data = 130
print("Character dari ascii code 117 : " + chr(data))