from Page_Objects.Login_Page import Login
from Utilities.readProperties import ReadConfig

class Test_001_Login:
    baseURL = ReadConfig.get_Application_URL()
    username = ReadConfig.get_Username()
    password = ReadConfig.get_Password()

    def get_homepage_title(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        title = self.driver.title
        self.driver.close()
        if title == "Your store. Login":
            self.driver.close()
            assert True
        else:
            self.driver.savescreenshot(".\\Screenshots\\"+"homepage_title.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.Lp = Login()
        self.Lp.set_username(self.username)
        self.Lp.set_password(self.password)
        self.Lp.click_login()
        title2 = self.driver.title
        self.driver.close()
        if title2 == "Dashboard / nopCommerce administration":
             assert True
        else:
            assert False






