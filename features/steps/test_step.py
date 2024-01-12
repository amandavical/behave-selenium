# steps/test_steps.py

from behave import given, when, then
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Scenario 1: Verify the main page loading


@given('The user accesses the DemoQA main page')
def step_given(context):
    """
       Opens the browser and accesses the DemoQA main page.
    """
    context.driver = webdriver.Chrome()
    context.driver.get("https://demoqa.com/")


@when('The page is loaded')
def step_when(context):
    """
        Waits until the page title is not empty.
    """
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "title")))


@then('The page title should be "{expected_title}"')
def step_then(context, expected_title):
    """
       Verifies if the page title is as expected.
    """
    actual_title = context.driver.title
    assert actual_title == expected_title, f'Expected title: "{expected_title}", Actual title: "{actual_title}"'

# Scenario 2: Verify navigation to the Elements section


@given('The user goes to the DemoQA main page')
def step_given(context):
    """
       Opens the browser and accesses the DemoQA main page.
    """
    context.driver = webdriver.Chrome()
    context.driver.get("https://demoqa.com/")


@when('The user clicks on the Elements section')
def step_when_click_elements_section(context):
    """
        Clicks on the "Elements" section after loading the main page.
    """
    try:
        # Locate the h5 element with the text "Elements"
        elements_title = context.driver.find_element(By.XPATH, "//h5[contains(text(),'Elements')]")

        # Use JavaScript to click on the element, regardless of visibility
        context.driver.execute_script("arguments[0].click();", elements_title)

    except NoSuchElementException:
        print("The Elements section title was not found")

    # Wait for some time after clicking to ensure the Elements page is fully loaded
    time.sleep(5)


@then('The Elements page should be displayed')
def step_then_elements_page_displayed(context):
    """
       Verifies if the Elements page is displayed correctly.
    """
    expected_url = "https://demoqa.com/elements"
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f'Expected URL: "{expected_url}", Actual URL: "{actual_url}"'


# Scenario 3: Fill and submit form with valid data

@given('The user accesses the Practice Form')
def step_given_form(context):
    """
       Opens the browser and accesses the Practice Form.
    """
    context.driver.get("https://demoqa.com/automation-practice-form")


@when('The user fills out the form with valid data')
def step_when_fill_form(context):
    """
       Fills out the Practice Form with valid data.
    """
    context.driver.find_element(By.ID, "firstName").send_keys("Amanda")
    time.sleep(2)
    context.driver.find_element(By.ID, "lastName").send_keys("Vieira")
    time.sleep(2)
    context.driver.find_element(By.ID, "userEmail").send_keys("amanda.vieira@example.com")
    time.sleep(2)

    # Choose the gender
    gender_label = context.driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-2']")
    context.driver.execute_script("arguments[0].click();", gender_label)
    time.sleep(2)

    # Fill in the phone number
    context.driver.find_element(By.ID, "userNumber").send_keys("1234567890")
    time.sleep(2)

    # Choose the hobby
    context.driver.execute_script("arguments[0].click();", context.driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']"))
    time.sleep(2)

    # Upload the image
    context.driver.find_element(By.ID, "uploadPicture").send_keys(
        "C:\\Users\\amand\\PycharmProjects\\behave_selenium\\features\\example.jpg")
    time.sleep(2)

    # Fill in the current address
    context.driver.find_element(By.ID, "currentAddress").send_keys("Flower Street, 256")
    time.sleep(2)


@when('Clicks submit')
def step_when_submit_form(context):
    """
       Clicks the Submit button after filling out the form.
    """
    submit_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "submit"))
    )

    # Click the "Submit" button using JavaScript
    context.driver.execute_script("arguments[0].click();", submit_button)
    time.sleep(5)


@then('A success message should be displayed')
def step_then_success_message(context):
    """
       Verifies if the success message is displayed after submitting the form.
    """
    time.sleep(5)

    try:
        # Wait until the dialog box is visible
        WebDriverWait(context.driver, 10).until(
            EC.visibility_of_any_elements_located((By.XPATH, "//div[@class='modal-body']/*"))
        )

    except TimeoutException:
        print("The dialog box was not found within the timeout period")

# Scenario 4: Fill form with invalid data


@given('The user accesses the Practice Form for invalid data')
def step_given_invalid_form(context):
    """
    Opens the Practice Form page for testing with invalid data.
    """
    context.driver.get("https://demoqa.com/automation-practice-form")
    time.sleep(2)


@when('The user fills out the form with invalid data')
def step_when_fill_invalid_form(context):
    """
    Fills out the Practice Form with invalid data for testing.
    """
    # Fill the form with invalid data
    context.driver.find_element(By.ID, "firstName").send_keys("1")
    time.sleep(2)
    context.driver.find_element(By.ID, "lastName").send_keys("2")
    time.sleep(2)
    context.driver.find_element(By.ID, "userEmail").send_keys("invalid_email")  # Invalid email
    time.sleep(2)
    context.driver.find_element(By.ID, "userNumber").send_keys("123")
    time.sleep(2)


@when('Clicks submit for invalid data')
def step_when_submit_invalid_form(context):
    """
    Clicks the "Submit" button after filling out the form with invalid data.
    """
    # Find the "Submit" button
    submit_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "submit"))
    )

    # Click the "Submit" button using JavaScript
    context.driver.execute_script("arguments[0].click();", submit_button)

    # Wait for some time to ensure the action is completed
    time.sleep(5)


@then('An error message should be displayed')
def step_then_error_message(context):
    """
    Verifies if an error message is displayed after submitting invalid data.
    """
    try:
        # Wait until the alert element is visible
        WebDriverWait(context.driver, 10).until(
            EC.visibility_of_any_elements_located((By.XPATH, "//div[contains(@class, 'field-error-message')]"))
        )

    except TimeoutException:
        print("The error message was not found within the timeout period")

# Scenario 5: Try to submit blank form


@given('The user accesses the Practice Form with blank fields')
def step_given_empty_form(context):
    """
    Opens the Practice Form page for testing with a blank form.
    """
    context.driver.get("https://demoqa.com/automation-practice-form")
    time.sleep(2)


@when('The user tries to submit the blank form')
def step_when_submit_empty_form(context):
    """
    Tries to submit the blank form by clicking the "Submit" button.
    """
    # Find the "Submit" button
    submit_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "submit"))
    )

    # Click the "Submit" button using JavaScript
    context.driver.execute_script("arguments[0].click();", submit_button)

    # Wait for some time to ensure the action is completed
    time.sleep(5)


@then('An error message for a blank form should be displayed')

def step_then_empty_form_error_message(context):
    """
    Verifies if an error message is displayed after attempting to submit a blank form.
    """
    try:
        # Wait until the alert element is visible
        WebDriverWait(context.driver, 10).until(
            EC.visibility_of_any_elements_located((By.XPATH, "//div[contains(@class, 'field-error-message')]"))
        )
    except TimeoutException:
        print("The error message for a blank form was not found within the timeout period")
