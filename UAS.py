def Penjumlahan():
	hasil=500+200
	return hasil
  
def Penjumlahan(*args):
	hasil=500+200
	return hasil
  
def Pengurangan():
	hasil=700-190
	return hasil
  
def Pengurangan(*args):
	hasil=700-190
	return hasil
  
def Tampil(func,func1):
	print "Anto memiliki bebek ",func()," ekor di Mataram"
	print "Bebek anto pada tahun 2013 menjadi ",func1()," karena mati keracunan"

def Utama():
	Tampil(Penjumlahan,Pengurangan)

#pemanggilan fungsi Utama
Utama()
