from kivy.metrics import dp
from kivy.modules._webdebugger import app
from kivy.properties import StringProperty
from kivymd.uix.button import MDRoundFlatButton, MDFillRoundFlatButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField, MDTextFieldRect
from kivymd.utils.fitimage import FitImage
from kivymd.uix.menu import MDDropdownMenu
from random import choice
from googletrans import Translator as GoogleTranslator
from googletrans import LANGUAGES, LANGCODES
from longuages import *
from asyncio import *
from time import sleep
import speech_recognition as SRG


class Item(OneLineAvatarIconListItem):
    left_icon = StringProperty()


# key : value


# translator = GoogleTranslator()
# print(LANGCODES)


class Translator(MDScreen):
    def __init__(self, manager, **kw):
        super().__init__(**kw)

        back = FitImage(source='1.jpg')
        self.add_widget(back)

        self.language_button_left = MDFillRoundFlatButton(
            text="Русский",
            pos_hint={'center_x': 0.3, 'center_y': 0.9},
            size_hint=(0.15, 0.08),
            md_bg_color=[100 / 255, 220 / 255, 180 / 255, 1],
            text_color=[10 / 255, 10 / 255, 10 / 255, 1],
            font_size=15
        )

        self.language_button_right = MDFillRoundFlatButton(
            text="Английский",
            pos_hint={'center_x': 0.7, 'center_y': 0.9},
            size_hint=(0.15, 0.08),
            md_bg_color=[100 / 255, 220 / 255, 180 / 255, 1],
            text_color=[10 / 255, 10 / 255, 10 / 255, 1],
            font_size=15
        )

        self.menu_left = self.language_button(self.language_button_left, self.left_button_action)
        self.menu_right = self.language_button(self.language_button_right, self.right_button_action)

        self.arrow = MDIconButton(
            icon="swap-horizontal",
            user_font_size="45sp",
            pos_hint={'center_x': 0.5, 'center_y': 0.9},
            theme_text_color="Custom",
            text_color=[100 / 255, 220 / 255, 180 / 255, 1],
            on_press=self.exchange
        )

        self.add_widget(self.arrow)

        self.field = MDTextFieldRect(
            pos_hint={'center_x': 0.5, 'center_y': 0.67},
            size_hint=(0.9, 0.3),
            cursor_color=[0, 0, 0, 1],
            background_color=[100 / 255, 220 / 255, 180 / 255, 1]

        )
        self.field.bind(text=self.translate)
        self.add_widget(self.field)

        self.translation = MDLabel(
            pos_hint={'center_x': 0.5, 'center_y': 0.35},
            size_hint=(0.9, 0.3),
            md_bg_color=[100 / 255, 220 / 255, 180 / 255, 1],
            valign='top'
        )

        self.translation.bind(size=self.translation.setter('text_size'))

        self.add_widget(self.translation)

        self.voice_input = MDIconButton(
            icon="microphone",
            user_font_size="45sp",
            pos_hint={'center_x': 0.25, 'center_y': 0.1},
            theme_text_color="Custom",
            text_color=[100 / 255, 220 / 255, 180 / 255, 1],
            on_press=self.active_microphone,
            on_release=self.voice
        )
        self.add_widget(self.voice_input)

        self.foto_input = MDIconButton(
            icon="camera",
            user_font_size="45sp",
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            theme_text_color="Custom",
            text_color=[100 / 255, 220 / 255, 180 / 255, 1],

        )
        self.add_widget(self.foto_input)

        self.forum_input = MDIconButton(
            icon="forum",
            user_font_size="45sp",
            pos_hint={'center_x': 0.75, 'center_y': 0.1},
            theme_text_color="Custom",
            text_color=[100 / 255, 220 / 255, 180 / 255, 1],

        )
        self.add_widget(self.forum_input)

        self.translator = GoogleTranslator()

    def exchange(self, button):
        self.language_button_left.text, self.language_button_right.text = self.language_button_right.text, self.language_button_left.text
        self.field.text, self.translation.text = self.translation.text.strip(), self.field.text.strip()
        self.translate(text=self.field.text)

    def language_button(self, button, action):
        languages = [
            {
                "text": lang,
                "left_icon": "Flag",
                "viewclass": "Item",
                "height": dp(54),
                "on_release": lambda x=lang: action(x),
            } for lang in languages_codes.keys()
        ]

        menu = MDDropdownMenu(
            caller=button,
            items=languages,
            width_mult=4,
            max_height=dp(250),
            ver_growth='down',
            background_color=[100 / 255, 220 / 255, 180 / 255, 1]
        )
        button.on_release = menu.open
        self.add_widget(button)

        return menu

    def left_button_action(self, text_item):
        self.language_button_left.text = text_item
        self.menu_left.dismiss()
        self.translate_input(text=self.field.text)


    def right_button_action(self, text_item):
        self.language_button_right.text = text_item
        self.menu_right.dismiss()
        self.translate(text=self.field.text)

    def translate_input(self,text):
        if text == '':
            self.field.text = ' '
        else:
            self.field.text = ' ' + self.translator.translate(
                text,
                dest=languages_codes[self.language_button_left.text].split("-")[0],
            ).text.replace(".", ". ")


    def translate(self, instance=None, text=''):
        if text == '':
            self.translation.text = ' '
        else:
            # print(self.translator.translate(
            #     text,
            #     src=languages_codes[self.language_button_left.text].split("-")[0],
            #     dest=languages_codes[self.language_button_right.text].split("-")[0],
            # ).text.replace(".", ". "))
            self.translation.text = ' ' + self.translator.translate(
                text,
                src=languages_codes[self.language_button_left.text].split("-")[0],
                dest=languages_codes[self.language_button_right.text].split("-")[0],
            ).text.replace(".", ". ")

    def voice(self, button):
        # button.text_color = [255 / 255, 10 / 255, 10 / 255, 1]
        store = SRG.Recognizer()
        with SRG.Microphone() as s:
            audio_input = store.listen(s)
            text_output = store.recognize_google(
                audio_input,
                language=languages_codes[self.language_button_left.text]
            ),
            self.field.text = text_output[0]
        button.text_color = [100 / 255, 220 / 255, 180 / 255, 1]

    def active_microphone(self, button):
        button.text_color = [255 / 255, 10 / 255, 10 / 255, 1]
