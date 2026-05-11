from nicegui import ui

class CardComponent:
    def __init__(self, card_data, cards_list, storage, refresh_callback):
        self.card_data = card_data
        self.cards_list = cards_list
        self.storage = storage
        self.refresh_callback = refresh_callback
    
    def render(self):
        with ui.card().classes('w-[200px] h-[300px] flex flex-col bg-gray-100'):
            ui.label(self.card_data.website_name).classes('text-lg font-bold text-center truncate')
            ui.separator()
            with ui.element('div').classes('flex-1'):
                ui.label(f'URL: {self.card_data.website_url or "—"}').classes('break-words')
                if self.card_data.login_name:
                    ui.label(f'Метка: {self.card_data.login_name}').classes('break-words')
                ui.label(f'Логин: {self.card_data.login}').classes('break-words')
                ui.label(f'Пароль: {self.card_data.password}').classes('break-words')
                if self.card_data.comment:
                    ui.label(f'Склор: {self.card_data.comment}').classes('break-words')
            
                with ui.column().classes('items-center gap-1 p-1'):
                    with ui.row().classes('justify-center gap-2'):
                        ui.button('Удалить', on_click=self.delete_card, color='red').props('flat').classes('text-xs w-[60px]')
                        url = self.card_data.website_url
                        if url and not url.startswith(('http://', 'https://')):
                            url = 'https://' + url
                        ui.button('Перейти', on_click=lambda: ui.navigate.to(f'{self.card_data.website_url}', new_tab=True), color='blue').props('flat').classes('text-xs w-[60px]')

    def delete_card(self):
        def confirm_delete(confirm_dialog):
            confirm_dialog.close()
            if self.card_data in self.cards_list:
                self.cards_list.remove(self.card_data)
                self.storage.save_cards(self.cards_list)
                self.refresh_callback()
        
        with ui.dialog() as dialog, ui.card():
            ui.label('Подтверждение').classes('text-lg font-bold')
            ui.label(f'Удалить карточку "{self.card_data.website_name}"?')
            with ui.row().classes('justify-end gap-2'):
                ui.button('Нет', on_click=dialog.close)
                ui.button('Да', on_click=lambda: confirm_delete(dialog), color='red')
        dialog.open()