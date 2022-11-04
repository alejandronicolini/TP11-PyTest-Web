from core.steps.BaseSteps import BaseStep
from core.assertion.Assertion import Assertion
from pages_constants import ProductPageConstants

class ProductPageService(BaseStep):


    def clickOnTabDescription(self):
        ProductPageConstants.TAB_DESCRIPTION_XPATH.click()

    def clickOnTabReviews(self):
        ProductPageConstants.TAB_REVIEWS_XPATH.click()
