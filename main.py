vize = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))
ortalama = (vize * 0.4) + (final * 0.6) 
sayi1=final
sayi2=vize
sayi3=ortalama
if sayi1<40:
    print("Maalesef kaldınız")
elif sayi2 == sayi1*2:
    print("Maalesef kaldınız")
elif  ortalama<50 :
    print("Maalesef kaldınız")
else:
    print("Geçtiniz")        




# eğer final 40'dan küçükse kullanıcı kaldı
# eğer ortalama 50'den küçükse kullanıcı kaldı
# eğer vize finalin 2 katı ise kullanıcı kaldı
# bunun dışındaki tüm durumlarda kullanıcı geçti yazdırmak istiyoruz. 