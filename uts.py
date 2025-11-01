import numpy as np
import matplotlib.pyplot as plt

# === Fungsi Keanggotaan Segitiga ===
def segitiga(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif x == b:
        return 1
    elif x < b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)

# === Input Data ===
permintaan = 2000
persediaan = 500

# === Rentang untuk plotting ===
x_permintaan = np.arange(0, 5001, 1)
x_persediaan = np.arange(0, 1001, 1)
x_produksi = np.arange(0, 8001, 1)

# === Fuzzy Set Permintaan ===
turun = [segitiga(x, 0, 1000, 3000) for x in x_permintaan]
naik = [segitiga(x, 1000, 3000, 5000) for x in x_permintaan]

# === Fuzzy Set Persediaan ===
sedikit = [segitiga(x, 0, 200, 400) for x in x_persediaan]
sedang = [segitiga(x, 200, 500, 800) for x in x_persediaan]
banyak = [segitiga(x, 600, 800, 1000) for x in x_persediaan]

# === Fuzzy Set Produksi ===
berkurang = [segitiga(x, 0, 2000, 7000) for x in x_produksi]
bertambah = [segitiga(x, 2000, 7000, 8000) for x in x_produksi]

# === Fuzzifikasi Nilai Input ===
μ_turun = segitiga(permintaan, 0, 1000, 3000)
μ_naik = segitiga(permintaan, 1000, 3000, 5000)
μ_sedikit = segitiga(persediaan, 0, 200, 400)
μ_sedang = segitiga(persediaan, 200, 500, 800)
μ_banyak = segitiga(persediaan, 600, 800, 1000)

# === Aturan Fuzzy ===
# 1. TURUN & BANYAK -> BERKURANG
r1 = min(μ_turun, μ_banyak)
# 2. TURUN & SEDANG -> BERKURANG
r2 = min(μ_turun, μ_sedang)
# 3. TURUN & SEDIKIT -> BERTAMBAH
r3 = min(μ_turun, μ_sedikit)
# 4. NAIK & BANYAK -> BERKURANG
r4 = min(μ_naik, μ_banyak)
# 5. NAIK & SEDANG -> BERTAMBAH
r5 = min(μ_naik, μ_sedang)
# 6. NAIK & SEDIKIT -> BERTAMBAH
r6 = min(μ_naik, μ_sedikit)

# === Agregasi ===
α_berkurang = max(r1, r2, r4)
α_bertambah = max(r3, r5, r6)

# === Defuzzifikasi (Metode Centroid sederhana) ===
z_berkurang = 2500
z_bertambah = 6000
z = (α_berkurang * z_berkurang + α_bertambah * z_bertambah) / (α_berkurang + α_bertambah)

# === Output ke Terminal ===
print("=== HASIL FUZZY INFERENCE SYSTEM ===")
print(f"Permintaan: {permintaan}")
print(f"Persediaan: {persediaan}")
print(f"μ TURUN = {μ_turun:.2f}, μ NAIK = {μ_naik:.2f}")
print(f"μ SEDIKIT = {μ_sedikit:.2f}, μ SEDANG = {μ_sedang:.2f}, μ BANYAK = {μ_banyak:.2f}")
print(f"Produksi BERKURANG = {α_berkurang:.2f}")
print(f"Produksi BERTAMBAH = {α_bertambah:.2f}")
print(f"\n➡️ Produksi disarankan: {z:.2f} kemasan")

# === Visualisasi Grafik ===
plt.figure(figsize=(12, 8))

# Grafik Permintaan
plt.subplot(3, 1, 1)
plt.plot(x_permintaan, turun, 'b', label='Turun')
plt.plot(x_permintaan, naik, 'r', label='Naik')
plt.title('Fungsi Keanggotaan Permintaan')
plt.xlabel('Permintaan (kemasan)')
plt.ylabel('Derajat Keanggotaan')
plt.legend()
plt.grid(True)

# Grafik Persediaan
plt.subplot(3, 1, 2)
plt.plot(x_persediaan, sedikit, 'b', label='Sedikit')
plt.plot(x_persediaan, sedang, 'orange', label='Sedang')
plt.plot(x_persediaan, banyak, 'g', label='Banyak')
plt.title('Fungsi Keanggotaan Persediaan')
plt.xlabel('Persediaan (kemasan)')
plt.ylabel('Derajat Keanggotaan')
plt.legend()
plt.grid(True)

# Grafik Produksi
plt.subplot(3, 1, 3)
plt.plot(x_produksi, berkurang, 'b', label='Berkurang')
plt.plot(x_produksi, bertambah, 'orange', label='Bertambah')
plt.title('Fungsi Keanggotaan Produksi')
plt.xlabel('Produksi (kemasan)')
plt.ylabel('Derajat Keanggotaan')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()