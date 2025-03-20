# Ürün Satış Analizi
import numpy as np
import matplotlib.pyplot as plt

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
