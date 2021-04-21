from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
import unittest
from time import sleep
import pandas as pd

from page import HomePage, CategoryPage, ItemPage

exec_path = r"D:\portfolios\selenium\drivers\geckodriver.exe"

ignore_list = ["https://bikroy.com/en/jobs", "https://bikroy.com/en/ads/bangladesh/overseas-jobs"]
white_list = ["https://bikroy.com/en/ads/bangladesh/mobiles", "https://bikroy.com/en/ads/bangladesh/hobbies-sports-kids"]

class BikroyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=exec_path)
        self.driver.maximize_window()

    def testHomePage(self):
        startPage = HomePage(self.driver)

        cat_list = startPage.find_categories()
        cat_links = [cat.get_attribute('href') for cat in cat_list]
        print(f'Found {len(cat_links)} category links.')
        item_details = []
        # print(cat_links)

        categories = CategoryPage(self.driver)
        for link in cat_links:
            if link in ignore_list:
                continue
            if link not in white_list:
                continue
            print(f'Fetching: {link}')

            item_list, category_name = categories.get_item_list(link)
            item_links = [itm.get_attribute('href') for itm in item_list]
            # print(category_name)

            items = ItemPage(self.driver)
            link_count = 0
            for item_link in item_links:
                link_count += 1
                print(f'Fetching Link #{link_count}: {item_link}')
                itm_info = items.get_item_info(item_link)
                itm_info.append(category_name)
                itm_info.append(item_link)

                item_details.append(itm_info)
                sleep(3)
            sleep(5)

            item_details_df = pd.DataFrame(item_details, columns = ['Title', 'Price', 'Details', 'Features', 'Description', 'Category', 'Address'])
            print(item_details_df)

            item_details_df.to_csv('Item_details.csv', index=False)


    def tearDown(self):
        sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
