from selenium.webdriver.common.by import By

class Locators:
    ### Страница регистрации
    # Ссылка на "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.LINK_TEXT, "Личный Кабинет")
    # Ссылка на "Зарегистрироваться"
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")
    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Поле ввода "Имя"
    NAME_INPUT = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')
    # Поле ввод email
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    # Поле ввод пароля
    PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    # Заголовок "Вход"
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")
    # Сообщение некорректный пароль
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")

    ### Страница входа
    # Кнопка "Войти в аккаунт"
    MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Ссылка "Войти"
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    # Поле ввод email
    EMAIL_INPUT_US = (By.XPATH, "//input[@name='name' or @type='email']")
    # Поле ввод пароля
    PASSWORD_INPUT_US = (By.XPATH, "//input[@type='password']")
    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'type_primary')]")
    # Ссылка на страницу восстановления пароля
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")
    # Кнопка "Оформить"
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить')]")
    # Кнопка "Выход"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    # Навигация
    # Профмль
    PROFILE_TAB = (By.XPATH, "//a[@href='/account/profile']")
    # Ссылка на конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH,"//a[@href='/']")
    # Заголовок "Соберите бургер"
    BURGER_HEADER = (By.XPATH,"//h1[text()='Соберите бургер']")
    # Логотип в шапке
    LOGO_BUTTON = (By.XPATH, "//header//a[.//*[name()='svg']]")
    # "Булки" в конструкторе
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
    # "Соусы" в конструкторе
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
    # "Начинки" в контрукторе
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")
    # Заголовок"Булки" 
    BUNS_HEADER = (By.XPATH, "//h2[text()='Булки']")
    # Заголовок"Сосиски" 
    SAUCES_HEADER = (By.XPATH, "//h2[text()='Соусы']")
    # Заголовок"Начинки" 
    FILLINGS_HEADER = (By.XPATH, "//h2[text()='Начинки']")
