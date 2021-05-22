from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import time

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")


link = "https://www.metric-conversions.org/"


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(10)
    yield browser
    browser.delete_all_cookies()
    browser.quit()

class TestConversionSite():
    def test_celsius_to_fahrenheit(self, browser):
        browser.get(link)
        temp_button = browser.find_element_by_css_selector("[title='Temperature Conversion']")
        temp_button.click()
        cels_button = browser.find_element_by_css_selector("[href='/temperature/celsius-conversion.htm']")
        cels_button.click()
        time.sleep(1)
        cels_to_far_button = browser.find_element_by_css_selector("[href='/temperature/celsius-to-fahrenheit.htm']")
        cels_to_far_button.click()
        time.sleep(1)
        conv_field = browser.find_element_by_css_selector("[placeholder~='°C']")
        conv_field.send_keys("40")
        result = browser.find_element_by_id("answer")
        temp = '104'
        res_text = result.text
        assert result.is_displayed(), "Result is not displayed"
        assert temp in res_text, "Convertion is not correct"
        


    def test_meters_to_feet(self, browser):
        browser.get(link)
        lenght_button = browser.find_element_by_css_selector("[title='Length Conversion']")
        lenght_button.click()
        time.sleep(1)
        meters_button = browser.find_element_by_css_selector("[href='/length/meters-conversion.htm']")
        meters_button.click()
        met_to_feet_button = browser.find_element_by_css_selector("[href='/length/meters-to-feet.htm']")
        met_to_feet_button.click()
        time.sleep(1)
        conv_field = browser.find_element_by_css_selector("[placeholder~='m']")
        conv_field.send_keys("10")
        result = browser.find_element_by_id("answer")
        lenght = '32'
        res_text = result.text
        assert result.is_displayed(), "Result is not displayed"
        assert lenght in res_text, "Convertion is not correct"




    def test_ounces_to_grams(self, browser):
        browser.get(link)
        weight_button = browser.find_element_by_css_selector("[title='Weight Conversion']")
        weight_button.click()
        time.sleep(1)
        ounce_button = browser.find_element_by_css_selector("[href='/weight/ounces-conversion.htm']")
        ounce_button.click()
        time.sleep(1)
        ounce_to_gr = browser.find_element_by_css_selector("[href='/weight/ounces-to-grams.htm']")
        ounce_to_gr.click()
        time.sleep(1)
        conv_field = browser.find_element_by_css_selector("[placeholder~='oz']")
        conv_field.send_keys("10")
        result = browser.find_element_by_id("answer")
        weight = '283'
        res_text = result.text
        assert result.is_displayed(), "Result is not displayed"
        assert weight in res_text, "Convertion is not correct"





       