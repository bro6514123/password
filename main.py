from selenium import webdriver
from selenium.webdriver.common.by import By
import threading
from itertools import product, islice


class ChromeWindow:
    def __init__(self):
        self.window = webdriver.Chrome()
        self.window.get("http://127.0.0.1:5000/")

    def start(self) -> None:
        while True:
            password = givPassword() 
            if not password:
                break

            try:
                text_input = self.window.find_element(By.NAME, "text")
                submit_button = self.window.find_element(By.NAME, "submit")

                text_input.send_keys(password)
                submit_button.click()
                editLastPassword(password)

            except KeyboardInterrupt:
                print("stop")
                break
            except Exception as error:
                editPassword()
                print(error)
                break



total_password = None
last_password = None
start_password = 0
last_index = 0


def editLastPassword(new_password):
    global last_password
    last_password = new_password

def printLastIndex():
    print(last_index)

def editPassword():
    global total_password

    total_password = last_password
    printLastIndex()
    print(total_password)

def givPasswords():
    symbols = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    all_passwords = (''.join(p) for p in product(symbols, repeat=4))

    return islice(all_passwords, start_password, None)


def newWindow():
    ChromeWindow().start()


passwords = givPasswords()
def givPassword():
    global last_index
    try:   
        last_index += 1
        if not total_password:
            password = next(passwords)
            return password
        else:
            return None
        
    except StopIteration:
        return None
    

if __name__ == "__main__":
    threading.Thread(target=newWindow).start()
    threading.Thread(target=newWindow).start()
    threading.Thread(target=newWindow).start()
    threading.Thread(target=newWindow).start()