from core.ui.WebUIElement import WebUIElement as UIElement
from core.ui.By import By


BTN_SHOPMENU_XPATH = UIElement(By.XPATH, "//ul[@id='main-nav']/li/a[.='Shop']")
BTN_MY_ACCOUNT_XPATH = UIElement(By.XPATH, "//ul[@id='main-nav']/li/a[.='My Account']")

DIV_SLIDER_XPATH = UIElement(By.XPATH, "//div[@class='n2-ss-slider-3']")
DIV_IMG_SLIDER_XPATH = UIElement(By.XPATH, "//*[@id='n2-ss-6']/div[1]/div/div/div/div/img")

DIV_ARRIVAL_XPATH = UIElement(By.XPATH, "//div[@class='themify_builder_sub_row clearfix gutter-default   sub_row_1-0-2']")
DIV_IMG_ARRIVAL_XPATH = UIElement(By.XPATH, "//div[@class='themify_builder_sub_row clearfix gutter-default   sub_row_1-0-2']//img")
DIV_FISRT_IMG_ARRIVAL_XPATH = UIElement(By.XPATH, "//*[@id='text-22-sub_row_1-0-2-0-0']/div/ul/li[1]")

