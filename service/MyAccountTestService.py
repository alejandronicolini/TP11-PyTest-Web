from core.steps.BaseSteps import BaseStep
from core.ui.WebUIElement import WebUIElement as UIElement
from core.ui.By import By
from core.assertion.Assertion import Assertion
from pages_constants import MyAccountPageConstants
from service.MyAccountPageService import MyAccountPageService

from core.driver.WebDriver import WebDriver as Driver
from selenium.webdriver.support.ui import WebDriverWait


class MyAccountTestService(BaseStep):


    def loginExitoso(self, message):
        respuesta = MyAccountPageConstants.DIV_TEXT_LOGIN_MESSAGE_XPATH.getText()
        Assertion.assertTrue("el mensaje no coindice con la respuesta", message in respuesta)

    def loginFallido(self, message):
        respuestaMensaje = MyAccountPageConstants.DIV_TEXT_ERRORMESSAGE_XPATH.getText()
        Assertion.assertTrue("el mensaje no coindice con la respuesta", message == respuestaMensaje)

    def verifyVisibilityPassword(self):
        atributoType = MyAccountPageConstants.INPUT_LOGIN_PASSWORD_ID.getAttribute("type")
        Assertion.assertEquals('atributo invalido', 'password', atributoType)

    def registroExitoso(self):
        WebDriverWait(Driver, 1500)
        datoEmail = str(MyAccountPageService.mail_registro)
        lista = datoEmail.split("@")
        mensaje = lista[0]
        respuesta = UIElement(By.XPATH, "/html/body").getText()
        Assertion.assertTrue('Mensaje no encontrado', mensaje in respuesta)

    def verificarIrAHomePage(self):
        MyAccountPageService().clickBtnHomeMenu()
        WebDriverWait(Driver, 1500)
        BaseStep.verifyUrlContains(self, "https://practice.automationtesting.in/", "URl incorrecta")

    def registroFallido(self, mensaje):
        WebDriverWait(Driver, 150)
        respuesta_mensaje = MyAccountPageConstants.DIV_TEXT_ERRORMESSAGE_XPATH.getText()
        Assertion.assertEquals('la respuesta no coincide', mensaje, respuesta_mensaje)
