import time

from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By


# Позитивные тесты:
#1. Все поля формы заполнены кириллицей:
def test_all_fields_filled_with_cyrillic_letters(driver):

    driver.find_element(By.ID, "userName").send_keys("Петр Петров")
    driver.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Москва")
    driver.find_element(By.ID, "permanentAddress").send_keys("Санкт-Петербург")

    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = driver.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrov@example" in result_box.text
    assert "Москва" in result_box.text
    assert "Санкт-Петербург" in result_box.text

#2. Все поля формы заполнены латиницей:
def test_all_fields_filled_with_latin_letters(driver):

    driver.find_element(By.ID, "userName").send_keys("Olga Ivanova")
    driver.find_element(By.ID,"userEmail").send_keys("olgaivanova@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Moscow")
    driver.find_element(By.ID, "permanentAddress").send_keys("Saint-Petersburg")

    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = driver.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Olga Ivanova" in result_box.text
    assert "olgaivanova@example.com" in result_box.text
    assert "Moscow" in result_box.text
    assert "Saint-Petersburg" in result_box.text


#3. В поле Full Name указано полное ФИО (с отчеством):
def test_name_surname_patronymic_in_name_field(driver):

    driver.find_element(By.ID, "userName").send_keys("Петров Петр Петрович")
    driver.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Москва")
    driver.find_element(By.ID, "permanentAddress").send_keys("Санкт-Петербург")

    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = driver.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петров Петр Петрович" in result_box.text
    assert "petrov@example" in result_box.text
    assert "Москва" in result_box.text
    assert "Санкт-Петербург" in result_box.text

#4. В поле Full Name указано короткое значение:
def test_short_name(driver):

    driver.find_element(By.ID, "userName").send_keys("Ян")
    driver.find_element(By.ID, "userEmail").send_keys("yan@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Москва")
    driver.find_element(By.ID, "permanentAddress").send_keys("Сочи")

    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = driver.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Ян" in result_box.text
    assert "yan@example.com" in result_box.text
    assert "Москва" in result_box.text
    assert "Сочи" in result_box.text


#5. В поле Full Name указано длинное значение:
def test_long_name(driver):

    driver.find_element(By.ID, "userName").send_keys("Константинопольская Апполинария Максимилиановна")
    driver.find_element(By.ID, "userEmail").send_keys("yan@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Москва")
    driver.find_element(By.ID, "permanentAddress").send_keys("Сочи")

    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = driver.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Константинопольская Апполинария Максимилиановна" in result_box.text
    assert "yan@example.com" in result_box.text
    assert "Москва" in result_box.text
    assert "Сочи" in result_box.text


#6. В поле Full Name присутствует дефис:
def test_hyphen_in_name_field(driver):
    driver.find_element(By.ID, "userName").send_keys("Иван Мамин-Сибиряк")
    driver.find_element(By.ID, "userEmail").send_keys("yan@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Москва")
    driver.find_element(By.ID, "permanentAddress").send_keys("Сочи")

    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = driver.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Иван Мамин-Сибиряк" in result_box.text
    assert "yan@example.com" in result_box.text
    assert "Москва" in result_box.text
    assert "Сочи" in result_box.text


#7. В поле Email буквы разных регистров:
def test_email_in_mixed_case(driver):
    driver.find_element(By.ID, "userName").send_keys("Петр Петров")
    driver.find_element(By.ID, "userEmail").send_keys("PetrovPetr@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Казань")
    driver.find_element(By.ID, "permanentAddress").send_keys("Москва")

    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = driver.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "PetrovPetr@example.com" in result_box.text
    assert "Казань" in result_box.text
    assert "Москва" in result_box.text


#8. В поле Email присутствуют цифры:
def test_numbers_in_email(driver):
    driver.find_element(By.ID, "userName").send_keys("Петр Петров")
    driver.find_element(By.ID, "userEmail").send_keys("petrov1985@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Тюмень")
    driver.find_element(By.ID, "permanentAddress").send_keys("Омск")

    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = driver.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrov1985@example.com" in result_box.text
    assert "Тюмень"
    assert "Омск"


