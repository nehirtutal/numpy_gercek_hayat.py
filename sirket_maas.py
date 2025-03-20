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
