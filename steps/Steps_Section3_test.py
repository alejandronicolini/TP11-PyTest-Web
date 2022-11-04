from pytest_bdd import scenarios, given, when, then
from service.HomePageService import HomePageService
from service.MyAccountPageService import MyAccountPageService
from service.MyAccountTestService import MyAccountTestService

scenarios('../features/section3_Registro.feature')

@given('el usuario esta en la home page de automationtesting.in')
def homePage():
    HomePageService().navegarWebTesting()

@given('clic on My Account Menu2')
def clicOnMyAccountMenu():
    HomePageService().clickBtnMyAccountMenu()

# @given("enter Email '{email}' in Email-Address textbox")
# def enterEmail(email):
#     MyAccountPageService().inputEmail(email)

@given("enter Email <email> in Email-Address textbox")
def enterEmail(email):
    MyAccountPageService().inputEmail(email)

@given("enter password <password> in password textbox")
def enterPassword(password):
    MyAccountPageService().inputRegPassword(password)

@then("user will be registered successfully message")
def SuccessfullyMessage():
    MyAccountTestService().registroExitoso()

@when("click on Register button")
def clickOnRegisterButton():
    MyAccountPageService().clickBtnRegister()

@then("will be navigated to the Home page")
def irAHomePage():
    MyAccountTestService().verificarIrAHomePage()

@then("Registration must fail with a warning message  <mensaje>")
def registrationErrorResponse(mensaje):
    MyAccountTestService().registroFallido(mensaje)

# def teardown():
#     MyAccountTestService().closeBrowser()
