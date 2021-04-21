from selenium.webdriver.common.by import By

class Locators():
    category_list_locator = (By.CSS_SELECTOR, "a.t-bold")
    items_locator = (By.XPATH, "//ul[@class='list--3NxGO']/li/a")
    category_name_locator = (By.XPATH, "//div[contains(@class, 'category')]//div[contains(@class, 'ellipsis')]")

    itm_title_locator = (By.XPATH, "//div[contains(@class, 'main-section')]//h1[contains(@class, 'title')]")
    itm_title_err_locator = (By.XPATH, "//div[contains(@class, 'main-section')]//h2")
    itm_price_locator = (By.XPATH, "//div[contains(@class, 'left-section')]//div[contains(@class, 'price')]")
    itm_meta_locator = (By.XPATH, "//div[contains(@class, 'left-section')]//div[contains(@class, 'ad-meta')]")
    itm_features_locator = (By.XPATH, "//div[contains(@class, 'left-section')]//div[contains(@class, 'features')]")
    itm_desc_locator = (By.XPATH, "//div[contains(@class, 'left-section')]//div[contains(@class, 'expandable')]//div[contains(@class, 'description')]")
