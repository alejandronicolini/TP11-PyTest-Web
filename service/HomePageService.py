from core.steps.BaseSteps import BaseStep
from pages_constants import HomePageConstants


class HomePageService(BaseStep):

    def navegarWebTesting(self):
        self.goToUrl('https://practice.automationtesting.in')

    def clickBtnShopMenu(self):
        HomePageConstants.BTN_SHOPMENU_XPATH.click()

    def clickBtnMyAccountMenu(self):
        HomePageConstants.BTN_MY_ACCOUNT_XPATH.click()

    def clickFistImgArrivals(self):
        HomePageConstants.DIV_FISRT_IMG_ARRIVAL_XPATH.click(True)
