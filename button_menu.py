from kivymd.uix.button import MDFillRoundFlatIconButton

translator = MDFillRoundFlatIconButton(
    text="Переводчик",
    text_color=[10/255, 10/255, 10/255, 1],
    font_size=30,
    size_hint=(0.5, 0.1),
    pos_hint={'center_x':0.5, 'center_y':0.7},
    md_bg_color=[100 / 255, 220 / 255, 180 / 255, 1],
    icon="google-translate",
    icon_color=[10/255, 10/255, 10/255, 1],
)

spelling = MDFillRoundFlatIconButton(
    text="Орфография",
    text_color=[10/255, 10/255, 10/255, 1],
    font_size=30,
    size_hint=(0.5, 0.1),
    pos_hint={'center_x':0.5, 'center_y':0.5},
    md_bg_color=[100 / 255, 220 / 255, 180 / 255, 1],
    icon="spellcheck",
    icon_color=[10/255, 10/255, 10/255, 1],
)

voice_recorder = MDFillRoundFlatIconButton(
    text="Диктофон",
    text_color=[10/255, 10/255, 10/255, 1],
    font_size=30,
    size_hint=(0.5, 0.1),
    pos_hint={'center_x':0.5, 'center_y':0.3},
    md_bg_color=[100 / 255, 220 / 255, 180 / 255, 1],
    icon="microphone",
    icon_color=[10/255, 10/255, 10/255, 1],
)

digitalization = MDFillRoundFlatIconButton(
    text="Цифровизация",
    text_color=[10/255, 10/255, 10/255, 1],
    font_size=30,
    size_hint=(0.5, 0.1),
    pos_hint={'center_x':0.5, 'center_y':0.1},
    md_bg_color=[100 / 255, 220 / 255, 180 / 255, 1],
    icon="camera",
    icon_color=[10/255, 10/255, 10/255, 1],
)

to_share = MDFillRoundFlatIconButton(
    text="Поделиться",
    text_color=[10/255, 10/255, 10/255, 1],
    font_size=30,
    size_hint=(0.5, 0.1),
    pos_hint={'center_x':0.5, 'center_y':0.9},
    md_bg_color=[100 / 255, 220 / 255, 180 / 255, 1],
    icon="share",
    icon_color=[10/255, 10/255, 10/255, 1],
)