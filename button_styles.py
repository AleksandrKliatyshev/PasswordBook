from nicegui import ui

BUTTON_STYLES = {
    'create': {'label': 'Создать', 'class': 'bg-[#10b981] hover:bg-[#059669]'},
    'delete': {'label': 'Удалить', 'class': 'bg-[#ef4444] hover:bg-[#dc2626]'},
    'go': {'label': 'Перейти', 'class': 'bg-[#3b82f6] hover:bg-[#2563eb]'},
    'save': {'label': 'Сохранить', 'class': 'bg-[#10b981] hover:bg-[#059669]'},
}

class ButtonStyles:
    @staticmethod
    def make(button_type, on_click):
        style = BUTTON_STYLES[button_type]
        return ui.button(style['label'], on_click=on_click).props('flat').classes(f'{style["class"]} text-white px-4 py-2 rounded-md')