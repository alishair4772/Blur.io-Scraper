import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class MemeLand:
    def launch_chrome(self):
        print("LAUNCHING CHROME")
        options = Options()
        options.add_extension("metamask.crx")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
        self.driver.implicitly_wait(60)

    def login_metamask(self,phrase,password):
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        import_wallet = self.driver.find_element(By.XPATH,'//button[@class="button btn--rounded btn-secondary"]')
        import_wallet.click()

        i_agree = self.driver.find_element(By.XPATH,'//button[@class="button btn--rounded btn-primary btn--large"]')
        i_agree.click()

        paste_seed_phrase = self.driver.find_elements(By.XPATH,'//input[@type="password"]')
        for i in range(0,12):
            paste_seed_phrase[i].send_keys(phrase[i])

        confirm_phrase = self.driver.find_element(By.XPATH,'//button[@class="button btn--rounded btn-primary btn--large import-srp__confirm-button"]')
        confirm_phrase.click()

        type_password = self.driver.find_elements(By.XPATH,'//input[@type="password"]')
        for p in type_password:
            p.send_keys(password)

        checkbox = self.driver.find_element(By.XPATH,'//input[@class="check-box far fa-square"]')
        checkbox.click()

        import_wallet = self.driver.find_element(By.XPATH,'//button[@class="button btn--rounded btn-primary btn--large create-password__form--submit-button"]')
        import_wallet.click()

        got_it = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="button btn--rounded btn-primary btn--large"]')))
        got_it.click()

        next = self.driver.find_element(By.XPATH,'//button[@class="button btn--rounded btn-primary"]')
        next.click()

        done = self.driver.find_element(By.XPATH,'(//button[contains(text(),Done)])[last()]')
        done.click()

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(3)

        original_window = self.driver.current_window_handle

        self.driver.get("https://blur.io/asset/0x769272677fab02575e84945f03eca517acc544cc/1")
        wait = WebDriverWait(self.driver,10)
        sign_in_metamask = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(text(),'connect wallet')]")))
        sign_in_metamask.click()
        connect_metamask = self.driver.find_element(By.XPATH,'//button[@id="METAMASK"]')
        connect_metamask.click()

        wait.until(EC.number_of_windows_to_be(2))

        # Loop through until we find a new window handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

        next_btn = self.driver.find_element(By.XPATH,'//button[@class="button btn--rounded btn-primary"]')
        next_btn.click()

        connect_btn = self.driver.find_element(By.XPATH,'//button[@class="button btn--rounded btn-primary page-container__footer-button"]')
        connect_btn.click()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)

        wait.until(EC.number_of_windows_to_be(2))

        # Loop through until we find a new window handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        sign_btn = self.driver.find_element(By.XPATH,'//button[@class="button btn--rounded btn-primary btn--large request-signature__footer__sign-button"]')
        self.driver.execute_script("arguments[0].click();", sign_btn)

        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0])




    def quit_browser(self):
        print("QUITING BROWSER")
        self.driver.quit()
    def generate_urls(self):
        urls = []
        for i in range(1,9999):
            urls.append(f"https://www.memeland.com/profile/captainz/{i}")
        return urls

    def generate_urls_txt(self):
        txt = open('ids.txt')
        urls = []
        line = txt.readline()
        split = line.split(',')
        for id in split:
            urls.append(f"https://www.memeland.com/profile/captainz/{id}")
        return urls

    def scrape(self,data):
        time.sleep(0.5)
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//p[@class="chakra-text css-5wdnqf"]')))
        except:
            pass
        unrevealed = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'(//div[@class="css-8884ms"]/div/div/div[2]/p)[1]')))
        data['Unrevealed'].append(unrevealed.text)
        special = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'(//div[@class="css-8884ms"]/div/div/div[2]/p)[2]')))
        data['Special'].append(special.text)
        extraordinary = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'(//div[@class="css-8884ms"]/div/div/div[2]/p)[3]')))
        data['Extraordinary'].append(extraordinary.text)
        magical = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'(//div[@class="css-8884ms"]/div/div/div[2]/p)[4]')))
        data['Magical'].append(magical.text)
        epic = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'(//div[@class="css-8884ms"]/div/div/div[2]/p)[5]')))
        data['Epic'].append(epic.text)
        mythical = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'(//div[@class="css-8884ms"]/div/div/div[2]/p)[6]')))
        data['Mythical'].append(mythical.text)
        total_maps = int(unrevealed.text)+int(special.text)+int(extraordinary.text)+int(magical.text)+int(epic.text)+int(mythical.text)
        data['Total Mapz'].append(total_maps)

        # data['link'].append(self.driver.current_url)

        questing = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'(//p[@class="chakra-text css-5wdnqf"])[1]'))).get_attribute('innerHTML')
        data['questing'].append(questing)

        id_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//p[@class="chakra-text css-n26cv3"]')))

        split_id = id_element.text.split("#")
        id = split_id[1]
        data['Captainz ID'].append(id)
        if questing == 'No':
            url = "https://blur.io/asset/0x769272677fab02575e84945f03eca517acc544cc/" + id
            self.driver.get(url)
            price = self.driver.find_element(By.XPATH,'//div[@class="sc-iJKOTD bjwkli  cell index-0"]/div').text
            data['price'].append(price)

        else:
            data['price'].append('None')

    def get_url(self,url):
        print(f"GETTING URL: {url}")
        self.driver.get(url)


    def scrape_blur(self):
        action = ActionChains(self.driver)
        ids = []
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//button[@class="sc-dkPtRN ipExGR"]').click()
        total_listings_element = self.driver.find_element(By.XPATH,'//div[@class="sc-iqseJM sc-gIDmLj igmZuF ieLWJW"]/div[1]').text
        total_listings = int(total_listings_element)

        print(total_listings)
        while True:
            element = self.driver.find_element(By.XPATH,'(//div[@role="cell"]/div[2]/div)[last()]')
            action.move_to_element(element).perform()
            time.sleep(3)
            total = WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@role="cell"]/div[2]/div')))
            for i in total:
                ids.append(i.text)
            if len(ids) >= total_listings:
                break
            print(len(ids))
            print(total_listings)
        li = []
        for i in ids:
            li.append(i.split('#')[1])
        mylist = list(dict.fromkeys(li))
        print(len(mylist))
        print(mylist)


