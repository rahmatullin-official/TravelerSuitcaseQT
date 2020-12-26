from PyQt5.QtGui import QIcon  # подкючение библоитек QT
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
import pyowm  # библиотека для определения определения погоды
from main_window_ui import Main_Window  # подключение стилей
from selectdata_ui import Data  # подключение стилей
from converter_ui import Converter  # подключение стилей
from currency_converter import CurrencyConverter  # библиотека для определения курса валюты
from country_ui import Country  # подключение стилей
from incountry_weather_ui import Incountry  # подключение стилей
from incountry_weather_type_ui import InCountryWarmType  # подключение стилей
from incountry_weather_beach_gender_ui import InCountryBeachGender  # подключение стилей
from incountry_weather_buisnesstrip_gender_ui import InCountryWeatherBuisnesstripGender  # подключение стилей
from incoutry_cold_type_ui import InCountryColdType  # подключение стилей
from incountry_weather_mountain_gender_ui import MountainGender  # подключение стилей
from incountry_cold_buisnesstrip_gender_ui import IncountryColdBuisnessTrip  # подключение стилей
from outcountry_weather_ui import OutcountryWeather  # подключение стилей
from outcountry_cold_type_ui import OutCountryTypeCold  # подключение стилей
from outcountry_warm_type_ui import OutCountryWarmType  # подключение стилей
from outcountry_cold_camping_gender_ui import OutcountryColdCamping  # подключение стилей
from outcountry_cold_excursion_gender_ui import OutcountryColdExcursion  # подключение стилей
from outcountry_warm_camping_gender_ui import OutcountryWarmCamping  # подключение стилей
from outcountry_warm_excursion_gender_ui import OutCountryWarmExcursion  # подключение стилей
from info_ui import Info  # подключение стилей
from temperature_ui import Temperature  # подключение стилей
import sys  # для работы с потоковым ввводом (QT)
import sqlite3  # библиотека для работы с БД

DATA = None  # вводим константу


class MyWidget(QMainWindow, Main_Window):  # создание главного окна приложения

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Traveler's suitcase")  # заголовок окна
        self.button_convert.clicked.connect(self.show_window_2)  # при нажатии на кнопку вызов функции show_window
        self.button_travel.clicked.connect(self.show_window_1)  # при нажатии на кнопку вызов функции show_window
        self.button_weather.clicked.connect(self.show_window_3)  # при нажатии на кнопку вызов функции show_window
        self.information.clicked.connect(self.show_window_4)  # при нажатии на кнопку вызов функции show_window
        self.setWindowIcon(QIcon('images/ico.png'))  # иконка окна

    def show_window_1(self):
        self.cams = FirstWindow()  # переключение камеры на класс FirstWidndow()
        self.cams.show()  # показть класс
        self.close()  # закрыть класс MyWidget()

    def show_window_2(self):
        self.cams = SecondWindow()  # переключение камеры на класс SecondWidndow()
        self.cams.show()  # показть класс
        self.close()  # закрыть класс MyWidget()

    def show_window_3(self):
        self.cams = ThirdWindow()  # переключение камеры на класс ThirdWidndow()
        self.cams.show()  # показть класс
        self.close()  # закрыть класс MyWidget()

    def show_window_4(self):
        self.cams = FourthWindow()  # переключение камеры на класс FourthWidndow()
        self.cams.show()  # показть класс
        self.close()  # закрыть класс MyWidget()


class FirstWindow(QMainWindow, Country):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Place')  # заголовок окна
        self.setWindowIcon(QIcon('images/ico.png'))  # иконка окна
        self.button_incountry.clicked.connect(
            self.show_window_InCountry)  # при нажатии на кнопку вызов функции show_window_InCountry
        self.button_outcontry.clicked.connect(
            self.show_window_OutCountry)  # при нажатии на кнопку вызов функции show_window_OutCountry

    def show_window_InCountry(self):
        self.cams = InCountry()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс

    def show_window_OutCountry(self):
        self.cams = OutCountry()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс


