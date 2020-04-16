#!env/bin/python
# -*- coding: utf-8 -*-

import time
import random
import string
from threading import Thread
from selenium import webdriver


def generate_data():
    amount = 10
    letters = string.ascii_lowercase + string.digits
    login = ''.join(random.sample(letters, amount))
    password = ''.join(random.sample(letters, amount))
    return login, password


def main(data):
    driver = webdriver.Firefox()
    driver.get('https://rt.pornhub.com/event/login?promo=free_global')
    time.sleep(3)

    username = driver.find_element_by_css_selector('#username')
    username.send_keys(data[0])

    password = driver.find_element_by_css_selector('#password')
    password.send_keys(data[1])

    email = driver.find_element_by_css_selector('#email')
    email.send_keys(data[0] + '@gmail.com')

    submit = driver.find_element_by_css_selector('#submitNewAccount')
    submit.click()
    submit.click()

    with open('accounts.txt', 'a') as f:
        f.write(data[0] + ':' + data[1] + '\n')

    time.sleep(5)
    driver.quit()


def create_thread(amount):
    for t in range(amount):
        t = Thread(target=main, args=(generate_data(),))
        t.start()
        t.join()


if __name__ in '__main__':
    create_thread(amount=int(input('Введите количество потоков: ')))
