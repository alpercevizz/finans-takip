import sqlite3
import tkinter as tk
from tkinter import messagebox

# Veritabanına bağlan
conn = sqlite3.connect("PYTHON/finans-takip/finans.db")
cursor = conn.cursor()

# Tkinter ana pencereyi oluştur
root = tk.Tk()
root.title("Finans Takip Uygulaması")
root.geometry("500x500")

# Gelir Ekleme Fonksiyonu
def gelir_ekle():
    tutar = entry_gelir_tutar.get()
    aciklama = entry_gelir_aciklama.get()
    
    if not tutar:
        messagebox.showerror("Hata", "Lütfen bir tutar girin!")
        return

    try:
        tutar = float(tutar)
        cursor.execute("INSERT INTO gelir (tarih, tutar, aciklama) VALUES (datetime('now'), ?, ?)", (tutar, aciklama))
        conn.commit()
        messagebox.showinfo("Başarılı", "Gelir başarıyla eklendi!")
        entry_gelir_tutar.delete(0, tk.END)
        entry_gelir_aciklama.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Hata", "Geçerli bir sayı girin!")

# Gider Ekleme Fonksiyonu
def gider_ekle():
    tutar = entry_gider_tutar.get()
    aciklama = entry_gider_aciklama.get()
    kategori = entry_gider_kategori.get()
    
    if not tutar:
        messagebox.showerror("Hata", "Lütfen bir tutar girin!")
        return

    try:
        tutar = float(tutar)
        cursor.execute("INSERT INTO gider (tarih, tutar, aciklama, kategori) VALUES (datetime('now'), ?, ?, ?)", (tutar, aciklama, kategori))
        conn.commit()
        messagebox.showinfo("Başarılı", "Gider başarıyla eklendi!")
        entry_gider_tutar.delete(0, tk.END)
        entry_gider_aciklama.delete(0, tk.END)
        entry_gider_kategori.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Hata", "Geçerli bir sayı girin!")

def gelirleri_listele():
    cursor.execute("SELECT * FROM gelir")
    gelirler = cursor.fetchall()
    
    text_gelirler.delete("1.0", tk.END)  # Önceki verileri temizle
    text_gelirler.insert(tk.END, "GELİR LİSTESİ\n\n")
    
    for gelir in gelirler:
        text_gelirler.insert(tk.END, f"{gelir[1]} - {gelir[2]} TL ({gelir[3]})\n")

def giderleri_listele():
    cursor.execute("SELECT * FROM gider")
    giderler = cursor.fetchall()
    
    text_giderler.delete("1.0", tk.END)  # Önceki verileri temizle
    text_giderler.insert(tk.END, "GİDER LİSTESİ\n\n")
    
    for gider in giderler:
        text_giderler.insert(tk.END, f"{gider[1]} - {gider[2]} TL ({gider[3]} - {gider[4]})\n")

def toplam_butce():
    cursor.execute("SELECT SUM(tutar) FROM gelir")
    toplam_gelir = cursor.fetchone()[0] or 0
    
    cursor.execute("SELECT SUM(tutar) FROM gider")
    toplam_gider = cursor.fetchone()[0] or 0

    butce = toplam_gelir - toplam_gider
    label_butce.config(text=f"Mevcut Bütçe: {butce} TL")

def gelirleri_listele():
    cursor.execute("SELECT * FROM gelir")
    gelirler = cursor.fetchall()
    
    text_gelirler.delete("1.0", tk.END)  # Önceki verileri temizle
    text_gelirler.insert(tk.END, "GELİR LİSTESİ\n\n")
    
    for gelir in gelirler:
        text_gelirler.insert(tk.END, f"{gelir[1]} - {gelir[2]} TL ({gelir[3]})\n")

def giderleri_listele():
    cursor.execute("SELECT * FROM gider")
    giderler = cursor.fetchall()
    
    text_giderler.delete("1.0", tk.END)  # Önceki verileri temizle
    text_giderler.insert(tk.END, "GİDER LİSTESİ\n\n")
    
    for gider in giderler:
        text_giderler.insert(tk.END, f"{gider[1]} - {gider[2]} TL ({gider[3]} - {gider[4]})\n")

def toplam_butce():
    cursor.execute("SELECT SUM(tutar) FROM gelir")
    toplam_gelir = cursor.fetchone()[0] or 0
    
    cursor.execute("SELECT SUM(tutar) FROM gider")
    toplam_gider = cursor.fetchone()[0] or 0

    butce = toplam_gelir - toplam_gider
    label_butce.config(text=f"Mevcut Bütçe: {butce} TL")


# Gelir Ekleme Arayüzü
tk.Label(root, text="Gelir Ekle", font=("Arial", 12, "bold")).pack(pady=5)
tk.Label(root, text="Tutar:").pack()
entry_gelir_tutar = tk.Entry(root)
entry_gelir_tutar.pack()
tk.Label(root, text="Açıklama:").pack()
entry_gelir_aciklama = tk.Entry(root)
entry_gelir_aciklama.pack()
tk.Button(root, text="Gelir Ekle", command=gelir_ekle).pack(pady=5)

# Gider Ekleme Arayüzü
tk.Label(root, text="Gider Ekle", font=("Arial", 12, "bold")).pack(pady=5)
tk.Label(root, text="Tutar:").pack()
entry_gider_tutar = tk.Entry(root)
entry_gider_tutar.pack()
tk.Label(root, text="Açıklama:").pack()
entry_gider_aciklama = tk.Entry(root)
entry_gider_aciklama.pack()
tk.Label(root, text="Kategori:").pack()
entry_gider_kategori = tk.Entry(root)
entry_gider_kategori.pack()
tk.Button(root, text="Gider Ekle", command=gider_ekle).pack(pady=5)

# GELİR LİSTESİ
tk.Label(root, text="Gelir Listesi", font=("Arial", 12, "bold")).pack(pady=5)
text_gelirler = tk.Text(root, height=5, width=50)
text_gelirler.pack()
tk.Button(root, text="Gelirleri Listele", command=gelirleri_listele).pack(pady=5)

# GİDER LİSTESİ
tk.Label(root, text="Gider Listesi", font=("Arial", 12, "bold")).pack(pady=5)
text_giderler = tk.Text(root, height=5, width=50)
text_giderler.pack()
tk.Button(root, text="Giderleri Listele", command=giderleri_listele).pack(pady=5)

# BÜTÇEYİ GÖSTERME
label_butce = tk.Label(root, text="💰 Mevcut Bütçe: -- TL", font=("Arial", 12, "bold"))
label_butce.pack(pady=10)
tk.Button(root, text="Bütçeyi Güncelle", command=toplam_butce).pack(pady=5)


# Tkinter ana döngüyü başlat
root.mainloop()
