import random

bilgisayar = random.randint(1,30)
for i in range(5):
    
    sayigir = int(input("""5 Hakkın var...
Lütfen bir sayı giriniz: """))
    if bilgisayar%2==0 and bilgisayar%3==0:
        print("Tuttuğum sayı 2 ve 3'ün katı! Küçük bir ipucu...")
    elif bilgisayar%2==0:
        print("Tuttuğum sayı 2'nin  katı! Küçük bir ipucu...")
    elif bilgisayar%5==0:
        print("Tuttuğum sayı 5'in katı.. Bence baya büyük bir ipucu...")
    if sayigir == bilgisayar:
        print("Doğru bildin!")
        break
    elif sayigir>bilgisayar:
        print("Daha düşük sayılara gitmelisin!")
    else:
        print("Daha yüksek sayılara gitmelisin!")
        
else:
    print("Kaybettin!!!")

#Discord: letmecode
#Instagram: egetunc_