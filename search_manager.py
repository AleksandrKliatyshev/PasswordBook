from nicegui import ui

class SearchBar:
    def __init__(self, cards, refresh_callback):
        self.cards = cards
        self.refresh_callback = refresh_callback
        self.query = ''
        self.input = ui.input('Поиск...').props('outlined dense').classes('w-64')
        self.input.on('keyup', self.on_search)
    
    def on_search(self):
        self.query = self.input.value.lower()
        self.refresh_callback()
    
    def get_filtered_cards(self):
        if not self.query:
            return self.cards
        return [card for card in self.cards 
                if self.query in card.website_name.lower() 
                or self.query in card.login.lower()]