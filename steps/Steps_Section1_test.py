from pytest_bdd import scenarios, given, when, then
from service.HomePageService import HomePageService
from service.HomePageTestService import HomePageTestService
from service.ProductPageService import ProductPageService
from service.ProductPageTestService import ProductPageTestService
from service.ShopPageService import ShopPageService

scenarios('../features/section1_HomePage.feature')

@given('el usuario esta en la home page de practice.automationtesting')
def homePage():
    HomePageService().navegarWebTesting()

@given('clic on Shop Menu')
def clicOnShopMenu():
    HomePageService().clickBtnShopMenu()

@when('click on Home menu button')
def clickOnHomeMenuButton():
    ShopPageService().clickBtnHomeMenu()

@then('the Home page has Three Sliders only')
def verifyThreeSlidersOnly():
    HomePageTestService().TestResultSliderInHomePage()

@then('the Home page has Three Arrivals only')
def theHomePageHasThreeArrivalsOnly():
    HomePageTestService().TestResultArrivalsInHomePage()

@then('click the image in the Arrivals')
def clicFistImageInTheArrivals():
    HomePageService().clickFistImgArrivals()

@then("navigating to next page where the user can add that book into his basket")
def navigatingToProductPageAndViewBtnAddToCart():
    ProductPageTestService().testResultPageProductAndBtnAddToCart()

@then("click on Description tab for the book you clicked on")
def clickOnDescriptionTabForTheBook():
    ProductPageService().clickOnTabDescription()

@then("there should be a description regarding that book the user clicked on")
def verifyTextInDescriptionThatBookTheUserClickedOn():
    ProductPageTestService().verifyTextInDescription()

@then("click on Reviews tab for the book you clicked on")
def clickOnReviewsTabForTheBook():
    ProductPageService().clickOnTabReviews()

@then("there should be a Reviews regarding that book the user clicked on")
def verifyTextReviewsRegardingThatBookTheUserClickedOn():
    ProductPageTestService().verifyTextInReviews()


def teardown():
    ProductPageTestService().closeBrowser()
