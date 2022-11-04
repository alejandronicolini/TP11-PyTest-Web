from pytest_bdd import scenarios, given, when, then
from service.SauceDemoService import SauceDemoService

scenarios('../features/LoginSauceDemo.feature')

@given("Se encuentra en la pagina de Login")
def navigateToHome():
    SauceDemoService().goToHome()

@when('Ingresa el usuario con <username>')
def setUserName(username):
    SauceDemoService().inputUserName(username)

@when('Ingresa la password con <password>')
def setPassword(password):
    SauceDemoService().inputPassword(password)

@when("Clic en el boton login")
def clicBtnLogin():
    SauceDemoService().clicBtnLogin()

@then("Aparece el home correctamente")
def step_impl():
    SauceDemoService().verifyRedirect()

@then('Aparece el mensaje <errorMensaje>')
def mensajeError(errorMensaje):
    SauceDemoService().verifyMessage(errorMensaje)

def teardown():
    SauceDemoService().closeBrowser()
