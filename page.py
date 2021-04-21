from selenium.common.exceptions import NoSuchElementException

from locators import Locators

class HomePage():
    def __init__(self, driver, base_url = "https://bikroy.com/en"):
        self.driver = driver
        self.driver.get(base_url)
        assert "Bikroy.com" in self.driver.title

    def find_categories(self):
        categories = self.driver.find_elements(*Locators.category_list_locator)
        return categories

class CategoryPage():
    def __init__(self, driver):
        self.driver = driver

    def get_item_list(self, link):
        self.driver.get(link)
        itm_list = self.driver.find_elements(*Locators.items_locator)
        category_name = self.driver.find_element(*Locators.category_name_locator).text
        return itm_list, category_name

class ItemPage():
    def __init__(self, driver):
        self.driver = driver

    def get_item_info(self, item_link):
        self.driver.get(item_link)

        try:
            itm_title = self.driver.find_element(*Locators.itm_title_locator).text
        except NoSuchElementException:
            itm_title = self.driver.find_element(*Locators.itm_title_err_locator).text
            print(f'ERROR: {itm_title}')
            return
        try:
            itm_price = self.driver.find_element(*Locators.itm_price_locator).text
        except NoSuchElementException:
            print('Price Not Provided')
            itm_price = 'Not Found'

        itm_meta = self.driver.find_element(*Locators.itm_meta_locator).text

        try:
            itm_features = self.driver.find_element(*Locators.itm_features_locator).text
        except NoSuchElementException:
            print('Features Not Provided')
            itm_features = 'Not Found'
        itm_desc = self.driver.find_element(*Locators.itm_desc_locator).text

        return [itm_title, itm_price, itm_meta, itm_features, itm_desc]
