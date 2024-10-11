import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.core.window import Window


class CounterApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.counter = 0
        self.history_count = 0
        self.multiplier = 1
        self.score = 0
        self.clicks_on_label = 0
        self.cheat_used = False

        # Criação do label para a pontuação discreta
        self.score_label = Label(text='Pontuação: 0', font_size='20sp', size_hint=(None, None), size=(100, 50))
        self.score_label.pos_hint = {'x': 0, 'top': 1}

        self.label = Label(text=f'Contador: {self.counter}', font_size='40sp')
        self.history_label = Label(text=f'Histórico de Cliques: {self.history_count}', font_size='20sp')
        self.level_label = Label(text='Nível: 1', font_size='30sp')
        self.multiplier_label = Label(text='Multiplicador: x1', font_size='30sp')

        # Barra de XP com rótulo para exibir mensagens
        self.xp_bar = ProgressBar(max=100, value=100)
        self.xp_label = Label(text='', font_size='18sp', color=(1, 0, 0, 1))  # Melhor aparência na fonte e cor

        self.paragon_button = Button(text='Ganhar Multiplicador', font_size='30sp')

        # Label para exibir a mensagem do bônus
        self.bonus_label = Label(text='', font_size='20sp', color=(0, 1, 0, 1))  # Verde para destacar o bônus

        self.add_widget(self.score_label)
        self.add_widget(self.label)
        self.add_widget(self.history_label)
        self.add_widget(self.level_label)
        self.add_widget(self.multiplier_label)
        self.add_widget(self.xp_bar)
        self.add_widget(self.xp_label)  # Adiciona o label da mensagem junto com a barra de XP
        self.add_widget(self.bonus_label)  # Adiciona o label do bônus
        self.add_widget(self.paragon_button)

        self.button = Button(text='Clique aqui', font_size='40sp')
        self.button.bind(on_press=self.increment_counter)
        self.add_widget(self.button)

        self.reset_button = Button(text='Resetar Progresso', font_size='40sp')
        self.reset_button.bind(on_press=self.reset_counter)
        self.add_widget(self.reset_button)

        self.label.bind(on_touch_down=self.on_counter_click)
        self.paragon_button.bind(on_press=self.gain_multiplier)

    def increment_counter(self, instance):
        self.counter += self.multiplier
        self.history_count += 1
        self.label.text = f'Contador: {self.counter}'
        self.history_label.text = f'Histórico de Cliques: {self.history_count}'
        self.update_score()
        self.update_level()

        self.button.background_color = [random.random() for _ in range(3)] + [1]

    def update_score(self):
        self.score += self.multiplier
        self.score_label.text = f'Pontuação: {self.score}'

    def update_level(self):
        if self.counter < 50:
            level = 1
            xp_needed = 50
        elif self.counter < 100:
            level = 2
            xp_needed = 100
        elif self.counter < 200:
            level = 3
            xp_needed = 200
        else:
            level = 4
            xp_needed = 200  # Nível máximo

        self.level_label.text = f'Nível: {level}'

        if level < 4:
            xp_current = 100 - (self.counter / xp_needed * 100)
            self.xp_bar.value = xp_current
        else:
            self.xp_bar.value = 0

    def gain_multiplier(self, instance):
        if self.counter >= 200:
            self.multiplier += 1
            self.multiplier_label.text = f'Multiplicador: x{self.multiplier}'
            self.counter = 0
            self.label.text = f'Contador: {self.counter}'
            self.level_label.text = 'Nível: 1'
            self.xp_bar.value = 100
            self.xp_label.text = ''  # Limpa a mensagem quando ganha o multiplicador
        else:
            self.xp_label.text = 'Você precisa estar no nível máximo para ganhar um multiplicador!'
            self.xp_bar.value = 100

    def reset_counter(self, instance):
        self.counter = 0
        self.score = 0
        self.label.text = f'Contador: {self.counter}'
        self.score_label.text = f'Pontuação: {self.score}'
        self.level_label.text = 'Nível: 1'
        self.xp_bar.value = 100
        self.multiplier = 1
        self.multiplier_label.text = 'Multiplicador: x1'
        self.xp_label.text = ''  # Limpa a mensagem ao resetar
        self.bonus_label.text = ''  # Reseta a mensagem de bônus também

    def on_counter_click(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.clicks_on_label += 1
            if self.clicks_on_label == 10 and not self.cheat_used:
                self.multiplier += 5
                self.multiplier_label.text = f'Multiplicador: x{self.multiplier}'
                self.cheat_used = True
                self.bonus_label.text = 'Bônus de 5x multiplicador concedido!'  # Mensagem do bônus


class MyApp(App):
    def build(self):
        return CounterApp()


if __name__ == '__main__':
    MyApp().run()
