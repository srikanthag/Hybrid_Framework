
class Login:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@class='button-1 login-button']"
    link_logout_link_text = "Logout"

    def __int__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.link_logout_link_text).click()

