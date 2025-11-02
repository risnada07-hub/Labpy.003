def atm_simulator():
    # Inisialisasi saldo awal
    saldo = 1000000
    
    # Loop utama program ATM
    while True:
        # Menampilkan saldo dan menu
        print(f"\nSaldo saat ini: Rp {saldo}")
        print("1. Tarik Uang")
        print("2. Keluar")
        
        # Meminta input pilihan menu
        pilihan_menu = input("Pilih menu (1/2): ")
        
        # --- Opsi 1: Tarik Uang ---
        if pilihan_menu == '1':
            try:
                # Meminta input jumlah penarikan
                jumlah_penarikan_str = input("Masukkan jumlah penarikan: ")
                jumlah_penarikan = int(jumlah_penarikan_str)
                
                # Cek apakah jumlah penarikan valid
                if jumlah_penarikan > 0:
                    # Cek apakah saldo mencukupi
                    if jumlah_penarikan <= saldo:
                        # Lakukan penarikan dan update saldo
                        saldo -= jumlah_penarikan
                        print("Penarikan berhasil!")
                    else:
                        print("Saldo tidak mencukupi. Penarikan dibatalkan.")
                else:
                    print("Jumlah penarikan harus lebih dari nol.")
            except ValueError:
                # Menangani jika input bukan bilangan bulat
                print("Input tidak valid. Masukkan angka.")
            
        # --- Opsi 2: Keluar ---
        elif pilihan_menu == '2':
            print("Terima kasih telah menggunakan ATM!")
            break  # Keluar dari loop utama
            
        # --- Opsi Tidak Valid ---
        else:
            print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
