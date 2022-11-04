#from pages_constants import SauceDemoPage as page
from pages_constants.SauceDemoPage import *
from core.steps.BaseSteps import BaseStep
from core.assertion.Assertion import Assertion


class SauceDemoService(BaseStep):

    def goToHome(self):
        self.goToUrl("https://www.saucedemo.com/")

    def inputUserName(self, username):
        inputUserName.setText(username)

    def inputPassword(self, password):
        inputPassword.setText(password)

    def clicBtnLogin(self):
        loginButton.click()

    def verifyRedirect(self):
        url_acceso = self.getUrl()
        print("Esto es lo que viene: " + url_acceso)
        url_esperada = "https://www.saucedemo.com/inventory.html"
        Assertion.assertEquals("las url no concuerdan", url_esperada, url_acceso)

    def verifyMessage(self, mensaje):
        mensajeRecibido = mensajePopUp.getText()
        Assertion.assertEquals("el mensaje recibido no es el correcto", mensaje, mensajeRecibido)

