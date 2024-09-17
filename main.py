from kivy.app import App
from kivy.graphics import RoundedRectangle, Color
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.core.text import LabelBase

# темный фон
Window.clearcolor = (0, 0, 0, 1)

LabelBase.register(name='Roboto', fn_regular='temples\ofont.ru_Ebbe.ttf')
class AboutMeScreen(Screen):
    def build_interface(self):
        root = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Фоновое изображение
        background = Image(source='imagine\logo.jpg', allow_stretch=True, keep_ratio=False)
        root.add_widget(background)

        # Основной слой для элементов интерфейса
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20, size_hint=(1, 1))
        layout.canvas.before.clear()
        with layout.canvas.before:
            Color(0.1, 0.1, 0.1, 0.8)  # Цвет фона (темный серый)
            self.rect = RoundedRectangle(size=layout.size, pos=layout.pos, radius=[15])
            layout.bind(size=self._update_rect, pos=self._update_rect)

        # Заголовок


        # Описание
        description = Label(
            text='Меня зовут Ифтихор Хайдаралиев. Я учусь в 11 классе и родился 22 июля 2007 года. Программированием занимаюсь более двух лет. За это время я освоил основы Python и несколько популярных библиотек, таких как Kivy для разработки графических интерфейсов, Aiogram для создания Telegram-ботов и Pygame для разработки игр. Я увлечен разработкой программного обеспечения и постоянно стремлюсь расширять свои знания и навыки. В своих проектах я сосредоточен на создании полезных инструментов и приложений, которые могут улучшить жизнь пользователей.',
            font_size='18sp', size_hint=(1, None), height=150, color=(0.9, 0.4, 0.8, 1), halign='center',
            font_name='Roboto'
        )
        description.bind(size=self.update_text_size)
        layout.add_widget(description)

        # Кнопка для открытия GitHub
        github_btn = Button(text='Моя страница в GitHub', size_hint=(1, None), height=50,
                            background_color=(0.29, 0.0, 0.51, 1), color=(1, 1, 1, 1))
        github_btn.bind(on_press=self.open_github)
        layout.add_widget(github_btn)

        # Кнопка для возврата назад
        back_btn = Button(text='Назад', size_hint=(1, None), height=50,
                          background_color=(0.29, 0.0, 0.51, 1), color=(1, 1, 1, 1))
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)

        root.add_widget(layout)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def update_text_size(self, instance, value):
        instance.text_size = (instance.width * 0.9, None)

    def open_github(self, instance):
        import webbrowser
        webbrowser.open('https://github.com/WSXvsLUCKY')  # Замените на свою страницу в GitHub

    def go_back(self, instance):
        self.manager.current = 'main_screen'

    def on_enter(self):
        self.clear_widgets()
        self.add_widget(self.build_interface())
#------------------------------------------------------------------------------------------------------------------------------------------
#Окно категории финанс приложения
class FinanceAppScreen(Screen):
    def build_interface(self):
        root = RelativeLayout()

        background = Image(source='imagine\gg.webp', allow_stretch=True, keep_ratio=False)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20, size_hint=(0.8, 0.8),
                           pos_hint={"center_x": 0.5, "center_y": 0.5})

        title = Label(text='Проект: Финансовое приложение на Kivy', font_size='20sp', size_hint=(1, None), height=50, color=(1, 1, 1, 1))
        description = Label(text='''Это приложение помогает пользователям отслеживать свои доходы и расходы. Пользователь может добавлять транзакции, просматривать текущий баланс, а также просматривать историю транзакций.

Основные функции:
- Добавление доходов и расходов: Пользователь может добавить финансовые транзакции, такие как доходы и расходы, указывая сумму, категорию и дату транзакции.
- Просмотр баланса: Приложение отображает текущий баланс пользователя на основе введенных данных.
- История транзакций: Пользователь может просмотреть историю всех транзакций, отображаемую в всплывающем окне.
- Интерфейс: Приложение имеет графический интерфейс, разработанный с использованием библиотеки Kivy, включая фоновое изображение и интерфейс для ввода данных.''',
                      font_size='16sp', size_hint=(1, None), height=300, color=(1, 1, 1, 1), halign='center')
        description.bind(size=self.update_text_size)

        github_link = Button(text='Перейти на GitHub', size_hint=(1, None), height=50, background_color=(0.29, 0.0, 0.51, 1))
        github_link.bind(on_press=lambda x: self.open_github())

        back_btn = Button(text='Назад', size_hint=(1, None), height=50, background_color=(0.29, 0.0, 0.51, 1))
        back_btn.bind(on_press=self.go_back)

        layout.add_widget(title)
        layout.add_widget(description)
        layout.add_widget(github_link)
        layout.add_widget(back_btn)

        root.add_widget(background)
        root.add_widget(layout)

        return root

    def update_text_size(self, instance, value):
        instance.text_size = (instance.width * 0.9, None)

    def open_github(self):
        import webbrowser
        webbrowser.open('https://github.com/WSXvsLUCKY/financekivy.git')

    def go_back(self, instance):
        self.manager.current = 'categories_screen'

    def on_enter(self):
        self.clear_widgets()
        self.add_widget(self.build_interface())


