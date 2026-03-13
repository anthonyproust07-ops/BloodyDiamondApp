from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class BloodyDiamondApp(App):
    def build(self):
        self.balance = 103.0
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.label = Label(text=f"💎 SOLDE : {self.balance} €", font_size='30sp')
        btn = Button(text="RECOLTER GAINS", size_hint=(1, 0.2), background_color=(0, 0.7, 0.9, 1))
        btn.bind(on_press=self.add_gain)
        
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def add_gain(self, instance):
        self.balance += 0.50
        self.label.text = f"💎 SOLDE : {round(self.balance, 2)} €"

if __name__ == "__main__":
    BloodyDiamondApp().run()
