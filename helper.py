from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from multipledispatch import dispatch


class AutoHelper:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 30, poll_frequency=1)

    ''' Click action '''

    @dispatch(WebElement)
    def click_on(self, locator):
        locator.click()

    @dispatch(tuple)
    def click_on(self, locator):
        self.wait_element_to_be_clickable(*locator)
        self.driver.find_element(*locator).click()

    @dispatch(str, str)
    def click_on(self, method, locator):
        self.wait_element_to_be_clickable(method, locator)
        self.driver.find_element(method, locator).click()

    def double_click_on_element(self, type, locator):
        self.wait_element_to_be_clickable(type, locator)
        mouse_tracker = self.driver.find_element(type, locator)
        self.action.double_click(mouse_tracker).perform()

    def right_click_on(self, type, locator):
        self.wait_element_to_be_clickable(type, locator)
        mouse_tracker = self.driver.find_element(type, locator)
        self.action.context_click(mouse_tracker).perform()

    def hover_on_element(self, type, locator):
        self.wait_element_to_be_clickable(type, locator)
        mouse_tracker = self.driver.find_element(type, locator)
        self.action.move_to_element(mouse_tracker).perform()

    def move_horizontal_slider(self, type, locator, x_value):
        self.wait_element_to_be_clickable(type, locator)
        mouse_tracker = self.driver.find_element(type, locator)
        self.action \
            .click_and_hold(mouse_tracker) \
            .move_to_element_with_offset(mouse_tracker, x_value, 0) \
            .perform()

    def drag_and_drop(self, source, target):
        try:
            if type(source) is WebElement:
                self.action.drag_and_drop(source, target).perform()
            else:
                source = self.driver.find_element(*source)
            if type(target) is WebElement:
                self.action.drag_and_drop(source, target).perform()
            else:
                target = self.driver.find_element(*target)
            self.action.drag_and_drop(source, target).perform()
        except:
            raise "Please, use set or WebElement"

    ''' Files '''

    def upload_file(self, type, locator, file_path):
        # ХЗ какой вейт
        self.enter_text(type, locator, file_path)

    ''' Inputs and textareas'''

    def clear_field(self, type, locator):
        self.wait_element_to_be_clickable(type, locator)
        if self.get_text_from_field(type, locator) == "":
            pass
        else:
            self.driver.find_element(type, locator).clear()
            assert self.get_text_from_field(type, locator) == "", "Field was not cleared"

    def enter_text(self, type, locator, text):
        self.wait_element_to_be_clickable(type, locator)
        self.clear_field(type, locator)
        element = self.driver.find_element(type, locator)
        element.send_keys(text)
        assert element.text == text, "Text was not entered"

    def get_text_from_field(self, type, locator):
        return self.driver.find_element(type, locator).get_attribute("value")

    ''' Waits '''

    @dispatch(WebElement)
    def wait_element_to_be_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable((locator)))

    @dispatch(str, str)
    def wait_element_to_be_clickable(self, method, locator):
        self.wait.until(EC.element_to_be_clickable((method, locator)))

    @dispatch(tuple)
    def wait_element_to_be_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable((locator)))

    def wait_visibility_of_element_located(self, type, locator):
        self.wait.until(EC.visibility_of_element_located((type, locator)))

    def wait_text_to_be_present_in_element(self, locator, text):
        self.wait.until(EC.text_to_be_present_in_element(locator, text))

    def wait_invisibility_of_element_located(self, type, locator):
        self.wait.until(EC.invisibility_of_element_located((type, locator)))

    def wait_presence_of_element_located(self, type, locator):
        self.wait.until(EC.presence_of_element_located((type, locator)))
