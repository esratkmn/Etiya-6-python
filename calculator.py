def toplama(a,b): 
  print(a+b) 
  
def cikarma(a,b): 
  print(a-b) 

def carpma(a,b): 
  print(a*b) 
  
def bolme(a,b): 
    x = (a / b) 
    print(x)
def mod(a,b):
   print(a%b)    

while True :
    secim = input("Seçenekler: +, -, *, /, % -> ") 
    if secim== "q":
       break  
    if secim not in ["+","-","*","/","%"]:
       print("Hatalı giriş yaptınız.")
       continue
    print(secim) 
    a = int(input("İlk sayı: "))
    b = int(input("İkinci sayı: "))  
    if secim == "+": toplama(a,b)
    elif secim == "-": cikarma(a,b)
    elif secim == "*": carpma(a,b) 
    elif secim == "/": bolme(a,b) 
    elif secim == "%": mod(a,b) 
    else: print("Hatalı giriş yaptınız.")

