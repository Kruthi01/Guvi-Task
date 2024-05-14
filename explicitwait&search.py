from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def perform_advanced_search(name="", birth_year="", death_year="", profession="", known_for="", gender=""):

    driver = webdriver.Chrome()


    driver.get("https://www.imdb.com/search/name/")

    try:
        # Fill in the search criteria
        if name:
            driver.find_element(By.ID, "sidebar").find_element_by_name("name").send_keys(name)
        if birth_year:
            driver.find_element(By.ID, "sidebar").find_element_by_name("birth_year").send_keys(birth_year)
        if death_year:
            driver.find_element(By.ID, "sidebar").find_element_by_name("death_year").send_keys(death_year)
        if profession:
            driver.find_element(By.ID, "sidebar").find_element_by_name("profession").send_keys(profession)
        if known_for:
            driver.find_element(By.ID, "sidebar").find_element_by_name("known_for").send_keys(known_for)
        if gender:
            driver.find_element(By.ID, "sidebar").find_element_by_name("gender").send_keys(gender)

        # Click on the search button
        driver.find_element(By.XPATH,'//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button/span').click()
        # Wait for search results to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "lister-list"))
        )
        # Print the titles of the search results
        search_results = driver.find_elements(By.CLASS_NAME, "lister-item-header")
        for result in search_results:
            print(result.text)

    finally:
        # Close the browser window
        driver.quit()


# Example usage
perform_advanced_search(name="Brad Pitt", birth_year="1963", profession="Actor", known_for="AA", gender="male")