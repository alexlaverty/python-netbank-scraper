from getpass import getpass
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json 
import os

NETBANK_ID = os.getenv('NETBANK_ID')
NETBANK_PASS = os.getenv('NETBANK_PASS')

if not (NETBANK_ID and NETBANK_PASS):
    NETBANK_ID = input("NetBank User: ")
    NETBANK_PASS = getpass("NetBank Pass (hidden): ")


driver = webdriver.Chrome()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 5)

def netbank():

    accounts = []
    url = "https://www.my.commbank.com.au/netbank/Logon/Logon.aspx"

    #driver.maximize_window()
    driver.get(url)

    # Login
    username = wait.until(EC.presence_of_element_located((By.NAME, "txtMyClientNumber$field")))
    username.send_keys(NETBANK_ID)
    password = driver.find_element(By.NAME, "txtMyPassword$field")
    password.send_keys(NETBANK_PASS)
    login = driver.find_element(By.NAME, "btnLogon$field")
    login.click()

    # Get Accounts
    account_elements = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'account-link-wrapper')))
    account_elements = driver.find_elements(By.CLASS_NAME, 'account-link-wrapper')
    for account_element in account_elements :
        account_name = account_element.find_element(By.CLASS_NAME, 'account-name').text
        account_url = account_element.find_element(By.CLASS_NAME, 'account-link').get_attribute('href')
        account_number = account_element.find_element(By.CLASS_NAME, 'account-number').text
        account_balances = account_element.find_element(By.CLASS_NAME, 'account-balances')
        balances = account_balances.find_elements(By.CLASS_NAME, 'balance')
        balance = ""
        available = ""
        for li_balance in balances:
            if li_balance.text.startswith('Balance'):
                balance = li_balance.find_element(By.CLASS_NAME, 'monetary-value').text
            elif li_balance.text.startswith('Available'):
                available = li_balance.find_element(By.CLASS_NAME, 'monetary-value').text

        account = {
            "name":account_name,
            "number":account_number,
            "balance":balance,
            "available":available,
            "url": account_url
           }

        accounts.append(account)

    print(json.dumps(accounts, indent=4, ensure_ascii=False))

    with open('accounts.json', 'w') as f:
        json.dump(accounts, f, indent=4)

    return accounts
    
def export_csv(account):

    if "name" in account:      
        account_name = account['name']
    else:
        account_name = "Unnamed"

    print(f"Exporting CSV From : {account_name}")

    driver.get(account['url'])

    wait = WebDriverWait(driver, 5)

    try:
        button = driver.find_element(By.ID, 'export-link')
    except:
        print("No export button, skipping!")
        return

    button.click()
    
    
    export_types = driver.find_elements(By.ID, 'export-format-type')
    for export_type in export_types:
        if "CSV (e.g. MS Excel)" in export_type.text:
            label = export_type.find_element(By.CLASS_NAME, 'form-check-label') 

            label.click()

            export = driver.find_element(By.ID, 'txnListExport-submit-btn')

            export.click()



if __name__ == "__main__":

    netbank_accounts = netbank()
    
    for netbank_account in netbank_accounts:
        export_csv(netbank_account)