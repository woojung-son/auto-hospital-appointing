from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
#import wait

def no_ssl_bypass(_driver) :
    chrome_no_ssl = "연결이 비공개로 설정되어 있지 않습니다."
    
    #if no_ssl_detail_button :

    if chrome_no_ssl in driver.page_source :
        print('no_ssl page handling ...')
        no_ssl_link = _driver.find_element_by_id('proceed-link')
        no_ssl_detail_button = _driver.find_element_by_id('details-button')

        no_ssl_detail_button.click()
        no_ssl_link.click()
        WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.CSS_SELECTOR, 'div.header.container-fluid > div.float-left > h1 > a > div'))
    else :
        print("Bypassed page loaded")
# abcdefghijklmnopqrstuvwxyz
# abcdefghijklmnopqrstuvwxyz
# abcdefghijklmnopqrstuvwxyz
# abcdefghijklmnopqrstuvwxyz
# abcdef

def login(_driver) :
    return

def lottery() :
    return

if __name__ == "__main__":
    #driver = webdriver.PhantomJS('C:/dev_python/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    #driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')
    driver = webdriver.Chrome('./chromedriver_v86/chromedriver.exe')
    driver.implicitly_wait(1)
    # driver = webdriver.PhantomJS('/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs')
    driver.get("http://**.or.kr/")
    #driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
    #driver.find_element(By.CSS_SELECTOR, "#btn_login_text").click()
    #driver.find_element_by_name('user_id').send_keys('agequodagis')
    #driver.find_element_by_name('password').send_keys('fw4545')

    no_ssl_bypass(driver)

    # Login
    driver.find_element(By.CSS_SELECTOR, 'body > header > div.header.container-fluid > div.float-right > a.btn_secondary_round.btn_header_login').click()
    driver.find_element(By.CSS_SELECTOR, '#loginForm > fieldset > input[type=text]:nth-child(1)').send_keys("agequodagis")
    driver.find_element(By.CSS_SELECTOR, '#loginForm > fieldset > input[type=password]:nth-child(2)').send_keys("fw4545")
    driver.find_element(By.CSS_SELECTOR, '#loginForm > fieldset > div.social > input').click()

    # Lottery Page & Handling alert Window
    while True :
        driver.get("https://**.or.kr/page_jEDe97")
        no_ssl_bypass(driver)
        #print(driver.page_source)

        lottery_iframe = driver.find_element(By.CSS_SELECTOR, "#mainFrame") # Store iframe web element

        driver.switch_to.frame(lottery_iframe) # switch to selected iframe

        lottery_chance_count = driver.find_element(By.CSS_SELECTOR, "#popHeader > div.lotte_body > div.lotte_point > table > tbody > tr:nth-child(3) > td.title")
        if lottery_chance_count : 
            print("lottery_chance_count.text[0] : ", lottery_chance_count.text[0])
            if int(lottery_chance_count.text[0]) >= 3 :
                print("Exceed today's maximum chance")
                break
            else :
                driver.find_element(By.CSS_SELECTOR, '#number > a').click() # "복권 구입" button

                #alert = wait.until(wait.expected_conditions.alert_is_present())
                #wait.until(expected_conditions.alert_is_present()) # Wait for the alert to be displayed

                alert = driver.switch_to.alert 
                text = alert.text # Store the alert text in a variable
                print("1st alert text : ", text)
                alert.accept()
                
                driver.find_element(By.CSS_SELECTOR, '#popHeader > div.lotte_body > div:nth-child(5) > div:nth-child(2) > a:nth-child(3)').click()
                alert = driver.switch_to.alert
                text = alert.text # Store the alert text in a variable
                print("2nd alert text : ", text)
                alert.accept()


#driver.switch_to.default_content()

#driver.close()
