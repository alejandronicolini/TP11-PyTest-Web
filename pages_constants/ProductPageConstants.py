from core.ui.WebUIElement import WebUIElement as UIElement
from core.ui.By import By


BTN_ADD_TO_BASKET = UIElement(By.XPATH, "//button[@type='submit' and text()='Add to basket']")
TAB_DESCRIPTION_XPATH = UIElement(By.XPATH, "//a[.='Description']")

TITLE_DESCRIPTION_XPATH = UIElement(By.XPATH, "//*[@id='tab-description']/h2")
CONTENT_DESCRIPTION_XPATH = UIElement(By.XPATH, "//div[@id='tab-description']/p")

TAB_REVIEWS_XPATH = UIElement(By.XPATH, "//ul[@class='tabs wc-tabs']/li[2]/a")
TITLE_REVIEWS_XPATH = UIElement(By.XPATH, "//*[@id='comments']/h2")

SPAN_CARTCONTENT_XPATH = UIElement(By.XPATH, "//span[@class='cartcontents']")
SPAN_AMOUNT_XPATH = UIElement(By.XPATH, "//span[@class='amount']")
SPAN_BOOK_PRICE_XPATH = UIElement(By.XPATH, "//span[@class='woocommerce-Price-amount amount']")

P_STOCK_DISPONIBLE_XPATH = UIElement(By.XPATH, "//p[@class='stock in-stock']")
INPUT_QUANTITY_ADD_XPATH = UIElement(By.XPATH, "//input[@name='quantity']")
