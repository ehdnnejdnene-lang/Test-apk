from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class PixelForgeTest(App):
    def build(self):
        self.count = 0
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Привет, Pixel Forge!", font_size='20sp')
        self.btn = Button(text="Нажми меня!", size_hint=(1, 0.5))
        self.btn.bind(on_press=self.on_button_press)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.btn)
        return self.layout

    def on_button_press(self, instance):
        self.count += 1
        self.label.text = f"Кликнул {self.count} раз!"

if __name__ == '__main__':
    PixelForgeTest().run()
