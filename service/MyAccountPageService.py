from core.steps.BaseSteps import BaseStep
from core.ui.WebUIElement import WebUIElement as UIElement
from core.ui.By import By
from pages_constants import MyAccountPageConstants


class MyAccountPageService(BaseStep):
    mail_registro = ""

    def inputUserName(self, username):
        MyAccountPageConstants.INPUT_USER_NAME_ID.click()
        MyAccountPageConstants.INPUT_USER_NAME_ID.setText(username)

    def inputLoginPassword(self, password):
        MyAccountPageConstants.INPUT_LOGIN_PASSWORD_ID.click()
        MyAccountPageConstants.INPUT_LOGIN_PASSWORD_ID.setText(password)

    def clicBtnLogin(self):
        MyAccountPageConstants.BTN_LOGIN_XPATH.click()

    def inputEmail(self, email):
        MyAccountPageConstants.INPUT_EMAIL_ID.click()
        MyAccountPageConstants.INPUT_EMAIL_ID.setText(email)
        self.mail_registro = email

    def inputRegPassword(self, password):
        MyAccountPageConstants.INPUT_REG_PASSWORD_ID.click()
        MyAccountPageConstants.INPUT_REG_PASSWORD_ID.setText(password)

    def clickBtnRegister(self):
        #clic auxiliar previo, para hacer visilble el boton Register
        clicAuxiliar = UIElement(By.XPATH, "//p[@class='woocomerce-FormRow form-row']")
        clicAuxiliar.click()
        MyAccountPageConstants.BTN_REGISTER_XPATH.click()

    def clickBtnHomeMenu(self):
        MyAccountPageConstants.BTN_HOMEMENU_XPATH.click()


