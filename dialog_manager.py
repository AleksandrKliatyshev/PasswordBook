# В отдельном файле dialog_manager.py
from nicegui import ui
from models import Card

class CreateCardDialog:
    def __init__(self, cards, storage, refresh_callback):
        self.cards = cards
        self.storage = storage
        self.refresh_callback = refresh_callback

    def open(self):
        with ui.dialog() as dialog, ui.card():
            ui.label('Новая карточка').classes('text-lg font-bold')
            website_name = ui.input('Название сайта')
            website_url = ui.input('URL сайта')
            login_name = ui.input('Имя логина (метка)')
            login = ui.input('Логин')
            password = ui.input('Пароль', password=True, password_toggle_button=True)
            comment = ui.textarea('Комментарий (склор)')

            def save():
                url = website_url.value.strip()
                import re
                if re.search(r'[^a-zA-Zа-яА-Я0-9\-\.]', url):
                    website_url.props('color=red')
                    ui.notify('Измените поле URL сайта.Он может содержать только английские буквы, цифры, дефис и точку', type='negative')
                    return
                if url and not url.startswith(('http://', 'https://')):
                    url = 'https://' + url
                
                new_card = Card(
                    website_name=website_name.value.strip(),
                    website_url=url,
                    login_name=login_name.value.strip(),
                    login=login.value.strip(),
                    password=password.value.strip(),
                    comment=comment.value.strip()
                )
                self.cards.append(new_card)
                self.storage.save_cards(self.cards)
                self.refresh_callback()
                dialog.close()

            ui.button('Сохранить', on_click=save, color='green')
        dialog.open()