from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

driver = webdriver.Chrome(webdriver.ChromeOptions())
driver.get("https://linkedin.com")
time.sleep(2)

# ********** LOG IN *************

username = driver.find_element(By.XPATH, "//input[@name='session_key']")
password = driver.find_element(By.XPATH, "//input[@name='session_password']")

username.send_keys('enteryourusername')
password.send_keys('enteryourpassword')
time.sleep(2)

submit = driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)

n_pages = 3

for n in range(1, n_pages + 1):

    driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH&page=" + str(n))
    time.sleep(2)

    all_buttons = driver.find_elements(By.TAG_NAME, "button")
    message_buttons = [btn for btn in all_buttons if btn.text == "Message"]

    for i in range(6, 7):
        # click on "Message" button
        driver.execute_script("arguments[0].click();", message_buttons[i])
        time.sleep(2)

        # activate main div
        main_div = driver.find_element(By.XPATH, "//div[starts-with(@class, 'msg-form__msg-content-container')]")
        driver.execute_script("arguments[0].click();", main_div)

        # type message
        paragraphs = driver.find_elements(By.TAG_NAME, "p")

        all_span = driver.find_elements(By.TAG_NAME, "span")
        all_span = [s for s in all_span if s.get_attribute("aria-hidden") == "true"]

        idx = [*range(3, 23, 2)]
        greetings = ["Hello", "Hi", "Hey"]
        all_names = []

        for j in idx:
            name = all_span[j].text.split(" ")[0]
            all_names.append(name)

        greetings_idx = random.randint(0, len(greetings) - 1)
        message = greetings[greetings_idx] + " " + all_names[i] + ", Happy to connect with you :)"

        paragraphs[-5].send_keys(message)
        time.sleep(2)

        # send message
        submit = driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

        # close div
        close_button = driver.find_elements(By.XPATH,"//button[starts-with(@data-control-name, 'overlay.close_conversation_window')]")
        driver.execute_script("arguments[0].click();", close_button)
        time.sleep(2)