class MobileAppsScreen(Screen):
    def build_interface(self):
        root = RelativeLayout()

        background = Image(source='imagine\gg.webp', allow_stretch=True, keep_ratio=False)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20, size_hint=(0.8, 0.6),
                           pos_hint={"center_x": 0.5, "center_y": 0.5})

        title = Label(text='Мобильные приложения', font_size='30sp', size_hint=(1, 0.3), color=(1, 1, 1, 1))

        finance_app_btn = Button(text='Финансовое приложение', font_size='20sp', size_hint=(1, 0.2), background_color=(0.29, 0.0, 0.51, 1))
        finance_app_btn.bind(on_press=self.show_finance_app)

        back_btn = Button(text='Назад', size_hint=(1, 0.2), background_color=(0.29, 0.0, 0.51, 1))
        back_btn.bind(on_press=self.go_back)

        layout.add_widget(title)
        layout.add_widget(finance_app_btn)
        layout.add_widget(back_btn)

        root.add_widget(background)
        root.add_widget(layout)

        return root

    def show_finance_app(self, instance):
        self.manager.current = 'finance_app_screen'

    def go_back(self, instance):
        self.manager.current = 'categories_screen'

    def on_enter(self):
        self.clear_widgets()
        self.add_widget(self.build_interface())

#------------------------------------------------------------------------------------------------------------------------------------------
#окно игры RocketSurvival
class RocketSurvivalScreen(Screen):
    def build_interface(self):
        root = RelativeLayout()

        # Добавление фонового изображения
        background = Image(source='imagine\gg.webp', allow_stretch=True, keep_ratio=False)

        # Основной вертикальный слой для элементов интерфейса
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20, size_hint=(0.8, 0.8),
                           pos_hint={"center_x": 0.5, "center_y": 0.5})

        # Заголовок и описание проекта
        title = Label(text='Проект: Rocket Survival', font_size='20sp', size_hint=(1, None),
                      height=50, color=(1, 1, 1, 1), halign='center')
        title.bind(size=self.update_text_size)

        description = Label(text='''Эта игра представляет собой простую аркаду, в которой игрок управляет ракетой и избегает столкновений с монстрами, которые падают сверху экрана. 
Основные функции:
- Управление ракетой с помощью клавиш LEFT и RIGHT
- Монстры появляются случайным образом и движутся вниз
- Счёт увеличивается за каждый монстр, который проходит мимо
- Игра завершается при столкновении ракеты с монстром
- Основной цикл обновляет экран, перемещает монстров и проверяет столкновения''', font_size='16sp',
                           size_hint=(1, None), height=300, color=(1, 1, 1, 1), halign='center')
        description.bind(size=self.update_text_size)

        # Кнопка для открытия GitHub
        github_link = Button(text='Перейти на GitHub', size_hint=(1, None), height=50,
                             background_color=(0.29, 0.0, 0.51, 1))
        github_link.bind(on_press=lambda x: self.open_github())

        # Кнопка для возврата назад
        back_btn = Button(text='Назад', size_hint=(1, None), height=50, background_color=(0.29, 0.0, 0.51, 1))
        back_btn.bind(on_press=self.go_back)

        # Добавляем виджеты в макет
        layout.add_widget(title)
        layout.add_widget(description)
        layout.add_widget(github_link)
        layout.add_widget(back_btn)

        # Добавляем фон и основной интерфейс в корневой слой
        root.add_widget(background)
        root.add_widget(layout)

        return root

    def update_text_size(self, instance, value):
        instance.text_size = (instance.width * 0.9, None)

    def go_back(self, instance):
        self.manager.current = 'games_screen'

    def open_github(self):
        import webbrowser
        webbrowser.open('https://github.com/WSXvsLUCKY/game.git')  # Замените на правильную ссылку на ваш репозиторий

    def on_enter(self):
        self.clear_widgets()
        self.add_widget(self.build_interface())


