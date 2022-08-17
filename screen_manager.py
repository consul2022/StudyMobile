from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton, MDFillRoundFlatButton
from kivymd.uix.screen import MDScreen
from kivymd.utils.fitimage import FitImage
from kivymd.uix.button import MDFloatingActionButton
from translator import Translator


class SM(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_one = ScreenOne(manager=self, name="Старт")  # self - экзепляр класса sm
        self.screen_two = ScreenTwo(manager=self, name="Меню")
        self.translator = Translator(manager=self, name="Переводчик")

        self.add_widget(self.screen_one)
        self.add_widget(self.screen_two)
        self.add_widget(self.translator)

    def switch_to_screen_two(self, button=None):
        self.switch_to(screen=self.screen_two, direction='left')

    def switch_to_screen_one(self, button=None):
        self.switch_to(screen=self.screen_one, direction='right')
    def switch_to_translator(self, button=None):
        self.switch_to(screen=self.translator, direction='left')
    def switch_to_menu(self, buttion=None):
        self.switch_to(screen=self.screen_two,direction="right")

class ScreenOne(MDScreen):
    def __init__(self, manager: SM, **kwargs):
        super().__init__(**kwargs)

        start_button = MDFillRoundFlatButton(
            text="Start",
            text_color=[10 / 255, 10 / 255, 10 / 255, 1],
            font_size=30,
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            on_press=manager.switch_to_screen_two,
            md_bg_color=[100 / 255, 220 / 255, 180 / 255, 1]
        )

        back = FitImage(source='1.jpg')
        self.add_widget(back)
        self.add_widget(start_button)


class ScreenTwo(MDScreen):
    def __init__(self, manager, **kw):
        super().__init__(**kw)

        back = FitImage(source='1.jpg')
        self.add_widget(back)

        # self.back_button = MDIconButton(
        #     icon="arrow-left-circle",
        #     user_font_size="64sp",
        #     on_press=manager.switch_to_screen_one
        #
        # )
        # self.add_widget(self.back_button)

        #self.front_button = MDIconButton(
            #icon="arrow-right-circle",
            #user_font_size="64sp",
            #pos_hint={'center_x': 0.15, 'center_y': 0.075},
        #)
        from button_menu import translator, spelling, voice_recorder, digitalization, to_share

        #self.add_widget(self.front_button)

        translator.on_press = manager.switch_to_translator
        self.add_widget(translator)
        self.add_widget(spelling)
        self.add_widget(voice_recorder)
        self.add_widget(digitalization)
        self.add_widget(to_share)


class WindowApp(MDApp):
    def build(self):
        return SM()


window = WindowApp()
window.title = "Study"
window.run()
