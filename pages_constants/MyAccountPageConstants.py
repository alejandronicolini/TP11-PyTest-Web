from core.ui.WebUIElement import WebUIElement as UIElement
from core.ui.By import By


INPUT_EMAIL_ID = UIElement(By.ID, 'reg_email')
INPUT_REG_PASSWORD_ID = UIElement(By.ID, 'reg_password')
BTN_REGISTER_XPATH = UIElement(By.XPATH, "//input[@name='register']")

INPUT_USER_NAME_ID = UIElement(By.ID, 'username')
INPUT_LOGIN_PASSWORD_ID = UIElement(By.ID, 'password')
BTN_LOGIN_XPATH = UIElement(By.XPATH, "//input[@name='login']")
DIV_TEXT_LOGIN_MESSAGE_XPATH = UIElement(By.XPATH, "//div[@class='woocommerce-MyAccount-content']/p[1]")

BTN_HOMEMENU_XPATH = UIElement(By.XPATH, "//div[@id='site-logo']/a/img[@title='Automation Practice Site']")

DIV_TEXT_ERROR_XPATH = UIElement(By.XPATH, "//ul[@class='woocommerce-error']//strong[.='Error:']")
DIV_TEXT_ERRORMESSAGE_XPATH = UIElement(By.XPATH, "//ul[@class='woocommerce-error']/li")