class OutCountry(QMainWindow, OutcountryWeather):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('OutCountry')  # заголовок
        self.setWindowIcon(QIcon('images/ico.png'))  # иконка
        self.button_outcontry.clicked.connect(self.show_window_Outcountry_cold)  # при нажатии на кнопку вызов функции
        self.button_outcountry_warm.clicked.connect(
            self.show_window_Outcountry_warm)  # при нажатии на кнопку вызов функции

    def show_window_Outcountry_warm(self):
        self.cams = OutCountryWarmTypee()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс

    def show_window_Outcountry_cold(self):
        self.cams = OutCountryColdType()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс


class OutCountryColdType(QMainWindow, OutCountryTypeCold):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Outcountry Cold')  # заголовок
        self.setWindowIcon(QIcon('images/ico.png'))  # иконка
        self.button_outcountry_cold_camping.clicked.connect(
            self.show_window_Outcountry_cold_camping)  # при нажатии на кнопку вызов функции
        self.button_outcountry_cold_excursion.clicked.connect(
            self.show_window_Outcountry_cold_excursion)  # при нажатии на кнопку вызов функции

    def show_window_Outcountry_cold_camping(self):
        self.cams = OutCountryCampingCold()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс

    def show_window_Outcountry_cold_excursion(self):
        self.cams = OutCountryExcursionCold()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс


class OutCountryCampingCold(QMainWindow, OutcountryColdCamping):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Outcountry camping cold')  # заголовок
        self.setWindowIcon(QIcon('images/ico.png'))  # иконка
        self.button_outcountry_cold_camping_male.clicked.connect(
            self.show_outcountry_cold_camping_male)  # при нажатии на кнопку вызов функции
        self.button_outcountry_cold_camping_female.clicked.connect(
            self.show_outcountry_cold_camping_female)  # при нажатии на кнопку вызов функции

    def show_outcountry_cold_camping_male(self):
        global DATA  # глобальная переменная для переноса данных из одного класса в другой ChecklistGenerator
        DATA = 'outcountry_cold_camping_man'  # присвоение названия таблицы в глобальную переменную для генератора
        self.cams = ChecklistGenerator()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс

    def show_outcountry_cold_camping_female(self):
        global DATA  # глобальная переменная
        DATA = 'outcountry_cold_camping_female'  # присвоение названия таблицы в глобальную переменную для генератора
        self.cams = ChecklistGenerator()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс


class OutCountryExcursionCold(QMainWindow, OutcountryColdExcursion):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Outcountry Excursion cold')  # заголовок
        self.setWindowIcon(QIcon('images/ico.png'))  # иконка
        self.button_outcountry_cold_excrusion_male.clicked.connect(
            self.show_outcountry_cold_excursion_male)  # при нажатии на кнопку вызов функции
        self.button_outcountry_cold_excursion_female.clicked.connect(
            self.show_outcountry_cold_excursion_female)  # при нажатии на кнопку вызов функции

    def show_outcountry_cold_excursion_male(self):
        global DATA
        DATA = 'outcountry_cold_excursion_man'  # присвоение названия таблицы в глобальную переменную для генератора
        self.cams = ChecklistGenerator()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс

    def show_outcountry_cold_excursion_female(self):
        global DATA
        DATA = 'outcountry_cold_excursion_female'  # присвоение названия таблицы в глобальную переменную для генератора
        self.cams = ChecklistGenerator()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс


class OutCountryWarmTypee(QMainWindow, OutCountryWarmType):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Outcountry warm')  # заголовок
        self.setWindowIcon(QIcon('images/ico.png'))  # иконка
        self.button_outcountry_warm_camping.clicked.connect(
            self.show_window_Outcountry_warm_camping)  # при нажатии на кнопку вызов функции
        self.button_outcountry_warm_excursion.clicked.connect(
            self.show_window_Outcountry_warm_excursion)  # при нажатии на кнопку вызов функции

    def show_window_Outcountry_warm_camping(self):
        self.cams = OutCountryWarmCamping()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс

    def show_window_Outcountry_warm_excursion(self):
        self.cams = OutCountryWarmExcursionn()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс


