import random

cevaplar = ["Bu Senin Kaderin","Cevabı Yakın Bir Arkadaşından Gelecek.", "Cevabım Hayır", "Bence Başka Bir Şey Sor", "Senin İçin İyi Bir Karar Değil", "Cevabım Evet","Bunun Cevabını Ben Veremem", "Kaçınılmaz Evet", "Sorduğun Olmayacak Ama Daha İyisi Senin İçin Olacak", "Bu Soruyu Duymamış Olayım!", "Cevabı Senin Yüreğinde","olabilir","olamaz","üç vakte kadar","uğursuzlu olabilir","senin için üzüntülü bir dönem","negatif olaylar","merak etme olur" ]
while True:
  soru = input("sihirli küreye ne sormak istersiniz:")
  if len(soru) < 5:
    print("soru sormadınız!")

  elif soru == "saçmalama":
        print("Cevap: Bu bir saçmalık!")

  else:
    cevap= random.choice(cevaplar)
    print("cevap:",cevap)
    
 
