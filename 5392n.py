from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Данные для входа
URL = "https://caml-kube-ukk-docs.comita.lan/"
LOGIN = "timofeyn"  # Логин
PASSWORD = "76RktyGtrkRfgnPevvCkfd"  # Пароль


def test_login_and_actions():
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

        # Ожидание завершения авторизации
        time.sleep(5)  # Подождать 5 секунд

        # Скролл до нужного раздела
        section = driver.find_element(By.XPATH, '//*[@id="nav"]/div/div[8]/div[1]/span')
        driver.execute_script("arguments[0].scrollIntoView();", section)

        # Открытие папки
        folder = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="nav"]/div/div[8]/div[2]/a[1]'))
        )
        folder.click()

        # Выбор документа и двойной клик
        document = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mainblock"]/app-strateg5392u-draft-list/div/div[2]/div[2]/table/tbody/tr[1]/td[2]'))
        )
        ActionChains(driver).double_click(document).perform()  # Двойной клик

        # Ожидание загрузки документа
        time.sleep(5)  # Подождать 5 секунд

        # Проверка наличия и активности полей
        fields = [
            '//*[@id="parentDivNav"]/app-armstrategko-oes-otkaz-goz-5392u/div/div[2]/app-arm-doc-view-service-part/div/div[1]/div[1]/input',
            '//*[@id="parentDivNav"]/app-armstrategko-oes-otkaz-goz-5392u/div/div[2]/app-arm-doc-view-service-part/div/div[1]/div[2]/input',
            '//*[@id="parentDivNav"]/app-armstrategko-oes-otkaz-goz-5392u/div/div[2]/app-arm-doc-view-service-part/div/div[2]/div[1]/input',
            '//*[@id="parentDivNav"]/app-armstrategko-oes-otkaz-goz-5392u/div/div[2]/app-arm-doc-view-service-part/div/div[2]/div[2]/input',
            '//*[@id="parentDivNav"]/app-armstrategko-oes-otkaz-goz-5392u/div/div[2]/app-arm-doc-view-service-part/div/div[3]/div[1]/ng-select/div/div/div[3]/input',
            '//*[@id="parentDivNav"]/app-armstrategko-oes-otkaz-goz-5392u/div/div[2]/app-arm-doc-view-service-part/div/div[3]/div[2]/app-datepicker/div/input[2]',
            '//*[@id="parentDivNav"]/app-armstrategko-oes-otkaz-goz-5392u/div/div[2]/app-arm-doc-info-auth-person-org/div/div[1]/div/input',
            '//*[@id="parentDivNav"]/app-armstrategko-oes-otkaz-goz-5392u/div/div[2]/app-arm-doc-info-auth-person-org/div/app-arm-doc-view-fio/div/div[1]/input',
            '//*[@id="parentDivNav"]/app-armstrategko-oes-otkaz-goz-5392u/div/div[2]/app-arm-doc-info-auth-person-org/div/app-arm-doc-view-fio/div/div[2]/input',
            '//*[@id="parentDivNav"]/app-armstrategko-oes-otkaz-goz-5392u/div/div[2]/app-arm-doc-info-auth-person-org/div/div[2]/div[1]/input',
            '//*[@id="parentDivNav"]/app-armstrategko-oes-otkaz-goz-5392u/div/div[2]/app-arm-doc-info-auth-person-org/div/div[2]/div[2]/input',
            '//*[@id="parentDivNav"]/app-armstrategko-oes-otkaz-goz-5392u/div/div[2]/app-armstrategko-sved-ko/div[1]/div[1]/input',
            '//*[@id="parentDivNav"]/app-armstrategko-oes-otkaz-goz-5392u/div/div[2]/app-armstrategko-sved-ko/div[1]/div[2]/input',
            '//*[@id="parentDivNav"]/app-armstrategko-oes-otkaz-goz-5392u/div/div[2]/app-armstrategko-sved-ko/div[2]/div[1]/input',
            '//*[@id="parentDivNav"]/app-armstrategko-oes-otkaz-goz-5392u/div/div[2]/app-armstrategko-sved-ko/div[2]/div[2]/app-dict-qref-cbbnkseek/app-custom-select/ng-select/div/div/div[3]/input'
        ]

        for field in fields:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, field))
            )
            assert element.is_displayed(), f"Поле {field} не отображается"
            assert element.is_enabled(), f"Поле {field} не активно"

        # Проверка наличия надписи раздела
        section_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="parentDivNav"]/app-armstrategko-oes-otkaz-goz-5392u/div/div[2]/h4[2]'))
        )
        assert section_title.is_displayed(), "Надпись раздела не отображается"

        # Проверка кнопки "Добавить"
        add_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="parentDivNav"]/app-armstrategko-oes-otkaz-goz-5392u/div/div[2]/app-armstrategko-vladelets/app-table-comp/div/div/div/button'))
        )
        assert add_button.is_displayed(), "Кнопка 'Добавить' не отображается"
        assert add_button.is_enabled(), "Кнопка 'Добавить' не активна"

        # Проверка чекбокса
        checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="parentDivNav"]/app-armstrategko-oes-otkaz-goz-5392u/div/div[2]/app-armstrategko-vladelets/app-table-comp/div/div/table/tbody/tr/td[1]'))
        )

        # Прокручиваем элемент в область видимости
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)

        # Ждем, пока элемент станет кликабельным
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="parentDivNav"]/app-armstrategko-oes-otkaz-goz-5392u/div/div[2]/app-armstrategko-vladelets/app-table-comp/div/div/table/tbody/tr/td[1]'))
        )

        # Активация чекбокса
        checkbox.click()

        # Проверка раскрытия раздела после активации чекбокса
        expanded_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="parentDivNav"]/app-armstrategko-oes-otkaz-goz-5392u/div/div[2]/h4[3]'))
        )
        assert expanded_section.is_displayed(), "Раздел не раскрылся после активации чекбокса"

        # Двойной клик по чекбоксу для входа в раздел
        ActionChains(driver).double_click(checkbox).perform()

        # Ожидание загрузки модального окна
        try:
            modal_window = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/ngb-modal-window"))
            )
            assert modal_window.is_displayed(), "Модальное окно не отображается"
        except TimeoutException:
            logger.error("Модальное окно не найдено.")
            driver.save_screenshot("modal_window_error.png")
            raise

        # Проверка полей в разделе "Сведения о владельцах отдельных счетов и отказах"
        owner_fields = [
            ('/html/body/ngb-modal-window/div/div/app-table-editor/div[2]/ng-component/div/div/div[1]', "ТипВладелец"),
            ('/html/body/ngb-modal-window/div/div/app-table-editor/div[2]/ng-component/div/div/div[2]/input', "НаимВладелец"),
            ('/html/body/ngb-modal-window/div/div/app-table-editor/div[2]/ng-component/div/div/div[3]/div[1]', "ОГРНВладелец"),
            ('/html/body/ngb-modal-window/div/div/app-table-editor/div[2]/ng-component/div/div/div[3]/div[2]', "ИННВладелец"),
            ('/html/body/ngb-modal-window/div/div/app-table-editor/div[2]/ng-component/div/div/div[3]/div[3]', "КППВладелец"),
            ('/html/body/ngb-modal-window/div/div/app-table-editor/div[2]/ng-component/div/div/div[4]/div', "НомерОтдСчет"),
        ]

        for xpath, field_name in owner_fields:
            try:
                element = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                assert element.is_displayed(), f"Поле '{field_name}' не отображается"
                assert element.is_enabled(), f"Поле '{field_name}' не активно"
            except TimeoutException:
                logger.error(f"Поле '{field_name}' не найдено.")
                driver.save_screenshot(f"{field_name}_error.png")
                raise

        # Выбор значения "1" (юридическое лицо резидент)
        owner_type_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/ngb-modal-window/div/div/app-table-editor/div[2]/ng-component/div/div/div[1]/app-dict-qref-clienttype-213/app-custom-select/ng-select/div/div/div[3]/input'))
        )
        owner_type_dropdown.click()

        # Выбор значения "1" из выпадающего списка
        option_1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="ng-dropdown-panel-items scroll-host"]//div[contains(text(), "1")]'))
        )
        option_1.click()

        # Проверка, что поле "Наименование владельца" отображается
        owner_name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/ngb-modal-window/div/div/app-table-editor/div[2]/ng-component/div/div/div[2]/input'))
        )
        assert owner_name_field.is_displayed(), "Поле 'Наименование владельца' не отображается"

        # Проверка, что поля для индивидуального предпринимателя скрыты
        try:
            WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/ngb-modal-window/div/div/app-table-editor/div[2]/ng-component/div/div/div[2]/app-arm-doc-view-fio/div/div[1]'))
            )
            raise AssertionError("Поле 'Фамилия' отображается, хотя не должно")
        except TimeoutException:
            logger.info("Поле 'Фамилия' скрыто, как и ожидалось.")

        # Выбор значения "3" (индивидуальный предприниматель)
        owner_type_dropdown.click()

        # Выбор значения "3" из выпадающего списка
        option_3 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="ng-dropdown-panel-items scroll-host"]//div[contains(text(), "3")]'))
        )
        option_3.click()

        # Проверка, что поле "Наименование владельца" скрыто
        try:
            WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/ngb-modal-window/div/div/app-table-editor/div[2]/ng-component/div/div/div[2]/input'))
            )
            raise AssertionError("Поле 'Наименование владельца' отображается, хотя не должно")
        except TimeoutException:
            logger.info("Поле 'Наименование владельца' скрыто, как и ожидалось.")

        # Проверка, что поля для индивидуального предпринимателя отображаются
        ip_fields = [
            ('/html/body/ngb-modal-window/div/div/app-table-editor/div[2]/ng-component/div/div/div[2]/app-arm-doc-view-fio/div/div[1]', "Фамилия"),
            ('/html/body/ngb-modal-window/div/div/app-table-editor/div[2]/ng-component/div/div/div[2]/app-arm-doc-view-fio/div/div[2]', "Имя"),
            ('/html/body/ngb-modal-window/div/div/app-table-editor/div[2]/ng-component/div/div/div[2]/app-arm-doc-view-fio/div/div[3]', "Отчество"),
            ('/html/body/ngb-modal-window/div/div/app-table-editor/div[2]/ng-component/div/div/div[4]/div[2]', "Дата рождения"),
        ]

        for xpath, field_name in ip_fields:
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                assert element.is_displayed(), f"Поле '{field_name}' не отображается"
                assert element.is_enabled(), f"Поле '{field_name}' не активно"
            except TimeoutException:
                logger.error(f"Поле '{field_name}' не найдено.")
                driver.save_screenshot(f"{field_name}_error.png")
                raise

        print("Все проверки прошли успешно!")

    finally:
        # Закрытие браузера
        driver.quit()