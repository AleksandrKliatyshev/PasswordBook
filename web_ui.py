from nicegui import ui
from storage import YandexStorage
from models import Card
import os
from dotenv import load_dotenv

load_dotenv()

storage = YandexStorage(
    token_write=os.getenv("YANDEX_TOKEN_WRITE"),
    token_read=os.getenv("YANDEX_TOKEN_READ")
)

storage.download()
cards = storage.load_cards()

@ui.refreshable
@ui.refreshable
def show_cards():
    with ui.element('div').classes('grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4 p-4'):
        for card in cards:
            with ui.card().classes('w-full h-96 flex flex-col justify-between bg-gray-100'):
                ui.label(card.website_name).classes('text-xl font-bold text-center truncate')
                ui.separator()
                with ui.element('div').classes('overflow-auto'):
                    ui.label(f'URL: {card.website_url or "—"}').classes('break-words')
                    if card.login_name:
                        ui.label(f'Метка: {card.login_name}').classes('break-words')
                    ui.label(f'Логин: {card.login}').classes('break-words')
                    ui.label(f'Пароль: {card.password}').classes('break-words')
                    if card.comment:
                        ui.label(f'Склор: {card.comment}').classes('break-words')

def open_create_dialog():
    with ui.dialog() as dialog, ui.card():
        ui.label('Новая карточка').classes('text-lg font-bold')
        website_name = ui.input('Название сайта')
        website_url = ui.input('URL сайта')
        login_name = ui.input('Имя логина (метка)')
        login = ui.input('Логин')
        password = ui.input('Пароль', password=True, password_toggle_button=True)
        comment = ui.textarea('Комментарий (склор)')
        
        def save():
            new_card = Card(
                website_name=website_name.value,
                website_url=website_url.value,
                login_name=login_name.value,
                login=login.value,
                password=password.value,
                comment=comment.value
            )
            cards.append(new_card)
            storage.save_cards(cards)
            show_cards.refresh()
            dialog.close()
        
        ui.button('Сохранить', on_click=save, color='green')

# Интерфейс
ui.label('PasswordBook').classes('text-3xl font-bold m-4')
with ui.row().classes('w-full justify-between p-4'):
    ui.button('Создать', on_click=open_create_dialog, color='green')
    ui.input('Поиск...').props('outlined dense').classes('w-64')

show_cards()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run()