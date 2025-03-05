
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
    # İşlem fonksiyonlarını bir sözlükte toplama
    islemler = {
        "+": toplama,
        "-": cikarma,
        "*": carpma,
        "x": carpma,  # Alternatif çarpma simgesi
        "/": bolme,
        "**": ussu,
        "%": mod_alma,
        "//": tam_bolme
    }

    # Kullanıcıdan işlemi alma
    hesap = input("Hesaplanacak İşlemi Girin (Örneğin 5 + 3): ")

    # Parçalara ayırmak ve verileri hazırlamak
    try:
        ilk, islem, ikinci = hesap.split(" ")
        ilk_sayi = int(ilk)
        ikinci_sayi = int(ikinci)
    except ValueError:
        print("Geçerli bir işlem yazın! Örneğin: 10 + 1")
        return

    # İşlemi kontrol et ve sonucu hesapla
    if islem in islemler:
        sonuc = islemler[islem](ilk_sayi, ikinci_sayi)
        print(f"{hesap} = {sonuc}")
    else:
        print("Geçersiz işlem! Lütfen +, -, *, /, **, %, // işlemlerinden birini girin.")

main()