class GamesScreen(Screen):
    def build_interface(self):
        root = RelativeLayout()

        # Добавление фонового изображения
        background = Image(source='imagine\gg.webp', allow_stretch=True, keep_ratio=False)

        # Основной вертикальный слой для элементов интерфейса
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20, size_hint=(0.8, 0.6),
                           pos_hint={"center_x": 0.5, "center_y": 0.5})

        # Заголовок "Игры"
        title = Label(text='Игры', font_size='30sp', size_hint=(1, 0.3), color=(1, 1, 1, 1))

        # Примеры кнопок для игр
        game1_btn = Button(text='Rocket Survival', font_size='20sp', size_hint=(1, 0.2), background_color=(0.29, 0.0, 0.51, 1))

        # Привязка действий кнопок
        game1_btn.bind(on_press=self.show_game1)

        # Кнопка для возврата назад
        back_btn = Button(text='Назад', size_hint=(1, 0.2), background_color=(0.29, 0.0, 0.51, 1))
        back_btn.bind(on_press=self.go_back)

        # Добавляем виджеты в макет
        layout.add_widget(title)
        layout.add_widget(game1_btn)
        layout.add_widget(back_btn)

        # Добавляем фон и основной интерфейс в корневой слой
        root.add_widget(background)
        root.add_widget(layout)

        return root

    def show_game1(self, instance):
        self.manager.current = 'rocket_survival_screen'

    def go_back(self, instance):
        self.manager.current = 'categories_screen'

    def on_enter(self):
        self.clear_widgets()
        self.add_widget(self.build_interface())


#------------------------------------------------------------------------------------------------------------------------------------------
# окно тг-бота(ежедневный план)
class EarningsBotScreen(Screen):
    def build_interface(self):
        root = RelativeLayout()

        # Добавление фонового изображения
        background = Image(source='imagine\gg.webp', allow_stretch=True, keep_ratio=False)

        # Основной вертикальный слой для элементов интерфейса
        layout = BoxLayout(orientation='vertical', padding=[30, 20, 30, 20], spacing=30, size_hint=(0.8, 0.8),
                           pos_hint={"center_x": 0.5, "center_y": 0.5})

        # Заголовок и описание проекта
        title = Label(text='Проект: Telegram Бот для управления ежедневными планами', font_size='20sp',
                      size_hint=(1, None),
                      height=50, color=(1, 1, 1, 1), halign='center')
        title.bind(size=self.update_text_size)

        description = Label(text='''Этот бот помогает пользователям управлять своими ежедневными планами, основываясь на их возрасте.
Основные функции:
- Установка возраста
- Создание плана на день
- Уведомления
- База данных (SQLite)''', font_size='16sp', size_hint=(1, None), height=200, color=(1, 1, 1, 1), halign='center')
        description.bind(size=self.update_text_size)

        # Кнопка для открытия GitHub
        github_link = Button(text='Перейти на GitHub', size_hint=(1, None), height=50,
                             background_color=(0.29, 0.0, 0.51, 1))
        github_link.bind(on_press=lambda x: self.open_github())

        # Кнопка для возврата назад
        back_btn = Button(text='Назад', size_hint=(1, None), height=50, background_color=(0.29, 0.0, 0.51, 1))
        back_btn.bind(on_press=self.go_back)

        # Добавляем виджеты в макет
        layout.add_widget(title)
        layout.add_widget(description)
        layout.add_widget(github_link)
        layout.add_widget(back_btn)

        # Добавляем фон и основной интерфейс в корневой слой
        root.add_widget(background)
        root.add_widget(layout)

        return root

    def update_text_size(self, instance, value):
        instance.text_size = (
        instance.width * 0.9, None)

    def go_back(self, instance):
        self.manager.current = 'telegram_bots_screen'

    def open_github(self):
        import webbrowser
        webbrowser.open('https://github.com/WSXvsLUCKY/Forplaneveryday.git')

    def on_enter(self):
        self.clear_widgets()
        self.add_widget(self.build_interface())



