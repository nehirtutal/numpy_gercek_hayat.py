# Hava Durumu Analizi
import numpy as np
import matplotlib.pyplot as plt

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
