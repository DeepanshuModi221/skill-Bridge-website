import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SkillBridgeDemoTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # 👉 Change this to your localhost URL if needed
        cls.driver.get("file:///C:/Users/dell/OneDrive/Desktop/DeepanshuP/skill-bridge/index.html")
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 10)

    def test_1_page_title_and_header(self):
        """Verify the page title and header text"""
        driver = self.driver
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.assertIn("Skill Bridge", driver.title)
        header = driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(header.text.strip(), "Skill Bridge")

    def test_2_tabs_exist_and_toggle(self):
        """Check both tabs exist and toggle visibility correctly"""
        driver = self.driver
        self.wait.until(EC.presence_of_element_located((By.ID, "tab-courses")))
        courses_tab = driver.find_element(By.ID, "tab-courses")
        jobs_tab = driver.find_element(By.ID, "tab-jobs")

        self.assertTrue(courses_tab.is_displayed())
        self.assertTrue(jobs_tab.is_displayed())

        jobs_tab.click()
        time.sleep(1)
        jobs_view = driver.find_element(By.ID, "view-jobs")
        self.assertFalse("hidden" in jobs_view.get_attribute("class"))

        courses_tab.click()
        time.sleep(1)
        courses_view = driver.find_element(By.ID, "view-courses")
        self.assertFalse("hidden" in courses_view.get_attribute("class"))

    def test_3_courses_controls_exist(self):
        """Check search input and dropdown exist in Courses view"""
        driver = self.driver
        self.wait.until(EC.presence_of_element_located((By.ID, "course-search")))
        search_box = driver.find_element(By.ID, "course-search")
        course_type = driver.find_element(By.ID, "course-type")
        self.assertTrue(search_box.is_displayed())
        self.assertTrue(course_type.is_displayed())
        search_box.send_keys("Python")
        time.sleep(1)
        search_box.clear()

    def test_4_jobs_controls_exist(self):
        """Check search input and dropdown exist in Jobs view"""
        driver = self.driver
        self.wait.until(EC.presence_of_element_located((By.ID, "tab-jobs"))).click()
        self.wait.until(EC.presence_of_element_located((By.ID, "job-search")))
        job_search = driver.find_element(By.ID, "job-search")
        job_type = driver.find_element(By.ID, "job-type")
        self.assertTrue(job_search.is_displayed())
        self.assertTrue(job_type.is_displayed())

    def test_5_list_containers_exist(self):
        """Verify courses-list and jobs-list containers exist"""
        driver = self.driver
        self.wait.until(EC.presence_of_element_located((By.ID, "courses-list")))
        courses_list = driver.find_element(By.ID, "courses-list")
        jobs_list = driver.find_element(By.ID, "jobs-list")
        self.assertTrue(courses_list.is_displayed() or jobs_list.is_displayed())

    def test_6_footer_displayed(self):
        """Verify footer text is visible"""
        driver = self.driver
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "site-footer")))
        footer = driver.find_element(By.CLASS_NAME, "site-footer")
        self.assertIn("Skill Bridge", footer.text)

    def test_7_course_type_dropdown_options(self):
        """Ensure all expected course type options exist"""
        driver = self.driver
        select = driver.find_element(By.ID, "course-type")

        # Fallback to 'value' attribute if inner text is empty
        options = []
        for opt in select.find_elements(By.TAG_NAME, "option"):
            text = opt.text.strip().lower()
            if not text:
                text = opt.get_attribute("value").strip().lower()
            options.append(text)

        expected = ["all", "programming", "design", "data", "cloud", "business"]

        for item in expected:
            found = any(item in option for option in options)
            self.assertTrue(found, f"Missing option for: {item}")

    def test_8_job_type_dropdown_options(self):
        """Ensure all expected job type options exist"""
        driver = self.driver
        self.wait.until(EC.presence_of_element_located((By.ID, "job-type")))
        select = driver.find_element(By.ID, "job-type")

        options = []
        for opt in select.find_elements(By.TAG_NAME, "option"):
            text = opt.text.strip().lower()
            if not text:
                text = opt.get_attribute("value").strip().lower()
            options.append(text)

        expected = ["all", "full-time", "part-time", "contract", "internship"]

        for item in expected:
            found = any(item in option for option in options)
            self.assertTrue(found, f"Missing job type: {item}")

    def test_9_tab_switch_persists_state(self):
        """Switch tabs back and forth and verify the active view changes correctly"""
        driver = self.driver
        courses_tab = driver.find_element(By.ID, "tab-courses")
        jobs_tab = driver.find_element(By.ID, "tab-jobs")

        jobs_tab.click()
        time.sleep(0.5)
        self.assertFalse("hidden" in driver.find_element(By.ID, "view-jobs").get_attribute("class"))

        courses_tab.click()
        time.sleep(0.5)
        self.assertFalse("hidden" in driver.find_element(By.ID, "view-courses").get_attribute("class"))

    def test_10_template_elements_exist(self):
        """Confirm the <template> elements exist for courses and jobs"""
        driver = self.driver
        course_tpl = driver.find_element(By.ID, "course-item-tpl")
        job_tpl = driver.find_element(By.ID, "job-item-tpl")
        self.assertIsNotNone(course_tpl)
        self.assertIsNotNone(job_tpl)

    def test_11_meta_description_exists(self):
        """Check that meta charset and viewport tags are present"""
        driver = self.driver
        meta_charset = driver.find_element(By.CSS_SELECTOR, 'meta[charset="utf-8"]')
        meta_viewport = driver.find_element(By.CSS_SELECTOR, 'meta[name="viewport"]')
        self.assertIsNotNone(meta_charset)
        self.assertIn("width=device-width", meta_viewport.get_attribute("content"))

    def test_12_header_tagline_present(self):
        """Verify tagline appears below the main heading"""
        driver = self.driver
        tagline = driver.find_element(By.CLASS_NAME, "tagline")
        self.assertIn("Search courses", tagline.text)

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)

