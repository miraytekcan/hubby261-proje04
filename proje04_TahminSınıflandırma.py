import tkinter as tk
import tkinter.messagebox as messagebox
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

paragraphs = []

with open("paragraphs.txt") as file:
    lines = file.readlines()
    for line in lines:
        paragraph, label = line.strip().split(",")
        paragraphs.append((paragraph, label))

X = [paragraph[0] for paragraph in paragraphs]
y = [paragraph[1] for paragraph in paragraphs]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X, y)

window = tk.Tk()
window.title("Miray Metin Kategorizasyonu")
label = tk.Label(window, text="Lütfen istediğiniz cümleyi yeşil bölgeye giriniz.")
label.pack()

paragraph_input = tk.StringVar()
paragraph_entry = tk.Entry(window, textvariable=paragraph_input, width=50, font=("Arial", 20), bg="green", fg="white")
paragraph_entry.pack()

def predict_paragraph():
    new_paragraph = paragraph_input.get()
    new_X = vectorizer.transform([new_paragraph])
    prediction = model.predict(new_X)[0]
    probability = model.predict_proba(new_X)[0][1]
    result_text.set(f"Tahmin edilen konu: {prediction}\nTahmin olasılığı: {probability:.2f}")

def clear_output():
    result_text.set("")
    paragraph_entry.delete(0, tk.END)

def quit_app():
    result = messagebox.askyesno("Çıkış", "Çıkış yapmak istediğinizden emin misiniz?")
    if result:
        window.destroy()

predict_button = tk.Button(window, text="Tahmin Et", command=predict_paragraph)
predict_button.pack()

result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text)
result_label.pack()

clear_button = tk.Button(window, text="Çıktıları Temizle", command=clear_output)
clear_button.pack()

exit_button = tk.Button(window, text="Çıkış", command=quit_app)
exit_button.pack()

window.mainloop()
