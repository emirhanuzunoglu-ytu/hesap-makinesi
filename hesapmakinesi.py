
def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def bolme(a, b):
    if b == 0:
        return "Bir sayıyı 0'a bölemezsiniz!"
    return round(a / b, 2)

def carpma(a, b):
    return a * b

def ussu(a, b):
    return a ** b

def mod_alma(a, b):
    return a % b

def tam_bolme(a, b):
    return a // b

def main():
    
    islemler = {
        "+": toplama,
        "-": cikarma,
        "*": carpma,
        "x": carpma,  
        "/": bolme,
        "**": ussu,
        "%": mod_alma,
        "//": tam_bolme
    }

    hesap = input("Hesaplanacak İşlemi Girin (Örneğin 5 + 3): ")

    try:
        ilk, islem, ikinci = hesap.split(" ")
        ilk_sayi = int(ilk)
        ikinci_sayi = int(ikinci)
    except ValueError:
        print("Geçerli bir işlem yazın! Örneğin: 10 + 1")
        return

    if islem in islemler:
        sonuc = islemler[islem](ilk_sayi, ikinci_sayi)
        print(f"{hesap} = {sonuc}")
    else:
        print("Geçersiz işlem! Lütfen +, -, *, /, **, %, // işlemlerinden birini girin.")

main()


