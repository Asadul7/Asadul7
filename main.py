import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()

total_url = []

while True:
    driver.get("https://www.tiktok.com/")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    profile_url = driver.find_elements("xpath", '//a[@class="tiktok-1lqhxf7-StyledAuthorAnchor emt6k1z1"]')
    for url in profile_url:
        link_url = url.get_attribute("href")
        if link_url not in total_url:
            total_url.append(link_url)
            print(total_url)
