import allure
from allure_commons.types import Severity

from model.pages.practice_form import RegistrationPage


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'v-victoriakir')
@allure.feature("Задача по Jenkins")
@allure.story("Успешная отправка полной формы")
@allure.link('https://github.com/', 'Testing')
def test_form_submitted():
    practice_form = RegistrationPage()
    practice_form.open()

    practice_form.fill_first_name("Maria")
    practice_form.fill_last_name("Lopez")
    practice_form.fill_email("MLopez@gmail.com")
    practice_form.select_gender("Female")
    practice_form.fill_mobile_number("0123456789")
    practice_form.fill_date_of_birth(9, 1996, 10)
    practice_form.fill_subject('Biology')
    practice_form.select_hobbies("Reading")
    practice_form.select_hobbies("Music")
    practice_form.set_avatar("unnamed.jpg")
    practice_form.fill_current_address("Main street, 55 bld, 10 apt.")
    practice_form.select_state("Rajasthan")
    practice_form.select_city("Jaipur")
    practice_form.submit_form()
    practice_form.registered_user_should_have(
        "Maria", "Lopez", "MLopez@gmail.com", "Female", "0123456789", "10 October,1996", "Biology", "Reading, Music",
        "unnamed.jpg", "Main street, 55 bld, 10 apt.", "Rajasthan", "Jaipur"
    )


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label('owner', 'v-victoriakir')
@allure.feature("Задача по Jenkins")
@allure.story("Успешная отправка формы с обязат. полями")
@allure.link('https://github.com/', 'Testing')
def test_form_required_fields_only(today_date):
    practice_form = RegistrationPage()
    practice_form.open()
    practice_form.fill_first_name("Maria")
    practice_form.fill_last_name("Lopez")
    practice_form.select_gender("Female")
    practice_form.fill_mobile_number("0123456789")
    practice_form.submit_form()
    practice_form.registered_user_should_have(
        "Maria", "Lopez", "", "Female", "0123456789", f"c", "", "",
        "", "", "", ""
    )


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'v-victoriakir')
@allure.feature("Задача по Jenkins")
@allure.story("Проверка на наличие валидации по заполнению обязательн. полей")
@allure.link('https://github.com/', 'Testing')
def test_form_error_required_fields_not_filled():
    practice_form = RegistrationPage()
    practice_form.open()
    practice_form.fill_first_name("Maria")
    practice_form.select_gender("Female")
    practice_form.submit_form()
    practice_form.check_if_required_fields_not_filled()


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'v-victoriakir')
@allure.feature("Задача по Jenkins")
@allure.story("Проверка на наличие валидации в инпуте Mobile")
@allure.link('https://github.com/', 'Testing')
def test_form_required_fields_but_wrong_number():
    practice_form = RegistrationPage()
    practice_form.open()
    practice_form.fill_first_name("Maria")
    practice_form.fill_last_name("Lopez")
    practice_form.select_gender("Female")
    practice_form.fill_mobile_number("123456789")
    practice_form.submit_form()
    practice_form.check_if_required_fields_not_filled()
