from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from win10toast import ToastNotifier
import time

toast = ToastNotifier()


timer = 10
driver = webdriver.Chrome(executable_path=r'C:\Users\hp\Desktop\proj\chromedriver.exe')

def ref():
    url = 'https://ru.investing.com/currencies/usd-kzt'
    options = Options()
    options.add_argument("--headless")
    driver.get(url)
    currency = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div/div/div[2]/main/div/div[1]/div[2]/div[1]/span').text
    difference = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div/div/div[2]/main/div/div[1]/div[2]/div[1]/div[2]/span[1]').text
    named_tuple = time.localtime()  # получить struct_time
    time_string = time.strftime("%m/%d, %H:%M:%S", named_tuple)
    f = open('log.txt', mode='a')
    f.write(f"Разность курса {difference}, Доллар стоит {currency} тенге -- {time_string}" + "\n" )
    f.close()
    toast.show_toast(
        "Обновление курса",
        f"Изменение курса {difference}, курс составляет {currency}",
        duration=10,
        icon_path="icon.ico",
        threaded=True,
    )

while True:
    if time.sleep(timer) != True:
        ref()

