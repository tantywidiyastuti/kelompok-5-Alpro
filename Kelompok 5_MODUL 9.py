import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading
import random

# Kumpulan kutipan motivasi
quotes = [
    "Percaya pada dirimu sendiri!",
    "Tetap positif, bekerja keras, dan wujudkan impianmu.",
    "Sukses bukanlah kebetulan.",
    "Terus maju, kamu hebat!",
    "Bermimpilah besar dan berani gagal."
]

# Fungsi untuk Timer
def start_timer():
    try:
        # Mengambil input durasi dalam menit dan mengubah ke detik
        minutes = int(timer_input.get())
        total_seconds = minutes * 60
        timer_label.config(text=f"Sisa Waktu: {total_seconds} detik")

        # Fungsi untuk menghitung mundur
        def countdown():
            for remaining in range(total_seconds, -1, -1):
                mins, secs = divmod(remaining, 60)  # Konversi ke menit dan detik
                timer_label.config(text=f"Sisa Waktu: {mins:02}:{secs:02}")
                time.sleep(1)
            # Pesan saat waktu habis
            messagebox.showinfo("Waktu Habis!", "Sesi belajar kamu selesai!")

        # Menjalankan fungsi hitung mundur dalam thread terpisah
        threading.Thread(target=countdown, daemon=True).start()
    except ValueError:
        # Menampilkan pesan kesalahan jika input tidak valid
        messagebox.showerror("Input Tidak Valid", "Masukkan angka yang valid.")

# Fungsi untuk To-Do List
def add_task():
    # Menambahkan tugas baru ke daftar
    task = task_input.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_input.delete(0, tk.END)  # Mengosongkan input setelah ditambahkan

def mark_done():
    # Menandai tugas sebagai selesai dengan mengganti warnanya
    selected = task_listbox.curselection()
    for index in selected:
        task_listbox.itemconfig(index, foreground="gray")

def clear_tasks():
    # Menghapus semua tugas dari daftar
    task_listbox.delete(0, tk.END)

# Fungsi untuk Catatan Harian
def save_note():
    # Menyimpan catatan ke file lokal
    note_text = notes_text.get("1.0", tk.END).strip()
    if note_text:
        with open("notes.txt", "w") as file:
            file.write(note_text)
        messagebox.showinfo("Berhasil", "Catatan berhasil disimpan!")

def load_note():
    # Membaca catatan dari file lokal
    try:
        with open("notes.txt", "r") as file:
            notes_text.delete("1.0", tk.END)
            notes_text.insert("1.0", file.read())
    except FileNotFoundError:
        messagebox.showwarning("Catatan Tidak Ditemukan", "Tidak ada catatan yang tersimpan.")

# Fungsi untuk Kalkulator Sederhana
def calculate():
    try:
        # Menghitung ekspresi matematika menggunakan eval
        result = eval(calculator_input.get())
        calculator_result_label.config(text=f"Hasil: {result}")
    except Exception:
        calculator_result_label.config(text="Kesalahan")

# Fungsi untuk Penghasil Kutipan Motivasi
def generate_quote():
    # Menampilkan kutipan acak
    quote_label.config(text=random.choice(quotes))

# Aplikasi Utama
root = tk.Tk()
root.title("Toolkit Produktivitas Mahasiswa")
root.geometry("600x600")  # Ukuran jendela utama

# Bagian Timer
timer_frame = ttk.LabelFrame(root, text="Timer Belajar")
timer_frame.pack(fill="x", padx=10, pady=5)
ttk.Label(timer_frame, text="Durasi (menit):").pack(side="left", padx=5, pady=5)
timer_input = ttk.Entry(timer_frame, width=10)
timer_input.pack(side="left", padx=5)
ttk.Button(timer_frame, text="Mulai", command=start_timer).pack(side="left", padx=5)
timer_label = ttk.Label(timer_frame, text="Sisa Waktu: --:--")
timer_label.pack(side="left", padx=10)

# Bagian Catatan Harian
notes_frame = ttk.LabelFrame(root, text="Catatan Harian")
notes_frame.pack(fill="x", padx=10, pady=5)
notes_text = tk.Text(notes_frame, height=10)
notes_text.pack(fill="x", padx=5, pady=5)
ttk.Button(notes_frame, text="Simpan", command=save_note).pack(side="left", padx=5)
ttk.Button(notes_frame, text="Muat", command=load_note).pack(side="left", padx=5)

# Bagian To-Do List
todo_frame = ttk.LabelFrame(root, text="To-Do List")
todo_frame.pack(fill="x", padx=10, pady=5)
task_input = ttk.Entry(todo_frame, width=40)
task_input.pack(side="left", padx=5)
ttk.Button(todo_frame, text="Tambah", command=add_task).pack(side="left", padx=5)
ttk.Button(todo_frame, text="Tandai Selesai", command=mark_done).pack(side="left", padx=5)
ttk.Button(todo_frame, text="Hapus Semua", command=clear_tasks).pack(side="left", padx=5)
task_listbox = tk.Listbox(todo_frame, height=10)
task_listbox.pack(fill="x", padx=5, pady=5)

# Bagian Kalkulator
calculator_frame = ttk.LabelFrame(root, text="Kalkulator Sederhana")
calculator_frame.pack(fill="x", padx=10, pady=5)
calculator_input = ttk.Entry(calculator_frame)
calculator_input.pack(side="left", fill="x", expand=True, padx=5)
ttk.Button(calculator_frame, text="Hitung", command=calculate).pack(side="left", padx=5)
calculator_result_label = ttk.Label(calculator_frame, text="Hasil: ")
calculator_result_label.pack(side="left", padx=5)

# Bagian Penghasil Kutipan Motivasi
quote_frame = ttk.LabelFrame(root, text="Penghasil Kutipan Motivasi")
quote_frame.pack(fill="x", padx=10, pady=5)
quote_label = ttk.Label(quote_frame, text="", wraplength=500, justify="center")
quote_label.pack(fill="x", padx=5, pady=5)
ttk.Button(quote_frame, text="Buat Kutipan", command=generate_quote).pack(pady=5)

# Menjalankan aplikasi
root.mainloop()