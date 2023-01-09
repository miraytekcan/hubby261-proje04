import tkinter as tk
import tkinter.messagebox as messagebox

students = []

window = tk.Tk()
window.geometry("525x1796")
window.title("Miray Dönem Sonu Ortalama Hessaplama")
label = tk.Label(window, text="Aşağıdaki alanlara notları girerek öğrencinin dersten geçip geçmediği öğrenilebilir.")
label.pack()
mesaj = tk.Label(window, text="(Girdiğiniz bilgiler ayrıca metin dosyasına kaydedilmektedir.)")
mesaj.pack()

name_label = tk.Label(window, text="Öğrenci Adını Sarı Alana Giriniz:")
name_label.pack()
name_entry = tk.Entry(window, bg = "#F1F67A", fg = "black", font=("Arial", 20), width=27)
name_entry.pack()

course_label = tk.Label(window, text="Ders seçimini buradan yapabilirsiniz:")
course_label.pack()
courses = ["Türkçe", "Matematik", "Müzik", "Tarih", "İngilizce", "Psikoloji", "Ekonomi",
           "Business", "Fransızca", "Beden Eğitimi", "Coğrafya", "Almanca",
           "Computer Science", "Fizik", "Kimya", "Biyoloji", "Mekanik", "İstatistik"]
course_var = tk.StringVar(window)
course_var.set("Dersler")
course_dropdown = tk.OptionMenu(window, course_var, *courses)
course_dropdown.pack()

course_label = tk.Label(window, text="Ders Adı:")
course_label.pack()
course_entry = tk.Entry(window, bg = "#e19d9e", fg = "black", font=("Arial", 20), width=27)
course_entry.pack()

def set_course(*args):
    course_entry.delete(0, tk.END)
    course_entry.insert(0, course_var.get())
course_var.trace("w", set_course)

midterm_label = tk.Label(window, text="Arasınavın Ağırlığını Seçip Puanı Yeşil Alana Giriniz:")
midterm_label.pack()
midterm_weights = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%"]
midterm_weight_var = tk.StringVar(window)
midterm_weight_var.set("Ağırlık")
midterm_weight_dropdown = tk.OptionMenu(window, midterm_weight_var, *midterm_weights)
midterm_weight_dropdown.pack()
midterm_entry = tk.Entry(window, bg = "#c0e19d", fg = "black", font=("Arial", 20), width=27)
midterm_entry.pack()

final_label = tk.Label(window, text="Finalin Ağırlığını Seçip Puanı Mavi Alana Giriniz:")
final_label.pack()
final_weights = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%"]
final_weight_var = tk.StringVar(window)
final_weight_var.set("Ağırlık")
final_weight_dropdown = tk.OptionMenu(window, final_weight_var, *final_weights)
final_weight_dropdown.pack()
final_entry = tk.Entry(window, bg = "#9de1e0", fg = "black", font=("Arial", 20), width=27)
final_entry.pack()

homework_label = tk.Label(window, text="Ödev Notunun Ağırlığını Seçip Puanı Mor Alana Giriniz:")
homework_label.pack()
homework_weights = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%"]
homework_weight_var = tk.StringVar(window)
homework_weight_var.set("Ağırlık")
homework_weight_dropdown = tk.OptionMenu(window, homework_weight_var, *homework_weights)
homework_weight_dropdown.pack()
homework_entry = tk.Entry(window, bg = "#be9de1", fg = "black", font=("Arial", 20), width=27)
homework_entry.pack()

result_label = tk.Label(window, text="Dersin Not Ortalaması:")
result_label.pack()
label = tk.Label(window, text="(Geçti)", fg="green")
label1 = tk.Label(window, text="(Kaldı)", fg="red")
label.pack()
label1.pack()

def add_student():
    try:
        name = name_entry.get()
        course = course_entry.get()
        midterm = int(midterm_entry.get())
        final = int(final_entry.get())
        homework = int(homework_entry.get())
    except ValueError:
        show_warning()
        return
    global midterm_weight
    global final_weight
    global homework_weight
    midterm_weight = float(midterm_weight_var.get().strip("%")) / 100
    final_weight = float(final_weight_var.get().strip("%")) / 100
    homework_weight = float(homework_weight_var.get().strip("%")) / 100
    students.append({"name": name, "course": course, "midterm": midterm, "final": final, "homework": homework})
    average = (midterm * midterm_weight) + (final * final_weight) + (homework * homework_weight)
    result_label.config(text=f"Not Ortalaması: {average:.2f}")
    if average >= 50:
        result_label.config(fg="green")
    else:
        result_label.config(fg="red")
    with open("dersNotlar.txt", "a") as file:
        file.write("Öğrenci: " + name + ", ")
        file.write("Ders: " + course + ", ")
        file.write("Arasınav: " + str(midterm) + ", ")
        file.write("Final: " + str(final) + ", ")
        file.write("Ödev: " + str(homework) + ", ")
        file.write("Ortalama: " + str(average) + "\n")
    global isim
    isim = tk.Label(window, text="Öğrenci: " + name)
    isim.pack()
    global ders
    ders = tk.Label(window, text="Ders: "+ course)
    ders.pack()
    global arasinav
    arasinav = tk.Label(window, text="Arasınav Notu: "+ str(midterm))
    arasinav.pack()
    global finalsinav
    finalsinav = tk.Label(window,  text="Final Notu: "+ str(final))
    finalsinav.pack()
    global odev
    odev = tk.Label(window, text="Ödev Notu: "+ str(homework))
    odev.pack()

def clear_entries():
    name_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    midterm_entry.delete(0, tk.END)
    final_entry.delete(0, tk.END)
    homework_entry.delete(0, tk.END)
    isim.pack_forget()
    ders.pack_forget()
    arasinav.pack_forget()
    finalsinav.pack_forget()
    odev.pack_forget()

def quit_app():
    result = messagebox.askyesno("Çıkış", "Çıkış yapmak istediğinizden emin misiniz?")
    if result:
        window.destroy()

def show_warning():
    messagebox.showwarning("Uyarı!", "Lütfen verileri tekrar giriniz")

def delete_last_record():
    with open("dersNotlar.txt", "r") as file:
        lines = file.readlines()
    with open("dersNotlar.txt", "w") as file:
        for line in lines[:-1]:
            file.write(line)

add_button = tk.Button(window, text="Dönem Sonu Ortalamasını Hesapla", command=add_student)
add_button.pack()

clear_button = tk.Button(window, text="Yeni Hesaplama Yapmadan Önce Sonuçları Temizle", command=clear_entries)
clear_button.pack()

delete_button = tk.Button(window, text="Son Kaydı Dosyadan Sil", command=delete_last_record)
delete_button.pack()

quit_button = tk.Button(window, text="Çıkış Yap", command=quit_app)
quit_button.pack()

window.mainloop()