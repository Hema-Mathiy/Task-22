from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class Guvi_insta:

    def __init__(self, url):
        self.url = url
        # Initialize the Chrome WebDriver
        driver_path = r"C:\Users\Asus\AppData\Local\Google\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.actions = ActionChains(self.driver)
        # Maximize the window and navigate to the given url
        self.driver.maximize_window()
        self.driver.get(self.url)

    def logging(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            print(f"Opened the insta webpage of guviofficial")

            followers = wait.until(EC.presence_of_element_located((By.XPATH,"(//button[@type='button'])[3]/span/span")))
            followings = wait.until(EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[4]/span/span")))

            # Extract text content from webpage
            followers_count = followers.text
            followings_count = followings.text
            
            # Printing the value of follower and followings
            print(f"No. of followers is {followers_count}")
            print(f"No. of followings is {followings_count}")
            sleep(5)
        except NoSuchElementException as selenium_error:
            print(selenium_error)
            
        finally :
            self.driver.quit()


url = "https://www.instagram.com/guviofficial/"
G = Guvi_insta(url)
G.logging()