class OutCountryWarmCamping(QMainWindow, OutcountryWarmCamping):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Outcountry warm camping')  # заголовок
        self.setWindowIcon(QIcon('images/ico.png'))  # иконка
        self.button_outcountry_warm_camping_female.clicked.connect(
            self.show_incountry_warm_camping_female)  # при нажатии на кнопку вызов функции
        self.button_outcountry_warm_camping_male.clicked.connect(
            self.show_incountry_warm_camping_male)  # при нажатии на кнопку вызов функции

    def show_incountry_warm_camping_male(self):
        global DATA  # глобальная переменная
        DATA = 'incountry_warm_camping_man'  # присвоение названия таблицы в глобальную переменную для генератора
        self.cams = ChecklistGenerator()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс

    def show_incountry_warm_camping_female(self):
        global DATA  # глобальная переменная
        DATA = 'incountry_warm_camping_female'  # присвоение названия таблицы в глобальную переменную для генератора
        self.cams = ChecklistGenerator()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс


class OutCountryWarmExcursionn(QMainWindow, OutCountryWarmExcursion):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Outcountry warm Excursion')  # заголовок
        self.setWindowIcon(QIcon('images/ico.png'))  # иконка
        self.button_outcountry_warm_excursion_female.clicked.connect(
            self.show_outcountry_warm_excursion_female)  # при нажатии на кнопку вызов функции
        self.button_outcountry_warm_excursion_male.clicked.connect(
            self.show_outcountry_warm_excursion_male)  # при нажатии на кнопку вызов функции

    def show_outcountry_warm_excursion_male(self):
        global DATA  # глобальная переменная
        DATA = 'outcountry_warm_excursion_man'  # присвоение названия таблицы в глобальную переменную для генератора
        self.cams = ChecklistGenerator()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс

    def show_outcountry_warm_excursion_female(self):
        global DATA  # глобальная пременная
        DATA = 'outcountry_warm_excursion_female'  # присвоение названия таблицы в глобальную переменную для генератора
        self.cams = ChecklistGenerator()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс


class InCountry(QMainWindow, Incountry):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Incountry')  # заголовок
        self.setWindowIcon(QIcon('images/ico.png'))  # иконка
        self.button_incountry_warm.clicked.connect(
            self.show_window_Incountry_warm)  # при нажатии на кнопку вызов функции
        self.button_outcontry.clicked.connect(self.show_window_Incountry_cold)  # при нажатии на кнопку вызов функции

    def show_window_Incountry_warm(self):
        self.cams = InCountryWarm()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс

    def show_window_Incountry_cold(self):
        self.cams = InCountryColdTypee()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс


class InCountryColdTypee(QMainWindow, InCountryColdType):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Incountry Cold')  # заголовок
        self.setWindowIcon(QIcon('images/ico.png'))  # иконка
        self.button_incountry_cold_mountains.clicked.connect(
            self.show_window_Incountry_cold_mountains)  # при нажатии на кнопку вызов функции
        self.button_incountry_cold_buisnesstrip.clicked.connect(
            self.show_window_Incountry_cold_buisnesstrip)  # при нажатии на кнопку вызов функции

    def show_window_Incountry_cold_mountains(self):
        self.cams = InCountryColdMountainGender()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс

    def show_window_Incountry_cold_buisnesstrip(self):
        self.cams = InCountryColdBuisnessTripGender()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс


class InCountryColdBuisnessTripGender(QMainWindow, IncountryColdBuisnessTrip):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Incountry cold buisnesstrip')  # заголовок
        self.setWindowIcon(QIcon('images/ico.png'))  # иконка
        self.button_incountry_cold_buisnesstrip_male.clicked.connect(
            self.show_incountry_cold_buisnesstrip_male)  # при нажатии на кнопку вызов функции
        self.button_incountry_cold_buisnesstrip_female.clicked.connect(
            self.show_incountry_cold_buisnesstrip_female)  # при нажатии на кнопку вызов функции

    def show_incountry_cold_buisnesstrip_male(self):
        global DATA  # глобальная переменная
        DATA = 'incountry_cold_buisnesstrip_man'  # присвоение названия таблицы в глобальную переменную для генератора
        self.cams = ChecklistGenerator()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс

    def show_incountry_cold_buisnesstrip_female(self):
        global DATA  # глобальная переменная
        DATA = 'incountry_cold_buisnesstrip_female'  # присвоение названия таблицы в глобальную переменную для генератора
        self.cams = ChecklistGenerator()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс


