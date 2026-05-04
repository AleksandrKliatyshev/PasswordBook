import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from storage import YandexStorage
from models import Card
from card_widget import CardWidget


class PasswordBookApp:
    def __init__(self, storage):
        self.storage = storage
        self.cards = []
        self.root = tk.Tk()
        self.root.title("PasswordBook")
        self.root.geometry("900x650")
        self.root.configure(bg="white")
        self.setup_menu()          # сначала меню
        self.setup_scrollable_area()  # потом скролл
        #self.canvas.bind("<Configure>", lambda e: self.show_cards())
        #self.root.bind("<Configure>", lambda e: self.root.after(100, self.show_cards))
        self.load_data()
        self.show_cards()
        self.root.mainloop()

    def setup_scrollable_area(self):
        self.canvas = tk.Canvas(self.root, bg="white")
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="white")
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def setup_menu(self):
        menu_frame = tk.Frame(self.root, bg="lightgray", height=50)
        menu_frame.pack(fill="x", pady=(0, 10), side="top")  # явно вверх
        menu_frame.pack_propagate(False)
        
        tk.Button(menu_frame, text="Создать", bg="green", fg="white", command=self.open_create_window).pack(side="left", padx=10, pady=10)
        tk.Button(menu_frame, text="Удалить", bg="red", fg="white").pack(side="left", padx=10, pady=10)
        
        self.search_entry = tk.Entry(menu_frame, width=30)
        self.search_entry.pack(side="right", padx=10, pady=10)
        self.search_entry.insert(0, "Поиск...")
        
        # Переносим canvas/scroller ниже
        # self.canvas.pack_forget()
        # self.scrollbar.pack_forget()
        # self.canvas.pack(side="left", fill="both", expand=True)
        # self.scrollbar.pack(side="right", fill="y")

    def load_data(self):
        self.storage.download()
        self.cards = self.storage.load_cards()

    def save_and_sync(self):
        self.storage.save_cards(self.cards)

    def open_create_window(self):
        win = tk.Toplevel(self.root)
        win.title("Новая карточка")
        win.geometry("350x450")
        win.configure(bg="lightgray")
        fields = {}
        labels = [
            ("Название сайта:", "website_name"),
            ("URL сайта:", "website_url"),
            ("Имя логина (метка):", "login_name"),
            ("Логин:", "login"),
            ("Пароль:", "password")
        ]
        for label_text, key in labels:
            tk.Label(win, text=label_text, bg="lightgray").pack(pady=2)
            entry = tk.Entry(win, width=40, show="*" if key == "password" else "")
            entry.pack(pady=2)
            fields[key] = entry
        tk.Label(win, text="Комментарий (склор):", bg="lightgray").pack(pady=2)
        comment_text = scrolledtext.ScrolledText(win, width=40, height=5)
        comment_text.pack(pady=5)

        def save():
            new_card = Card(
                website_name=fields["website_name"].get().strip(),
                website_url=fields["website_url"].get().strip(),
                login_name=fields["login_name"].get().strip(),
                login=fields["login"].get().strip(),
                password=fields["password"].get().strip(),
                comment=comment_text.get("1.0", tk.END).strip()
            )
            if not new_card.website_name or not new_card.login or not new_card.password:
                messagebox.showerror("Ошибка", "Заполните название, логин и пароль")
                return
            self.cards.append(new_card)
            self.save_and_sync()
            win.destroy()
            self.show_cards()

        tk.Button(win, text="Сохранить", bg="green", fg="white", command=save).pack(pady=20)

    def show_cards(self):
        def show_cards(self):
         for widget in self.scrollable_frame.winfo_children():
          widget.destroy()
    
        row = tk.Frame(self.scrollable_frame, bg="white")
        row.pack(fill="x", pady=10)
    
        for i, card_data in enumerate(self.cards):  # card_data определен здесь
            if i > 0 and i % 2 == 0:
                row = tk.Frame(self.scrollable_frame, bg="white")
                row.pack(fill="x", pady=10)
            
            card_frame = CardWidget(row, card_data)  # row и card_data существуют
            card_frame.pack(side="left", padx=10, expand=True)