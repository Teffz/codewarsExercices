from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class LoveApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=40)
        
        self.result_label = Label(text="O quanto eu te amo?")
        layout.add_widget(self.result_label)
        

        
        no_button = Button(text="Quase nada")
        no_button.bind(on_release=self.remove_no_option)
        layout.add_widget(no_button)
        
        noo_button = Button(text="Normal")
        noo_button.bind(on_release=self.remove_noo_option)
        layout.add_widget(noo_button)
        
        yes_button = Button(text="Muito muito muito, mais do que você pode imaginar!")
        yes_button.bind(on_release=self.propose)
        layout.add_widget(yes_button)

        nooo_button = Button(text="Só um pouquinho")
        nooo_button.bind(on_release=self.remove_nooo_option)
        layout.add_widget(nooo_button)
        
        noooo_button = Button(text="Muito?")
        noooo_button.bind(on_release=self.remove_noooo_option)
        layout.add_widget(noooo_button)
        
        return layout
    
    def remove_no_option(self, instance):
        instance.parent.remove_widget(instance)
        Button(text=("Errou"))
        
    def remove_noo_option(self, instance):
        instance.parent.remove_widget(instance)
        Button(text=("Errou"))
        
    def remove_nooo_option(self, instance):
        instance.parent.remove_widget(instance)
        Button(text=("Errou"))
        
    def remove_noooo_option(self, instance):
        instance.parent.remove_widget(instance)
        Button(text=("Errou")) 
        
    def propose(self, instance):
        self.result_label.text = "Parabéns! Você acertou, Eu te amo muito meu amor <3"

if __name__ == '__main__':
    LoveApp().run()
