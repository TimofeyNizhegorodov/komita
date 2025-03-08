from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NavigationPage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_section(self):
        # Скролл до нужного раздела
        section = self.driver.find_element(By.XPATH, '//*[@id="nav"]/div/div[8]/div[1]/span')
        self.driver.execute_script("arguments[0].scrollIntoView();", section)

    def open_folder(self):
        # Открытие папки
        folder = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="nav"]/div/div[8]/div[2]/a[1]'))
        )
        folder.click()

class DocumentPage:
    def __init__(self, driver):
        self.driver = driver

    def select_document(self):
        # Выбор документа
        document = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mainblock"]/app-strateg5392u-draft-list/div/div[2]/div[2]/table/tbody/tr[1]/td[2]'))
        )
        document.click()