# Labpy.003 
import random

def latihan5():
    # Input dan validasi N
    while True:
        try:
        
            N = int(input("Masukkan nilai N: "))
            if N >= 1:
                break
            print("N harus bilangan bulat positif.")
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")
    
    # Mencetak N bilangan acak
    for i in range(1, N + 1):
        data_random = random.random()
        # Output contoh: data ke: 1 => 0.1729492204357056
        print(f"data ke: {i} => {data_random}")
        
    print("Selesai")



def latihan6():
    # Data Laba Bulanan (asumsi: total 19.000.000)
    laba_bulanan = [
        0.0, 0.0, 1000000.0, 1000000.0, 
        5000000.0, 5000000.0, 5000000.0, 2000000.0
    ]
    
    total_laba = 0.0
    
    # Loop untuk menampilkan dan menjumlahkan laba
    for i in range(len(laba_bulanan)):
        bulan_ke = i + 1
        laba = laba_bulanan[i]
        
        # Output contoh: laba bulan ke- 1 sebesar: 0
        print(f"laba bulan ke- {bulan_ke} sebesar: {laba}")
        
        total_laba += laba
        
    # Output total laba
    # Output contoh: Total laba adalah: 19000000.0
    print(f"Total laba adalah: {total_laba}")

if __name__ == "__main__":
    latihan6()



    def atm_simulator():
    # Saldo awal
    saldo = 1000000
    
    # Loop utama
    while True:
        print(f"\nSaldo saat ini: Rp {saldo}")
        print("1. Tarik Uang")
        print("2. Keluar")
        
        pilihan_menu = input("Pilih menu (1/2): ")
        
        if pilihan_menu == '1':
            try:
                jumlah_penarikan = int(input("Masukkan jumlah penarikan: "))
                
                if jumlah_penarikan > 0 and jumlah_penarikan <= saldo:
                    saldo -= jumlah_penarikan
                    print("Penarikan berhasil!")
                elif jumlah_penarikan > saldo:
                    print("Saldo tidak mencukupi!")
                else:
                    print("Jumlah penarikan harus positif.")
            except ValueError:
                print("Input tidak valid. Masukkan angka.")
            
        elif pilihan_menu == '2':
            print("Terima kasih telah menggunakan ATM!")
            break
            
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    atm_simulator()
