import tkinter as tk

class CardWidget(tk.Frame):
    def __init__(self, parent, card_data, **kwargs):
        super().__init__(parent, relief="solid", borderwidth=1, bg="lightgray", width=280, height=350, **kwargs)
        self.pack_propagate(False)
        self.card_data = card_data
        self.build()

    def build(self):
        tk.Label(self, text=self.card_data.website_name, font=("Arial", 14, "bold"), bg="lightgray", wraplength=250).pack(anchor="center", padx=10, pady=(10, 5))
        tk.Frame(self, height=2, bg="gray").pack(fill="x", padx=10, pady=5)
        
        inner = tk.Frame(self, bg="lightgray")
        inner.pack(expand=True, fill="both", padx=10, pady=5)
        
        tk.Label(inner, text=f"URL: {self.card_data.website_url or '—'}", font=("Arial", 10), bg="lightgray", wraplength=250, justify="left").pack(anchor="w", pady=2)
        if self.card_data.login_name:
            tk.Label(inner, text=f"Метка: {self.card_data.login_name}", font=("Arial", 10), bg="lightgray", wraplength=250, justify="left").pack(anchor="w", pady=2)
        tk.Label(inner, text=f"Логин: {self.card_data.login}", font=("Arial", 10), bg="lightgray", wraplength=250, justify="left").pack(anchor="w", pady=2)
        tk.Label(inner, text=f"Пароль: {self.card_data.password}", font=("Arial", 10), bg="lightgray", wraplength=250, justify="left").pack(anchor="w", pady=2)
        if self.card_data.comment:
            tk.Label(inner, text=f"Склор: {self.card_data.comment}", font=("Arial", 10), bg="lightgray", wraplength=250, justify="left").pack(anchor="w", pady=2)