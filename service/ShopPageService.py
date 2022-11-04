from core.steps.BaseSteps import BaseStep
from pages_constants.ShopPageConstants import *


class ShopPageService(BaseStep):

    def clickBtnHomeMenu(self):
        BTN_HOMEMENU_XPATH.click()
