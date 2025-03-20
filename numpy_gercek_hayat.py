import numpy as np
import matplotlib.pyplot as plt

# Şirket Maaş Analizi
def maas_analizi():
    maaslar = np.random.randint(3000, 15001, 500)
    ortalama_maas = np.mean(maaslar)
    max_maas = np.max(maaslar)
    min_maas = np.min(maaslar)

    print(f"Ortalama Maaş: {ortalama_maas:.2f} TL")
    print(f"Maksimum Maaş: {max_maas} TL")
    print(f"Minimum Maaş: {min_maas} TL")

    plt.hist(maaslar, bins=10, color='blue', edgecolor='black')
    plt.title('Maaş Dağılımı')
    plt.xlabel('Maaş (TL)')
    plt.ylabel('Kişi Sayısı')
    plt.show()

# Hava Durumu Analizi
def sicaklik_analizi():
    sicakliklar = np.random.uniform(-10, 40, 365)
    ortalama_sicaklik = np.mean(sicakliklar)
    en_sicak_gun = np.max(sicakliklar)
    en_soguk_gun = np.min(sicakliklar)

    print(f"Ortalama Sıcaklık: {ortalama_sicaklik:.2f} °C")
    print(f"En Sıcak Gün: {en_sicak_gun:.2f} °C")
    print(f"En Soğuk Gün: {en_soguk_gun:.2f} °C")

    plt.plot(sicakliklar, color='red')
    plt.title('365 Günlük Sıcaklık Değişimi')
    plt.xlabel('Gün')
    plt.ylabel('Sıcaklık (°C)')
    plt.show()

# Ürün Satış Analizi
def satis_analizi():
    urunler = ["Telefon", "Bilgisayar", "Kulaklık", "Saat", "Tablet"]
    satislar = np.random.randint(10, 101, (5, 30))

    toplam_satis = np.sum(satislar, axis=1)
    ortalama_satis = np.mean(satislar, axis=1)

    for i, urun in enumerate(urunler):
        print(f"{urun} - Toplam Satış: {toplam_satis[i]}, Ortalama Satış: {ortalama_satis[i]:.2f}")

    plt.bar(urunler, toplam_satis, color=['blue', 'green', 'red', 'purple', 'orange'])
    plt.title('Ürün Bazında Toplam Satışlar')
    plt.xlabel('Ürünler')
    plt.ylabel('Toplam Satış Miktarı')
    plt.show()

# Tüm fonksiyonları çalıştırma
maas_analizi()
sicaklik_analizi()
satis_analizi()

