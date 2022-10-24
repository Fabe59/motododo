from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('window-size=1920x1080')


class Chrome_Login_Logout_FunctionalTestCase(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.browser.get(self.live_server_url)
        self.browser.implicitly_wait(30)
        self.browser.maximize_window()

        User = get_user_model()
        User.objects.create_user(
            username="UsernameTest",
            password="PasswordTest2020"
        )

    def tearDown(self):
        self.browser.close()

    def test_user_can_connect_and_disconnect(self):
        self.browser.find_element_by_css_selector('#button-login').click()
        user = self.browser.find_element_by_css_selector('#id_username')
        user.send_keys("UsernameTest")
        password = self.browser.find_element_by_css_selector('#id_password')
        password.send_keys("PasswordTest2020")
        self.browser.find_element_by_css_selector('#button-submit').click()
        self.browser.find_element_by_css_selector('#button-logout').click()
        self.assertTemplateUsed('users/logout.html')


class Chrome_Search_FunctionalTestCase(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.browser.get(self.live_server_url)
        self.browser.implicitly_wait(30)
        self.browser.maximize_window()

    def tearDown(self):
        self.browser.close()

    def test_search_empty_searchbox1(self):
        inputtest = self.browser.find_element_by_css_selector('#searchbox1')
        inputtest.send_keys("")
        self.browser.find_element_by_css_selector('#searchbutton1').click()
        self.assertTemplateUsed('accomodation/all_result.html')

    def test_search_searchbox1(self):
        inputtest = self.browser.find_element_by_css_selector('#searchbox1')
        inputtest.send_keys("Auray")
        self.browser.find_element_by_css_selector('#searchbutton1').click()
        self.assertTemplateUsed('accomodation/search.html')

    def test_search_empty_searchbox2(self):
        inputtest = self.browser.find_element_by_css_selector('#searchbox2')
        inputtest.send_keys("")
        self.browser.find_element_by_css_selector('#searchbutton2').click()
        self.assertTemplateUsed('accomodation/all_result.html')

    def test_search_searchbox2(self):
        inputtest = self.browser.find_element_by_css_selector('#searchbox2')
        inputtest.send_keys("Auray")
        self.browser.find_element_by_css_selector('#searchbutton2').click()
        self.assertTemplateUsed('accomodation/search.html')


class Chrome_Favorite_Page_FunctionalTestCase(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.browser.get(self.live_server_url)
        self.browser.implicitly_wait(30)
        self.browser.maximize_window()

        User = get_user_model()
        User.objects.create_user(
            username="UsernameTest",
            password="PasswordTest2020"
        )

    def tearDown(self):
        self.browser.close()

    def test_user_can_connect_and_disconnect(self):
        self.browser.find_element_by_css_selector('#button-login').click()
        user = self.browser.find_element_by_css_selector('#id_username')
        user.send_keys("UsernameTest")
        password = self.browser.find_element_by_css_selector('#id_password')
        password.send_keys("PasswordTest2020")
        self.browser.find_element_by_css_selector('#button-submit').click()
        self.browser.find_element_by_css_selector('#button-fav').click()
        self.assertTemplateUsed('users/favorite.html')


class Chrome_Add_Accomodation_FunctionalTestCase(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.browser.get(self.live_server_url)
        self.browser.implicitly_wait(30)
        self.browser.maximize_window()

        User = get_user_model()
        User.objects.create_user(
            username="UsernameTest",
            password="PasswordTest2020"
        )

    def tearDown(self):
        self.browser.close()

    def test_registred_user_can_add_accomodation(self):
        self.browser.find_element_by_css_selector('#button-login').click()
        user = self.browser.find_element_by_css_selector('#id_username')
        user.send_keys("UsernameTest")
        password = self.browser.find_element_by_css_selector('#id_password')
        password.send_keys("PasswordTest2020")
        self.browser.find_element_by_css_selector('#button-submit').click()
        self.browser.find_element_by_css_selector(
            '#button-add_accomodation').click()
        self.assertTemplateUsed('user/add.html')
        password = self.browser.find_element_by_css_selector(
            '#id_addAccomodation_name')
        password.send_keys("TestAccomodation")
        password = self.browser.find_element_by_css_selector(
            '#id_addAccomodation_category')
        password.send_keys("Hotel")
        password = self.browser.find_element_by_css_selector(
            '#id_addAccomodation_road')
        password.send_keys("Rue du Test")
        password = self.browser.find_element_by_css_selector(
            '#id_addAccomodation_zipcode')
        password.send_keys("59000")
        password = self.browser.find_element_by_css_selector(
            '#id_addAccomodation_city')
        password.send_keys("Lille")
        password = self.browser.find_element_by_css_selector(
            '#id_addAccomodation_phone')
        password.send_keys("0102030405")
        password = self.browser.find_element_by_css_selector(
            '#id_addAccomodation_parking')
        password.send_keys("Garage")
        password = self.browser.find_element_by_css_selector(
            '#id_addAccomodation_description')
        password.send_keys("Cool!")
        self.browser.find_element_by_css_selector(
            '#validation-add_accomodation').click()
        self.assertTemplateUsed('openrider/home.html')