#9. Значения полей current_address и permanent_address совпадают:
def test_current_address_equals_permanent_address(driver):
    driver.find_element(By.ID, "userName").send_keys("Петр Петров")
    driver.find_element(By.ID, "userEmail").send_keys("petrovpetya@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Москва")
    driver.find_element(By.ID, "permanentAddress").send_keys("Москва")

    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = driver.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrovpetya@example.com" in result_box.text
    assert "Москва" in result_box.text
    assert "Москва" in result_box.text


#10. В поле current_address указан адрес с городом, улицей, номерами дома и квартиры:
def test_current_address_with_city_street_house_flat(driver):
    driver.find_element(By.ID, "userName").send_keys("Петр Петров")
    driver.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Москва, ул. Тверская, дом 5, кв. 23")
    driver.find_element(By.ID, "permanentAddress").send_keys("Краснодар")

    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = driver.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrov@example.com" in result_box.text
    assert "Москва, ул. Тверская, дом 5, кв. 23" in result_box.text
    assert "Краснодар" in result_box.text

#11. В поле current_address указан адрес с городом, улицей, номерами дома, строения и квартиры:
def test_current_address_with_city_street_house_building_flat(driver):
    driver.find_element(By.ID, "userName").send_keys("Петр Петров")
    driver.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Москва, ул. Тверская, дом 5, корп. 1, кв. 23")
    driver.find_element(By.ID, "permanentAddress").send_keys("Краснодар")

    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = driver.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrov@example.com" in result_box.text
    assert "Москва, ул. Тверская, дом 5, корп. 1, кв. 23" in result_box.text
    assert "Краснодар" in result_box.text


#12. В поле current_address указан адрес с городом и улицей:
def test_current_address_only_city_and_street(driver):
        driver.find_element(By.ID, "userName").send_keys("Петр Петров")
        driver.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
        driver.find_element(By.ID, "currentAddress").send_keys("Москва, ул. Тверская")
        driver.find_element(By.ID, "permanentAddress").send_keys("Краснодар")

        driver.find_element(By.ID, "submit").click()

        time.sleep(3)

        result_box = driver.find_element(By.ID, "output")

        assert result_box.is_displayed()
        assert "Петр Петров" in result_box.text
        assert "petrov@example.com" in result_box.text
        assert "Москва, ул. Тверская" in result_box.text
        assert "Краснодар" in result_box.text


#13. В поле current_address указан длинный адрес:
def test_long_current_address(driver):
        driver.find_element(By.ID, "userName").send_keys("Петр Петров")
        driver.find_element(By.ID, "userEmail").send_keys("petrov@example.com")

        long_current_address: str = ("192177, г. Санкт-Петербург, Внутригородское "
                                                               "муниципальное образование Санкт-Петербурга "
                                                               "муниципальный округ Рыбацкое, Шлиссельбургский проспект, "
                                                               "дом 24, корпус 2, строение 1, подвальный этаж, "
                                                               "помещение 3-Н, комната 14, офис 5")

        driver.find_element(By.ID, "currentAddress").send_keys(long_current_address)
        driver.find_element(By.ID, "permanentAddress").send_keys("Краснодар")

        driver.find_element(By.ID, "submit").click()

        time.sleep(3)

        result_box = driver.find_element(By.ID, "output")

        assert result_box.is_displayed()
        assert "Петр Петров" in result_box.text
        assert "petrov@example.com" in result_box.text
        assert long_current_address in result_box.text
        assert "Краснодар" in result_box.text


#14. В поле current_address указан короткий адрес:
def test_short_current_address(driver):
    driver.find_element(By.ID, "userName").send_keys("Петр Петров")
    driver.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Уфа")
    driver.find_element(By.ID, "permanentAddress").send_keys("Краснодар")

    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = driver.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrov@example.com" in result_box.text
    assert "Уфа" in result_box.text
    assert "Краснодар" in result_box.text


