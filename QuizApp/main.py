import tkinter as tk
from tkinter import messagebox, ttk
from ttkthemes import ThemedStyle # Bilgisayarınızın komut sisteminden pip install ttkthemes yazarak kurmayı unutmayınız

from quiz_data import quiz_data

# Geçerli soruyu görmek için
def show_question():
    # quiz data'dan soruları alıyoruz
    question = quiz_data[current_question]
    gs_label.config(text=question["question"])

    # şıkları buton haline getiriyoruz
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal") 

    # feedback etiketini temizleyip boş bırakıyoruz ve next butonunu devre dışı yapıyoruz
    feedback_label.config(text="")
    next_btn.config(state="disabled")

# İşaretlenen cevabı kontrol etme ve feedback sağlama
def check_answer(choice):
    question = quiz_data[current_question] 
    selected_choice = choice_btns[choice].cget("text")

    # cevabın doğruluğunu kontrol etme
    if selected_choice == question["answer"]:
        # Score güncelleme
        global score # Skoru fonksiyon içerisinde değiştirebilmek için global olarak ayarladık
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))   
        feedback_label.config(text="Correct!", foreground="green")
    else:  
        feedback_label.config(text="False!", foreground="red") 

    # bir şıkkı işaretledikten sonra diğer şıkları devre dışı bırakıyoruz ve next butonunu etkinleştiriyoruz 
    for button in choice_btns:
        button.config(state="disabled")     
    next_btn.config(state="normal")

# Bir sonraki soruya geçme işlemi
def next_question():
    global current_question
    current_question += 1

    if current_question < len(quiz_data):
        # Eğer soru varsa göster
        show_question()
    else:
        # eğer daha fazla soru yoksa bitir ve skoru göster
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data))) 
        root.destroy()   

# açılacak olan ana pencere kısmı
root = tk.Tk()
root.title("Python Quiz App")
root.geometry("600x700")
style = ThemedStyle(theme = "clearlooks")

# Soruların ve şıkların yazı tipi ve boyutu
style.configure("TLabel", font=("Comic Sans MS",20))
style.configure("TButton", font=("Comic Sans MS", 15))

# question kısmının oluşturulması
gs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=300,
    padding=10
)
gs_label.pack(pady=10)

# choice kısmının oluşumu
choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

# feedback kısmının oluşumu
feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

# score başlangıç değeri
score = 0

# score kısmının oluşumu
score_label = ttk.Label(
    root,
    text="Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

#next butonunun oluşumu
next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disable"
)
next_btn.pack(pady=10)

# geçerli soru indeksi 
current_question = 0

# ilk soruyu gösterir
show_question()

# ana döngüyü başlatır
root.mainloop()