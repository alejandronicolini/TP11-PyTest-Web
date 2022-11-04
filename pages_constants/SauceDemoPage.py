from core.ui.WebUIElement import WebUIElement as UIElement
from core.ui.By import By


loginButton = UIElement(By.ID, 'login-button')
inputUserName = UIElement(By.ID, 'user-name')
inputPassword = UIElement(By.ID, 'password')
mensajePopUp = UIElement(By.XPATH, "//h3[@data-test='error']")

