from core.steps.BaseSteps import BaseStep
from core.assertion.Assertion import Assertion
from pages_constants import HomePageConstants

from core.ui.WebUIElement import WebUIElement


class HomePageTestService(BaseStep):

    def clicBtnLogin(self):
        HomePageConstants.loginButton.click()

    def TestResultSliderInHomePage(self):
        listado = WebUIElement.getElementsList(HomePageConstants.DIV_IMG_SLIDER_XPATH)
        Assertion.assertEquals("no coinciden las cantidad de elementos encontrados",3, len(listado))

    def TestResultArrivalsInHomePage(self):
        listado = WebUIElement.getElementsList(HomePageConstants.DIV_IMG_ARRIVAL_XPATH)
        Assertion.assertEquals("no coinciden las cantidad de elementos encontrados", 3, len(listado))