#15. В поле current_address присутствуют спецсимволы:
def test_current_address_contains_symbols(driver):
        driver.find_element(By.ID, "userName").send_keys("Петр Петров")
        driver.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
        driver.find_element(By.ID, "currentAddress").send_keys("г. Санкт-Петербург, Невский пр., д. 15/2, кв. №34")
        driver.find_element(By.ID, "permanentAddress").send_keys("Пермь")

        driver.find_element(By.ID, "submit").click()

        time.sleep(3)

        result_box = driver.find_element(By.ID, "output")

        assert result_box.is_displayed()
        assert "Петр Петров" in result_box.text
        assert "petrov@example.com" in result_box.text
        assert "г. Санкт-Петербург, Невский пр., д. 15/2, кв. №34" in result_box.text
        assert "Пермь" in result_box.text


#16. В поле permanent_address указан адрес с городом, улицей, номерами дома и квартиры:
def test_permanent_address_with_city_street_house_flat(driver):
    driver.find_element(By.ID, "userName").send_keys("Петр Петров")
    driver.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Казань")
    driver.find_element(By.ID, "permanentAddress").send_keys("Москва, ул. Тверская, дом 5, кв. 23")

    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = driver.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrov@example.com" in result_box.text
    assert "Казань" in result_box.text
    assert "Москва, ул. Тверская, дом 5, кв. 23" in result_box.text


#17. В поле permanent_address указан адрес с городом, улицей, номерами дома, строения и квартиры:
def test_permanent_address_with_city_street_house_building_flat(driver):
    driver.find_element(By.ID, "userName").send_keys("Петр Петров")
    driver.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Казань")
    driver.find_element(By.ID, "permanentAddress").send_keys("Москва, ул. Тверская, дом 5, корп. 1, кв. 23")

    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = driver.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrov@example.com" in result_box.text
    assert "Казань" in result_box.text
    assert "Москва, ул. Тверская, дом 5, корп. 1, кв. 23" in result_box.text


#18. В поле permanent_address указан адрес с городом и улицей:
def test_permanent_address_only_city_and_street(driver):
        driver.find_element(By.ID, "userName").send_keys("Петр Петров")
        driver.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
        driver.find_element(By.ID, "currentAddress").send_keys("Казань")
        driver.find_element(By.ID, "permanentAddress").send_keys("Москва, ул. Тверская")

        driver.find_element(By.ID, "submit").click()

        time.sleep(3)

        result_box = driver.find_element(By.ID, "output")

        assert result_box.is_displayed()
        assert "Петр Петров" in result_box.text
        assert "petrov@example.com" in result_box.text
        assert "Казань" in result_box.text
        assert "Москва, ул. Тверская" in result_box.text


#19. В поле permanent_address указан длинный адрес:
def test_long_permanent_address(driver):
        driver.find_element(By.ID, "userName").send_keys("Петр Петров")
        driver.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
        driver.find_element(By.ID, "currentAddress").send_keys("Казань")

        long_permanent_address: str = ("192177, г. Санкт-Петербург, Внутригородское "
                                                               "муниципальное образование Санкт-Петербурга "
                                                               "муниципальный округ Рыбацкое, Шлиссельбургский проспект, "
                                                               "дом 24, корпус 2, строение 1, подвальный этаж, "
                                                               "помещение 3-Н, комната 14, офис 5")

        driver.find_element(By.ID, "permanentAddress").send_keys(long_permanent_address)

        driver.find_element(By.ID, "submit").click()

        time.sleep(3)

        result_box = driver.find_element(By.ID, "output")

        assert result_box.is_displayed()
        assert "Петр Петров" in result_box.text
        assert "petrov@example.com" in result_box.text
        assert "Казань" in result_box.text
        assert long_permanent_address in result_box.text


#20. В поле permanent_address указан короткий адрес:
def test_short_permanent_address(driver):
    driver.find_element(By.ID, "userName").send_keys("Петр Петров")
    driver.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Мурманск")
    driver.find_element(By.ID, "permanentAddress").send_keys("Уфа")

    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = driver.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrov@example.com" in result_box.text
    assert "Мурманск" in result_box.text
    assert "Уфа" in result_box.text


