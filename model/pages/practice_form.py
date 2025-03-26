import allure
from selene import browser, have

from model import resource


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element("#firstName")
        self.last_name = browser.element("#lastName")
        self.email = browser.element("#userEmail")
        self.gender = browser.element("#gender-radio-1 + .custom-control-label")
        self.mobile_number = browser.element("#userNumber")

        self.date_of_birth_input = browser.element("#dateOfBirthInput")
        self.month = browser.element(".react-datepicker__month-select")
        self.year = browser.element(".react-datepicker__year-select")

        self.subject_input = browser.element('#subjectsInput')
        self.hobbies = browser.all('[for^=hobbies-checkbox]')
        self.upload_avatar = browser.element('#uploadPicture')
        self.current_address = browser.element("#currentAddress")
        self.state = browser.element("#state")
        self.city = browser.element("#city")

    @allure.step("Открыть страницу с формой регистрации")
    def open(self):
        browser.open("/")
        browser.driver.execute_script("$('#RightSide_Advertisement').remove()")
        return self

    @allure.step("Ввод имени")
    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    @allure.step("Ввод фамилии")
    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    @allure.step("Ввод эл. почты")
    def fill_email(self, value):
        self.email.type(value)
        return self

    @allure.step("Выбор пола")
    def select_gender(self, value):
        browser.element(f'[value={value}]').element('..').click()
        return self

    @allure.step("Ввод моб. телефона")
    def fill_mobile_number(self, value):
        self.mobile_number.type(value)
        return self

    @allure.step("Выбор даты рождения")
    def fill_date_of_birth(self, month, year, day):
        self.date_of_birth_input.click()
        self.month.click().element(f'[value="{month}"]').click()
        self.year.click().element(f'[value="{year}"]').click()
        browser.element(f".react-datepicker__day--0{day}").click()
        return self

    @allure.step("Выбор предмета")
    def fill_subject(self, value):
        self.subject_input.send_keys(value).press_enter()
        return self

        # self.subject_input.set_value(value).element(
        #     f'//*[contains(text(),{value})]'
        # ).click()
        # return self

        # self.subject_input.type(value).press_enter()
        # return self

    @allure.step("Выбор хобби")
    def select_hobbies(self, value):
        self.hobbies.element_by(have.text(value)).click()
        return self

    @allure.step("Загрузка аватара")
    def set_avatar(self, file_name):
        self.upload_avatar.set_value(resource.path(file_name))
        return self

    @allure.step("Ввод адреса проживания")
    def fill_current_address(self, value):
        self.current_address.type(value)
        return self

    @allure.step("Выбор штата")
    def select_state(self, value):
        self.state.click().all('[id^=react-select-3-option]').element_by(
            have.exact_text(value)).click()
        return self

    @allure.step("Выбор города")
    def select_city(self, value):
        self.city.click().all('[id^=react-select-4-option]').element_by(have.text(value)).click()
        return self

    @allure.step("Отправка формы")
    def submit_form(self):
        browser.element("#submit").click()
        return self

    @allure.step("Проверка отображения данных в отправленной форме")
    def registered_user_should_have(self, first_name, last_name, email, gender, mobile_number, date_of_birth, subjects,
                                    hobbies, file_name, address, state, city):
        browser.element(".table").should(have.text(f'{first_name} {last_name}'))
        browser.element(".table").should(have.text(email))
        browser.element(".table").should(have.text(gender))
        browser.element(".table").should(have.text(mobile_number))
        browser.element(".table").should(have.text(date_of_birth))
        browser.element(".table").should(have.text(subjects))
        browser.element(".table").should(have.text(hobbies))
        browser.element(".table").should(have.text(file_name))
        browser.element(".table").should(have.text(address))
        browser.element(".table").should(have.text(f'{state} {city}'))
        return self

    @allure.step("Проверка наличия валидации на незаполненных обязательных полях")
    def check_if_required_fields_not_filled(self):
        browser.element("#userForm").should(have.attribute("class").value("was-validated"))
        return self
