import os
import re
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Color
from kivy.core.window import Window
from kivy.uix.image import Image
from docx import Document

class ChatbotApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        title_label =Label(text="Chatbot", font_size=40, size_hint=(1, 0.1), bold=True, color=(1, 0, 0, 1))
        self.text_output = TextInput(readonly=True, size_hint=(1, 0.6), font_size=18, background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))
        self.text_input = TextInput(size_hint=(1, 0.2), multiline=False, font_size=18)
        button = Button(text='Extraer información', on_press=self.extract_information, size_hint=(1, 0.1), font_size=20)
        button.background_color = (1, 0, 0, 1)
        button.color = (1, 1, 1, 1)

        # Establecer el color de fondo de la ventana a blanco
        Window.clearcolor = (1, 1, 1, 1)

        # Cambiar el color del botón a rojo
        with button.canvas.before:
            Color(1, 0, 0, 1)  # Valor RGBA de rojo

        layout.add_widget(title_label)
        layout.add_widget(self.text_output)
        layout.add_widget(self.text_input)
        layout.add_widget(button)

        return layout

    def extract_information(self, instance):
        palabra_clave = self.text_input.text.strip().upper()
        resultado = extraer_informacion(palabra_clave)
        self.text_output.text = resultado

def extraer_informacion(palabra_clave):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    document_path = os.path.join(script_dir, "nuevo.docx")
    if os.path.exists(document_path):
        document = Document(document_path)
        respuesta = ""
        for paragraph in document.paragraphs:
            if re.search(r"\b{}\b".format(re.escape(palabra_clave)), paragraph.text, re.IGNORECASE):
                respuesta += paragraph.text + "\n"
        if respuesta:
            return respuesta
        else:
            return f"No se encontró información relacionada con '{palabra_clave}'."
    else:
        return "No se encontró el archivo 'nuevo.docx'."

if __name__ == '__main__':
    ChatbotApp().run()