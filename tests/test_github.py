import allure
from allure_commons.types import AttachmentType
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "sakhr-qa-autotest")
@allure.feature("Задачи в репозитории")
@allure.story("Пример теста без шагов")
@allure.link("https://github.com", name="Testing")
def test_github():
    browser.open("https://github.com")
    browser.driver.maximize_window()
    s(".header-search-input").click()
    s(".header-search-input").send_keys("allure-framework/allure-python")
    s(".header-search-input").submit()
    s(by.link_text("allure-framework/allure-python")).click()
    s("#issues-tab").click()
    s(by.partial_text("#726")).should(be.visible)


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "sakhr-qa-autotest")
@allure.feature("Задачи в репозитории")
@allure.story("Пример теста с лямбда шагами")
@allure.link("https://github.com", name="Testing")
def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")
    with allure.step("Ищем репозитория"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("allure-framework/allure-python")
        s(".header-search-input").submit()
    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("allure-framework/allure-python")).click()
    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()
    with allure.step("Проверяем наличие Issue с номером 726"):
        s(by.partial_text("#726")).should(be.visible)
    with allure.step("Делаем финальный скриншот"):
        allure.attach(browser.driver.get_screenshot_as_png(), name="Happypath", attachment_type=AttachmentType.JPG)


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "sakhr-qa-autotest")
@allure.feature("Задачи в репозитории")
@allure.story("Пример теста с декоратором")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps():
    open_main_page()
    search_for_repository("allure-framework/allure-python")
    go_to_repository("allure-framework/allure-python")
    open_issue_tab()
    should_see_issue_with_number("#726")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()
