from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Данные для входа
URL = "https://caml-kube-ukk-docs.comita.lan/"
LOGIN = "timofeyn"
PASSWORD = "76RktyGtrkRfgnPevvCkfd"

def test_login():
    # Настройка опций Chrome для игнорирования SSL-ошибок
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')

    # Инициализация драйвера с опциями
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Развернуть окно браузера на весь экран
        driver.maximize_window()

        # Открытие страницы
        driver.get(URL)

        # Ожидание и нажатие кнопки для перехода к авторизации
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/div[2]/app-home-page-header/div/div[3]/a/span"))
        )
        login_button.click()

        # Ввод логина
        login_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/div[2]/app-auth-page/div/div/div/form/fieldset/div/fieldset[1]/input"))
        )
        login_field.send_keys(LOGIN)

        # Ввод пароля
        password_field = driver.find_element(By.XPATH, "/html/body/app-root/div/div[2]/app-auth-page/div/div/div/form/fieldset/div/fieldset[2]/input")
        password_field.send_keys(PASSWORD)

        # Нажатие кнопки входа
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/div[2]/app-auth-page/div/div/div/form/fieldset/button"))
        )
        submit_button.click()

        # Ожидание для демонстрации результата
        time.sleep(5)  # Подождать 5 секунд перед закрытием браузера

    finally:
        # Закрытие браузера
        driver.quit()