class FinanceBotScreen(Screen):
    def build_interface(self):
        root = RelativeLayout()

        # Добавление фонового изображения
        background = Image(source='imagine\gg.webp', allow_stretch=True, keep_ratio=False)

        # Основной вертикальный слой для элементов интерфейса
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20, size_hint=(0.8, 0.8),
                           pos_hint={"center_x": 0.5, "center_y": 0.5})

        # Заголовок и описание проекта
        title = Label(text='Проект: Telegram Бот для управления личными финансами', font_size='20sp', size_hint=(1, 0.1), color=(1, 1, 1, 1))
        description = Label(text='''Этот бот помогает пользователям отслеживать свои доходы и расходы.
Основные функции:
- Добавление доходов и расходов
- Просмотр баланса
- Категории транзакций
- Фильтрация и статистика
- Логирование (SQLite база данных)''', font_size='16sp', size_hint=(1, 0.6), color=(1, 1, 1, 1))

        # Кнопка для открытия GitHub
        github_link = Button(text='Перейти на GitHub', size_hint=(1, 0.1), background_color=(0.29, 0.0, 0.51, 1))
        github_link.bind(on_press=lambda x: self.open_github())

        # Кнопка для возврата назад
        back_btn = Button(text='Назад', size_hint=(1, 0.1), background_color=(0.29, 0.0, 0.51, 1))
        back_btn.bind(on_press=self.go_back)

        # Добавляем виджеты в макет
        layout.add_widget(title)
        layout.add_widget(description)
        layout.add_widget(github_link)
        layout.add_widget(back_btn)

        # Добавляем фон и основной интерфейс в корневой слой
        root.add_widget(background)
        root.add_widget(layout)

        return root

    def go_back(self, instance):
        self.manager.current = 'telegram_bots_screen'

    def open_github(self):
        import webbrowser
        webbrowser.open('https://github.com/WSXvsLUCKY/-.git')


    def on_enter(self):
        self.clear_widgets()
        self.add_widget(self.build_interface())

# Окно категориями Telegram ботов
class TelegramBotsScreen(Screen):
    def build_interface(self):
        root = RelativeLayout()

        # Добавление фонового изображения
        background = Image(source='imagine\gg.webp', allow_stretch=True, keep_ratio=False)

        # Основной вертикальный слой для элементов интерфейса
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20, size_hint=(0.8, 0.6),
                           pos_hint={"center_x": 0.5, "center_y": 0.5})

        # Заголовок "Telegram боты"
        title = Label(text='Telegram Боты', font_size='30sp', size_hint=(1, 0.3), color=(1, 1, 1, 1))

        # Кнопки проектов
        earnings_bot_btn = Button(text='Telegram Бот для управления ежедневными планами', font_size='20sp', size_hint=(1, 0.2), background_color=(0.29, 0.0, 0.51, 1))
        finance_bot_btn = Button(text='Бот для финанса', font_size='20sp', size_hint=(1, 0.2), background_color=(0.29, 0.0, 0.51, 1))
        finance_bot_btn.bind(on_press=self.show_finance_bot)
        earnings_bot_btn.bind(on_press=self.show_earnings_bot)  # Привязываем обработчик

        # Кнопка для возврата назад
        back_btn = Button(text='Назад', size_hint=(1, 0.2), background_color=(0.29, 0.0, 0.51, 1))
        back_btn.bind(on_press=self.go_back)

        # Добавляем виджеты в макет
        layout.add_widget(title)
        layout.add_widget(earnings_bot_btn)
        layout.add_widget(finance_bot_btn)
        layout.add_widget(back_btn)

        # Добавляем фон и основной интерфейс в корневой слой
        root.add_widget(background)
        root.add_widget(layout)

        return root

    def show_earnings_bot(self, instance):
        self.manager.current = 'earnings_bot_screen'

    def show_finance_bot(self, instance):
        self.manager.current = 'finance_bot_screen'

    def go_back(self, instance):
        self.manager.current = 'categories_screen'

    def on_enter(self):
        self.clear_widgets()
        self.add_widget(self.build_interface())


