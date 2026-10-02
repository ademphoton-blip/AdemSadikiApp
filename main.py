from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class AdemSadikiApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        label = Label(text='مرحباً بك في لعبتي/تطبيقي!', font_size=24)
        button = Button(text='اضغط هنا', font_size=20)
        
        def on_press_button(instance):
            label.text = 'تم ضغط الزر بنجاح!'
            
        button.bind(on_press=on_press_button)
        layout.add_widget(label)
        layout.add_widget(button)
        return layout

if __name__ == '__main__':
    AdemSadikiApp().run()
