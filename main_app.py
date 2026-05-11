from nicegui import ui
from storage import YandexStorage
from models import Card
from dialog_manager import CreateCardDialog
from card_component import CardComponent
from search_manager import SearchBar
from button_styles import ButtonStyles
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
    filtered_cards = search_bar.get_filtered_cards() if search_bar else cards
    with ui.element('div').classes('flex flex-wrap gap-4 p-4'):
        for card in filtered_cards:
            CardComponent(card, cards, storage, show_cards.refresh).render()

ui.label('Книга паролей').classes('text-3xl font-bold m-4')
ui.separator()
with ui.row().classes('w-full justify-between items-center p-4'):
    create_dialog = CreateCardDialog(cards, storage, show_cards.refresh)
    ButtonStyles.make('create', create_dialog.open)
    search_bar = SearchBar(cards, show_cards.refresh)

show_cards()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(host='0.0.0.0', port=8080, reload=False)