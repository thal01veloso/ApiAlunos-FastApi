from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton

from servico import mostarAlunos

class Aplicativo(MDApp):
    def build(self):
        self.layout = MDBoxLayout()
        self.btn = MDFlatButton(text="Sou um botão")
        self.btn.bind(on_press=mostarAlunos)

        self.layout.add_widget(self.btn)
        return self.layout
    


if __name__=="__main__":
    Aplicativo().run()