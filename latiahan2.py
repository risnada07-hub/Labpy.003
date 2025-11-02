def latihan6():
    # Definisikan laba bulanan sesuai dengan output yang terlihat.
    # Laba untuk bulan ke-1 hingga ke-8
    # Bulan 1 & 2: 0
    # Bulan 3 & 4: 1000000.0
    # Bulan 5, 6, 7: 5000000.0
    # Bulan 8: 2000000.0
    laba_bulanan = [
        0.0,         # Bulan 1
        0.0,         # Bulan 2
        1000000.0,   # Bulan 3
        1000000.0,   # Bulan 4
        5000000.0,   # Bulan 5
        5000000.0,   # Bulan 6
        5000000.0,   # Bulan 7
        2000000.0    # Bulan 8
    ]
    
    # Inisialisasi variabel untuk menghitung total laba
    total_laba = 0.0
    
    # Loop untuk mencetak laba setiap bulan dan menghitung total
    for i in range(len(laba_bulanan)):
        # i + 1 digunakan untuk mendapatkan nomor bulan yang dimulai dari 1
        bulan_ke = i + 1
        laba = laba_bulanan[i]
        
        # Cetak laba bulan ke-i
        print(f"laba bulan ke- {bulan_ke} sebesar: {laba}")
        
        # Tambahkan laba bulan ini ke total laba
        total_laba += laba
        
    # Setelah loop selesai, cetak total laba
    print(f"Total laba adalah: {total_laba}")
