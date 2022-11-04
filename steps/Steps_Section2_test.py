from pytest_bdd import scenarios, given, when, then, parsers
from service.HomePageService import HomePageService
from service.MyAccountPageService import MyAccountPageService
from service.MyAccountTestService import MyAccountTestService

scenarios('../features/section2_Login.feature')

@given("el usuario esta en la home page de practice.automationtesting.in")
def homePage():
    HomePageService().navegarWebTesting()

@given('clic on My Account Menu')
def clicOnMyAccountMenu():
    HomePageService().clickBtnMyAccountMenu()

@given(parsers.parse('enter username {username} in username textbox1'))
def enterUsername(username):
    MyAccountPageService().inputUserName(username)

@given(parsers.parse("enter password {password} in password textbox login1"))
def enterPasswordLogin(password):
    MyAccountPageService().inputLoginPassword(password)

@then(parsers.parse('user must successfully login to the web page, message: {message}'))
def SuccessfullyLoginMessage(message):
    MyAccountTestService().loginExitoso(message)

@given('enter username <username> in username textbox')
def enterUsername(username):
    MyAccountPageService().inputUserName(username)

@given("enter password <password> in password textbox login")
def enterPasswordLogin(password):
    MyAccountPageService().inputLoginPassword(password)

@when('click on login button')
def clickOnLoginButton():
    MyAccountPageService().clicBtnLogin()

@then('Proper error must be displayed <message> and prompt to enter login again')
def loginErrorResponse(message):
    MyAccountTestService().loginFallido(message)

@when('enter the password field with some characters.')
def inputSomeCharacterInThePasswordField():
    MyAccountPageService().inputLoginPassword("contraseña")

@when("the password field should display the characters in asterisks")
def passwordFieldWithAsterisks():
    MyAccountTestService().verifyVisibilityPassword()

def teardown():
    MyAccountTestService().closeBrowser()