#------------------------------------------------------------------------------------------------------------------------------------------
# окно с категориями проектов
class CategoriesScreen(Screen):
    def build_interface(self):
        root = RelativeLayout()

        background = Image(source='imagine\gg.webp', allow_stretch=True, keep_ratio=False)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20, size_hint=(0.8, 0.6),
                           pos_hint={"center_x": 0.5, "center_y": 0.5})

        title = Label(text='Категории проектов', font_size='30sp', size_hint=(1, 0.3), color=(1, 1, 1, 1))

        telegram_btn = Button(text='Телеграм-боты', font_size='20sp', size_hint=(1, 0.2),
                              background_color=(0.29, 0.0, 0.51, 1))
        telegram_btn.bind(on_press=self.show_telegram_bots)

        game_btn = Button(text='Игры', font_size='20sp', size_hint=(1, 0.2), background_color=(0.29, 0.0, 0.51, 1))
        game_btn.bind(on_press=self.show_games_screen)

        # Добавляем новую кнопку "Мобильные приложения"
        mobile_apps_btn = Button(text='Мобильные приложения', font_size='20sp', size_hint=(1, 0.2), background_color=(0.29, 0.0, 0.51, 1))
        mobile_apps_btn.bind(on_press=self.show_mobile_apps)

        back_btn = Button(text='Назад', size_hint=(1, 0.2), background_color=(0.29, 0.0, 0.51, 1))
        back_btn.bind(on_press=self.go_back)

        layout.add_widget(title)
        layout.add_widget(telegram_btn)
        layout.add_widget(game_btn)
        layout.add_widget(mobile_apps_btn)  # Добавляем новую кнопку
        layout.add_widget(back_btn)

        root.add_widget(background)
        root.add_widget(layout)

        return root

    def show_telegram_bots(self, instance):
        self.manager.current = 'telegram_bots_screen'

    def show_games_screen(self, instance):
        self.manager.current = 'games_screen'

    def show_mobile_apps(self, instance):  # Добавляем переход на экран мобильных приложений
        self.manager.current = 'mobile_apps_screen'

    def go_back(self, instance):
        self.manager.current = 'main_screen'

    def on_enter(self):
        self.clear_widgets()
        self.add_widget(self.build_interface())


#------------------------------------------------------------------------------------------------------------------------------------------
# Основной экран
class MainScreen(Screen):
    def build_interface(self):
        root = RelativeLayout()

        # Добавление фонового изображения
        background = Image(source='imagine\gg.webp', allow_stretch=True, keep_ratio=False)

        # Основной вертикальный слой для элементов интерфейса
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20, size_hint=(0.8, 0.6),
                           pos_hint={"center_x": 0.5, "center_y": 0.5})

        # Заголовок "Мои проекты"
        title = Label(text='Мои проекты', font_size='30sp', size_hint=(1, 0.3), color=(0.83, 0.83, 0.83, 1))

        # Кнопка "Категории"
        categories_btn = Button(text='Категории', font_size='20sp', size_hint=(1, 0.2), background_color=(0.29, 0.0, 0.51, 1))
        categories_btn.bind(on_press=self.show_categories)

        # Кнопка "Обо мне"
        about_btn = Button(text='Обо мне', font_size='20sp', size_hint=(1, 0.2), background_color=(0.29, 0.0, 0.51, 1))
        about_btn.bind(on_press=self.go_about_me)  # Исправление привязки метода

        # Добавляем виджеты в макет
        layout.add_widget(title)
        layout.add_widget(categories_btn)
        layout.add_widget(about_btn)

        # Добавляем фон и основной интерфейс в корневой слой
        root.add_widget(background)
        root.add_widget(layout)

        return root

    def show_categories(self, instance):
        self.manager.current = 'categories_screen'

    def go_about_me(self, instance):
        self.manager.current = 'about_me_screen'  # Исправление атрибута

    def on_enter(self):
        self.clear_widgets()
        self.add_widget(self.build_interface())



#------------------------------------------------------------------------------------------------------------------------------------------
# Основное приложение
class PortfolioApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())

        # Добавляем экраны
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(CategoriesScreen(name='categories_screen'))
        sm.add_widget(TelegramBotsScreen(name='telegram_bots_screen'))
        sm.add_widget(FinanceBotScreen(name='finance_bot_screen'))
        sm.add_widget(EarningsBotScreen(name='earnings_bot_screen'))  # Добавляем новый экран
        sm.add_widget(GamesScreen(name='games_screen')),
        sm.add_widget(RocketSurvivalScreen(name='rocket_survival_screen')),
        sm.add_widget(FinanceAppScreen(name='mobile_apps_screen')),
        sm.add_widget(AboutMeScreen(name='about_me_screen'))
        return sm


if __name__ == '__main__':
    PortfolioApp().run()
