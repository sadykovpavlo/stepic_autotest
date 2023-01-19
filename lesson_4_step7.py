from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc_x(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = Chrome()
driver.get('http://suninjuly.github.io/explicit_wait2.html')

try:

    price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element(locator=(By.ID, 'price'), text_='100'
                                                                             ))
    book = driver.find_element(By.ID, 'book')
    book.click()

    x = driver.find_element(By.ID, 'input_value')
    y = calc_x(x.text)

    answer = driver.find_element(By.ID, 'answer')
    answer.send_keys(y)

    button = driver.find_element(By.ID, 'solve')
    button.click()

    # You will see answer at terminal
    alert = driver.switch_to.alert
    print(alert.text)


finally:
    driver.quit()
