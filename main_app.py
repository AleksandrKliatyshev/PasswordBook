from nicegui import ui
from storage import YandexStorage
from models import Card
from dialog_manager import CreateCardDialog
from card_component import CardComponent
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
def show_cards():
    with ui.element('div').classes('flex flex-wrap gap-4 p-4'):
        for card in cards:
         CardComponent(card, cards, storage, show_cards.refresh).render()

ui.label('PasswordBook').classes('text-3xl font-bold m-4')
with ui.row().classes('w-full justify-between p-4'):
    create_dialog = CreateCardDialog(cards, storage, show_cards.refresh)
    ui.button('Создать', on_click=create_dialog.open, color='green')
    ui.input('Поиск...').props('outlined dense').classes('w-64')

show_cards()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(host='0.0.0.0', port=8080, reload=False)