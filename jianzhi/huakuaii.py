import time
import uuid
import StringIO
import Image
from selenium.webdriver.common.action_chains import ActionChains
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class BaseGeetestCrack(object):

    

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def input_by_id(self, text=u"fsd", element_id="keyword_qycx"):
        input_el = self.driver.find_element_by_id(element_id)
        input_el.clear()
        input_el.send_keys(text)
        time.sleep(3.5)

    def click_by_id(self, element_id="popup-submit"):

        search_el = self.driver.find_element_by_id(element_id)
        search_el.click()
        time.sleep(3.5)

    def calculate_slider_offset(self):

        img1 = self.crop_captcha_image()
        self.drag_and_drop(x_offset=5)
        img2 = self.crop_captcha_image()
        w1, h1 = img1.size
        w2, h2 = img2.size
        if w1 != w2 or h1 != h2:
            return False
        left = 0
        flag = False
        for i in xrange(45, w1):
            for j in xrange(h1):
                if not self.is_pixel_equal(img1, img2, i, j):
                    left = i
                    flag = True
                    break
            if flag:
                break
        if left == 45:
            left -= 2
        return left

    def is_pixel_equal(self, img1, img2, x, y):
        pix1 = img1.load()[x, y]
        pix2 = img2.load()[x, y]
        if (abs(pix1[0] - pix2[0] < 60) and abs(pix1[1] - pix2[1] < 60) and abs(pix1[2] - pix2[2] < 60)):
            return True
        else:
            return False

    def crop_captcha_image(self, element_id="gt_box"):

        captcha_el = self.driver.find_element_by_class_name(element_id)
        location = captcha_el.location
        size = captcha_el.size
        left = int(location['x'])
        top = int(location['y'])
        left = 1010
        top = 535
        # right = left + int(size['width'])
        # bottom = top + int(size['height'])
        right = left + 523
        bottom = top + 235
        print(left, top, right, bottom)

        screenshot = self.driver.get_screenshot_as_png()

        screenshot = Image.open(StringIO.StringIO(screenshot))
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save("%s.png" % uuid.uuid4().get_hex())
        return captcha

    def get_browser_name(self):

        return str(self.driver).split('.')[2]

    def drag_and_drop(self, x_offset=0, y_offset=0, element_class="gt_slider_knob"):

        dragger = self.driver.find_element_by_class_name(element_class)
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(dragger, x_offset, y_offset).perform()
        
        time.sleep(8)

    def move_to_element(self, element_class="gt_slider_knob"):

        time.sleep(3)
        element = self.driver.find_element_by_class_name(element_class)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        time.sleep(4.5)

    def crack(self):

        raise NotImplementedError