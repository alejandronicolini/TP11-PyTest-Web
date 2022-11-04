from core.steps.BaseSteps import BaseStep
from core.assertion.Assertion import Assertion
from pages_constants import ProductPageConstants

class ProductPageTestService(BaseStep):


    def testResultPageProductAndBtnAddToCart(self):
        urlPage = BaseStep.getUrl(self)
        urlProductos = 'https://practice.automationtesting.in/product' in urlPage
        Assertion.assertTrue('Url incorrecta', urlProductos)
        Assertion.assertTrue('el Boton Add To Basket no esta presente', ProductPageConstants.BTN_ADD_TO_BASKET.isPresent())

    def verifyTextInDescription(self):
        titleDescription = ProductPageConstants.TITLE_DESCRIPTION_XPATH.getText()
        Assertion.assertTrue('titulo incorrecto', titleDescription == 'Product Description')

    def verifyTextInReviews(self):
        titleReviews = ProductPageConstants.TITLE_REVIEWS_XPATH.getText()
        Assertion.assertEquals('Titulo incorrecto', 'Reviews', titleReviews);
