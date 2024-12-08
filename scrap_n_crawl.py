# TODO: Create a program that does the following:
#  1. Using selenium navigate to https://www.how-to-type.com/typing-practice/programming/py/
#  2. Create a file called <sample_name>.tfd and write the PREFIX
#  3. Grab the text with beautiful soup, or selenium
#  4. Append text to the .tfd file followed by # ---
#  5. Use Selenium to press on the new  'New Code snippet'
#  6. Repeat steps 4-6 as many times as you want
#  7. Enjoy your life

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime as dt

URL = 'https://www.how-to-type.com/typing-practice/programming/py/'

PREFIX = ('@id custom-b92760dd-0f00-4933-a426-a72f3d78ef5c\n'
          '@type code\n'
          '@name Python\n'
          '@language python\n'
          '@items\n')

POSTFIX = '\n\n# ---\n\n'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
reps_ = 0

if __name__ == '__main__':
    reps_ = int(input('How many times would you like to attempt fetching code snippets from "how-to-type"? '))
    driver.get(URL)  # Navigate to page
    sleep(1)  # Wait for the page to load
    driver.find_element(By.CLASS_NAME, 'fc-cta-consent').click()  # Hit cookie button
    driver.maximize_window()
    sleep(3)


"------------------------DEFINITIONS----------------------"


def grab_and_format_text(reps):
    entries_cnt = 0
    c = 0
    final_text = PREFIX
    while c < reps:
        letters = ""
        elements = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div/div/div[2]/div[2]/div[3]/div[1]/span')
        for i, e in enumerate(elements):
            if e.text == "":
                if e.get_attribute('id') and not elements[i + 1].get_attribute('id'):
                    letters += "\n"
                else:
                    letters += " "
            else:
                letters += e.text
        letters += POSTFIX
        if letters not in final_text:
            final_text += letters
            print('successful entry')
            entries_cnt += 1
        else:
            print('Entry skipped, as it already exists')
        print(f'Entry added {entries_cnt}/{c + 1}')
        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div[2]/div[2]/a').click()
        sleep(1)
        c += 1
    return final_text.rstrip(POSTFIX)


"------------------------/DEFINITIONS----------------------"
if __name__ == '__main__':
    with open(file=rf'E:\Desktop\TypeFu\scraped_tfd\TF{dt.now().strftime("%d%m%y_%H%M")}.tfd', mode='w') as f:
        f.write(grab_and_format_text(reps_))
    driver.close()  # closes tab
    # driver.quit()  # closes browser
