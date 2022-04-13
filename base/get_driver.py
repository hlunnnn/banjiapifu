from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class GetDriver:
    driver = None

    @classmethod
    def get_driver(cls):
        # 配置
        ch_options = Options()
        ch_options.add_argument("--headless")  # => 为Chrome配置无头模式
        if cls.driver is None:
            # cls.driver = webdriver.Chrome(chrome_options=ch_options)
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
        return cls.driver


    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None

