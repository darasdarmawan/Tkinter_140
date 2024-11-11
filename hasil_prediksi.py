import tkinter as tk
from tkinter import messagebox

#fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try:
        for entry in entries:
            nilai = int(entry.get())  #mengkonversi teks dari entry menjadi integer
            if not (0 <= nilai <= 100):  #memastikan nilai berada dalam rentang 0-100
                raise ValueError("Nilai harus antara 0 dan 100.")
        #jika semua nilai valid, hasil prediksi ditampilkan
        hasil_label.config(text="Prediksi Prodi : Teknologi Informasi")
    except ValueError:
        #menampilkan pesan kesalahan jika input tidak valid
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

#jendela utama Tkinter
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  #menuliskan judul 
root.geometry("500x600")  #menentukan ukuran(500x600)
root.configure(bg="#ffc0cb")  #warna backgorund menjadi pink

# label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Helvetica", 16), bg="#ffc0cb")
judul_label.pack(pady=20) #label dengan padding vertikal 20

# Membuat frame untuk mengelompokkan input nilai
frame_input = tk.Frame(root, bg="#ffc0cb")
frame_input.pack(pady=10)    #label dengan padding vertikal 10

entries = []  #menyimpan widget entry input nilai
for i in range(10):  # mengulang input nilai sebanyak 10 kali
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i+1}:", bg="#ffc0cb")  #label untuk input
    label.grid(row=i, column=0, padx=5, pady=5, sticky="e")  
    entry = tk.Entry(frame_input)  #entry untuk input nilai
    entry.grid(row=i, column=1, padx=5, pady=5) #menempatkan entry dengan grid
    entries.append(entry)  #masukin entry ke daftar entries

#tombol untuk menampilkan hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, bg="#fffacd", font=("Helvatica", 12))
prediksi_button.pack(pady=20) 

#label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#ffc0cb")
hasil_label.pack(pady=10)  

#menjalankan aplikasi Tkinter
root.mainloop()