class InCountryColdMountainGender(QMainWindow, MountainGender):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Incountry cold Mountain')  # заголовок
        self.setWindowIcon(QIcon('images/ico.png'))  # иконка
        self.button_incountry_cold_mountains_male.clicked.connect(
            self.show_incountry_cold_mountains_male)  # при нажатии на кнопку вызов функции
        self.button_incountry_cold_mountains_female.clicked.connect(
            self.show_incountry_cold_mountains_female)  # при нажатии на кнопку вызов функции

    def show_incountry_cold_mountains_male(self):
        global DATA  # глобальная переменная
        DATA = 'incountry_mountains_man'  # присвоение названия таблицы в глобальную переменную для генератора
        self.cams = ChecklistGenerator()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс

    def show_incountry_cold_mountains_female(self):
        global DATA  # глобальная переменная
        DATA = 'incountry_mountains_female'  # присвоение названия таблицы в глобальную переменную для генератора
        self.cams = ChecklistGenerator()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс


class InCountryWarm(QMainWindow, InCountryWarmType):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Incountry warm')  # заголовок
        self.setWindowIcon(QIcon('images/ico.png'))  # иконка
        self.button_incountry_warm_beach.clicked.connect(
            self.show_incountry_warm_beach)  # при нажатии на кнопку вызов функции
        self.button_incountry_warm_buisnesstrip.clicked.connect(
            self.show_incountry_warm_buisnesstrip)  # при нажатии на кнопку вызов функции

    def show_incountry_warm_beach(self):
        self.cams = InCountryWarmBeachGender()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс

    def show_incountry_warm_buisnesstrip(self):
        self.cams = InCountryWarmBuisnesstripGender()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс


class InCountryWarmBuisnesstripGender(QMainWindow, InCountryWeatherBuisnesstripGender):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Incountry warm buisnesstrip')  # заголовок
        self.setWindowIcon(QIcon('images/ico.png'))  # иконка
        self.button_incountry_warm_buisnesstrip_male.clicked.connect(
            self.show_incountry_warm_buisnesstrip_male)  # при нажатии на кнопку вызов функции
        self.button_incountry_warm_buisnesstrip_female.clicked.connect(
            self.show_incountry_warm_buisnesstrip_female)  # при нажатии на кнопку вызов функции

    def show_incountry_warm_buisnesstrip_male(self):
        global DATA  # глобальная переменная
        DATA = 'incountry_warm_buisnesstrip_man'  # присвоение названия таблицы в глобальную переменную для генератора
        self.cams = ChecklistGenerator()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс

    def show_incountry_warm_buisnesstrip_female(self):
        global DATA  # глобальная переменная
        DATA = 'incountry_warm_buisnesstrip_female'  # присвоение названия таблицы в глобальную переменную для генератора
        self.cams = ChecklistGenerator()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс


class InCountryWarmBeachGender(QMainWindow, InCountryBeachGender):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Incountry warm beach')  # заголовок
        self.setWindowIcon(QIcon('images/ico.png'))  # иконка
        self.button_incountry_warm_beach_male.clicked.connect(
            self.show_window_InCountryWarmBeachMale)  # при нажатии на кнопку вызов функции
        self.button_incountry_warm_beach_female.clicked.connect(
            self.show_window_InCountryWarmBeachFemale)  # при нажатии на кнопку вызов функции

    def show_window_InCountryWarmBeachMale(self):
        global DATA  # глобальная
        DATA = 'incounty_beach_man'  # присвоение названия таблицы в глобальную переменную для генератора
        self.cams = ChecklistGenerator()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс

    def show_window_InCountryWarmBeachFemale(self):
        global DATA  # глоабльная
        DATA = 'incountry_beach_female'  # присвоение названия таблицы в глобальную переменную для генератора
        self.cams = ChecklistGenerator()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс


class ChecklistGenerator(QMainWindow, Data):
    global DATA  # глобальная

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Your Checklist!')  # заголовок
        self.setWindowIcon(QIcon('images/ico.png'))  # иконка
        mydb = sqlite3.connect("bd.db")  # подключпение к БД

        mycursor = mydb.cursor()  # курсор БД
        mycursor.execute(f"""SELECT * from {DATA}""")  # выборка из БД

        result = mycursor.fetchall()  # получение результата
        self.tableWidget.setRowCount(0)  # отсчет таблицы с нуля
        for row_number, row_data in enumerate(result):  # циклом проходимся по результату заполняем таблицу
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))


class SecondWindow(QMainWindow, Converter):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('Converter')  # заголовок
        self.setWindowIcon(QIcon('images/payments.png'))  # иконка

        self.input_currency.setPlaceholderText('From Valute: (USD/RUB)')  # подсказка что вводить пользователю
        self.input_amount.setPlaceholderText('Your Valute: (100/200)')  # подсказка что вводить пользователю
        self.output_currency.setPlaceholderText('In Valute: (USD/RUB)')  # подсказка что вводить пользователю
        self.output_amount.setPlaceholderText('I claim:')  # подсказка что получит пользователь

        self.btn_home.clicked.connect(self.show_window_1)  # при нажатии на кнопку вызов функции
        self.pushButton.clicked.connect(self.converter)  # при нажатии на кнопку вызов функции

    def converter(self):  # функция для конвертирования валюты
        try:
            c = CurrencyConverter()  # кладем класс в переменную
            input_currency = self.input_currency.text()  # получаем информацию с lable и кладем ее в переменную
            output_currency = self.output_currency.text()  # получаем информацию с lable и кладем ее в переменную
            input_amount = int(self.input_amount.text())  # получаем информацию с lable и кладем ее в переменную

            output_amount = round(c.convert(input_amount, '%s' % (input_currency), '%s' % (output_currency)),
                                  2)  # конвертируем и присваеваем в переменную значения

            self.output_amount.setText(str(output_amount))  # добавляем результат в label
        except BufferError:  # если ошибка буфферизации
            self.input_currency.setText(str('incorrect value!'))  # говорим пользователю что он неправильно ввел данные
            self.input_amount.setText(str('correct USD/RUB/EUR'))  # говорим пользователю что он неправильно ввел данные

    def show_window_1(self):
        self.cams = MyWidget()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс


class ThirdWindow(QMainWindow, Temperature):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Weather')  # заголовок
        self.setWindowIcon(QIcon('images/cloudy.png'))  # иконка
        self.btn_home.clicked.connect(self.show_window_1)  # при нажатии на кнопку вызов функции
        self.button_get_the_weather.clicked.connect(self.get_the_weather)  # при нажатии на кнопку вызов функции

    def get_the_weather(self):
        object = self.lineEdit.text()  # забираем данные с lineEdit где user хочет узнать погоду
        owm = pyowm.OWM(
            'c95cbe441c8af39819d1f47e716aa49e')  # для работы библиотеки требуется свой api ключ, который получается на сайте
        mgr = owm.weather_manager()  # обращаемся к owm
        observation = mgr.weather_at_place(object)  # получаем сводку погоды из нужного места
        w = observation.weather  # получаем погоду
        temperature = w.temperature('celsius')[
            'temp']  # берем температуру указываем в градусах цельсия можно в фарингейте по приколу но пользователям не удобно будет
        self.label_2.setText(
            f"В {object} сейчас {temperature}°С")  # результат записываем на label отображая пользователю

    def show_window_1(self):
        self.cams = MyWidget()  # переключение камеры на класс
        self.cams.show()  # показть класс
        self.close()  # закрыть класс


class FourthWindow(QMainWindow, Info):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Information')  # заголовок
        self.setWindowIcon(QIcon('images/info.png'))  # иконка
        self.btn_home.clicked.connect(self.show_window_1)  # при нажатии на кнопку вызов функции

    def show_window_1(self):
        self.cams = MyWidget()  # переключение камеры на класс MyWidget()
        self.cams.show()  # показть класс
        self.close()  # закрыть класс


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