#21. В поле permanent_address присутствуют спецсимволы:
def test_permanent_address_contains_symbols(driver):
        driver.find_element(By.ID, "userName").send_keys("Петр Петров")
        driver.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
        driver.find_element(By.ID, "currentAddress").send_keys("Пермь")
        driver.find_element(By.ID, "permanentAddress").send_keys("г. Санкт-Петербург, Невский пр., д. 15/2, кв. №34")

        driver.find_element(By.ID, "submit").click()

        time.sleep(3)

        result_box = driver.find_element(By.ID, "output")

        assert result_box.is_displayed()
        assert "Петр Петров" in result_box.text
        assert "petrov@example.com" in result_box.text
        assert "Пермь" in result_box.text
        assert "г. Санкт-Петербург, Невский пр., д. 15/2, кв. №34" in result_box.text

#22. Форма отправляется, если все поля формы пустые (позитивная проверка, так как все поля формы необязательные):
# Падает из-за опечатки на странице ("permananet" вместо "permanent")
def test_text_form_sent_if_all_fields_empty(driver):
    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = driver.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Name:\n" in result_box.text
    assert "Email:\n" in result_box.text
    assert "Current Address :\n" in result_box.text
    assert "Permanent Address :\n" in result_box.text


# Негативные тесты:
#1. Email без символа @:
def test_email_with_no_mail_symbol (driver):
    driver.find_element(By.ID, "userName").send_keys("Петр Петров")
    driver.find_element(By.ID, "userEmail").send_keys("petrovexample.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Мурманск")
    driver.find_element(By.ID, "permanentAddress").send_keys("Уфа")

    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    error_text = driver.find_element(By.ID, "userEmail").get_attribute("validationMessage")

    assert error_text != ""


#2. В поле Email используется кириллица:
def test_long_email(driver):
    driver.find_element(By.ID, "userName").send_keys("Петр Петров")
    driver.find_element(By.ID, "userEmail").send_keys("петров@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Москва")
    driver.find_element(By.ID, "permanentAddress").send_keys("Санкт-Петербург")

    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    error_text = driver.find_element(By.ID, "userEmail").get_attribute("validationMessage")

    assert error_text != ""


#3. В поле Email два символа @@:
def test_email_with_two_mail_symbols(driver):
    driver.find_element(By.ID, "userName").send_keys("Петр Петров")
    driver.find_element(By.ID, "userEmail").send_keys("petrov@@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Москва")
    driver.find_element(By.ID, "permanentAddress").send_keys("Санкт-Петербург")

    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    error_text = driver.find_element(By.ID, "userEmail").get_attribute("validationMessage")

    assert error_text != ""


#4. В поле Email спецсимволы:
def test_special_symbols_in_email_field(driver):
    driver.find_element(By.ID, "userName").send_keys("Петр Петров")
    driver.find_element(By.ID, "userEmail").send_keys("petrov[]@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Москва")
    driver.find_element(By.ID, "permanentAddress").send_keys("Санкт-Петербург")

    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    error_text = driver.find_element(By.ID, "userEmail").get_attribute("validationMessage")

    assert error_text != ""


#5. В поле Email пробел:
def test_space_in_email_field(driver):
    driver.find_element(By.ID, "userName").send_keys("Петр Петров")
    driver.find_element(By.ID, "userEmail").send_keys("petrov @example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Москва")
    driver.find_element(By.ID, "permanentAddress").send_keys("Санкт-Петербург")

    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    error_text = driver.find_element(By.ID, "userEmail").get_attribute("validationMessage")

    assert error_text != ""

#6. HTML-иньекция (тест падает, так как html выполняется):
def test_html_injection(driver):
    payload = "<div id='hack'>Hello</div>"

    driver.find_element(By.ID, "userName").send_keys(payload)
    driver.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Москва")
    driver.find_element(By.ID, "permanentAddress").send_keys("Санкт-Петербург")

    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    html_elements = driver.find_elements(By.ID, "hack")

    assert len(html_elements) == 0


#7. XSS-иньекция:
def test_xss_injection(driver):
    payload = "<script>alert(1)</script>"

    driver.find_element(By.ID, "userName").send_keys(payload)
    driver.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Москва")
    driver.find_element(By.ID, "permanentAddress").send_keys("Санкт-Петербург")

    driver.find_element(By.ID, "submit").click()

    time.sleep(3)

    try:
        alert = driver.switch_to.alert
        assert False, f"XSS работает! Alert: {alert.text}"
    except NoAlertPresentException:
        pass