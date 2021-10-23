from selenium import webdriver
#from selenium.webdriver.chrome.options import Options     # HEADLESS OPTIONS
#options = Options()
#options.headless = True
# browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome()
browser.implicitly_wait(10)  # seconds



def duke(X, loginlist, passwordlist):

    browserX = X

    browserX = webdriver.Chrome()
    browserX.implicitly_wait(10)  # seconds

    browserX.get('https://www.duke-energy.com/home')

    browserX.find_element_by_css_selector('input#login-username').send_keys(loginlist)

    browserX.find_element_by_css_selector('input#login-password').send_keys(passwordlist)

    browserX.find_element_by_css_selector('input.btn-medium.btn-reverse').click()


duke(1, 'testlogin', 'testpassword')

duke(2, 'testlogin2', 'testpassword2')



def rduwater(X, login, pass1):

    browserX = X

    browserX = webdriver.Chrome()
    browserX.implicitly_wait(10)  # seconds

    browserX.get('https://ubwss.raleighnc.gov/login')

    browserX.find_element_by_css_selector('input#userId').send_keys(login)

    browserX.find_element_by_css_selector('input#password').send_keys(pass1)

    browserX.find_element_by_css_selector('input#submitButton').click()


rduwater(1, 'testlogin', 'testpassword')

rduwater(2, 'testlogin2', 'testpassword2')
