import time, string, os
from twocaptcha import TwoCaptcha
from random import *
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Generator():
    letters = string.ascii_letters + string.digits
    return ''.join(choice(letters) for i in range(randint(15, 25)))

def solveRecaptcha(sitekey, url):
    api_key = os.getenv('APIKEY_2CAPTCHA', '9e646e89775a494f20423509239c9850')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(
            sitekey=sitekey,
            url=url)

    except Exception as e:
        print(e)

    else:
        return result

def Creator():
    driver = webdriver.Chrome()
    driver.get('https://www.spotify.com/be-nl/signup')

    try:

        try:
            cookie_consent_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookie_consent_button.click()
        except:
            pass

        driver.find_element(By.ID, 'email').send_keys(Generator() + '@gmail.com')
        driver.find_element(By.ID, 'password').send_keys(Generator() + 'aA@')
        driver.find_element(By.ID, 'displayname').send_keys('Andrew')
        driver.find_element(By.ID, 'day').send_keys('12')
        driver.find_element(By.ID, 'year').send_keys('1999')
        Select(driver.find_element(By.ID, 'month')).select_by_index(1)
        driver.find_element(By.CSS_SELECTOR, "label[for='gender_option_male']").click()
        driver.find_element(By.CSS_SELECTOR, "label[for='third-party-checkbox']").click()
        driver.find_element(By.CSS_SELECTOR, "button[data-encore-id='buttonPrimary']").click()

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'g-recaptcha-response'))
            )

            result = solveRecaptcha(
                "6LeO36obAAAAALSBZrY6RYM1hcAY7RLvpDDcJLy3",
                driver.current_url
            )
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
        driver.close()
        Creator()


if __name__ == '__main__':
    for _ in range(100):
        Creator()

