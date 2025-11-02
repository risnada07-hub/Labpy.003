import random

def latihan5():
    # Meminta input nilai N
    while True:
        try:
            n_str = input("Masukkan nilai N: ")
            N = int(n_str)
            if N < 1:
                print("N harus bilangan bulat positif.")
                continue
            break
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")
    
    # Menghasilkan dan mencetak N bilangan acak
    for i in range(1, N + 1):
        # random.random() menghasilkan bilangan float acak dalam rentang [0.0, 1.0)
        data_random = random.random()
        print(f"data ke: {i} => {data_random}")
        
    # Mencetak pesan selesai
    print("Selesai")

