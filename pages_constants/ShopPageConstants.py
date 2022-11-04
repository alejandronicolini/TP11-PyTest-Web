from core.ui.WebUIElement import WebUIElement as UIElement
from core.ui.By import By


BTN_HOMEMENU_XPATH = UIElement(By.XPATH, "//div[@id='site-logo']/a/img[@title='Automation Practice Site']")

SLIDER_FILTER_PRICE_XPATH = UIElement(By.XPATH, "//div[@class='ui-slider-range ui-corner-all ui-widget-header']")
SLIDER_CIRCLE_PRICE_MINIMO_XPATH = UIElement(By.XPATH, "//div[@class='price_slider ui-slider ui-corner-all ui-slider-horizontal ui-widget ui-widget-content']/span[1]")
SLIDER_CIRCLE_PRICE_MAXIMO_XPATH = UIElement(By.XPATH, "//div[@class='price_slider ui-slider ui-corner-all ui-slider-horizontal ui-widget ui-widget-content']/span[2]")

BTN_FILTER_By_PRICE_XPATH = UIElement(By.XPATH, "//div[@class='price_slider_amount']//button[@class='button']")

SPAN_PRICE_CON_DESCUENTO_XPATH = UIElement(By.XPATH, "//ins/span[@class=\"woocommerce-Price-amount amount\"]")
SPAN_PRICE_ORIGINAL_XPATH = UIElement(By.XPATH, "//*[@id='content']/ul/li/a/span/span")

FIRST_ELEMENT_CATEGORY_XPATH = UIElement(By.XPATH, "//ul[@class='product-categories']/li[1]/a")
DROPDOWN_SORT_XPATH = UIElement(By.XPATH, "//select[@name='orderby']")
