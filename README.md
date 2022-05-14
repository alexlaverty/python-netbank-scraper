# python-netbank-scraper

Python selenium script to automate logging into NetBank and exporting your accounts as CSV file.


# Instructions

## Install Chrome Driver
Download and install latest stable chrome driver for your operating system :

https://chromedriver.chromium.org/home

Add chromedriver.exe exe to your `Path`, or just copy file to `c:\Windows` directory :

```
C:\Windows\chromedriver.exe
```

## Install Python Requirements

```
pip install -r requirements.txt
```

## Check Python Version
This script was written with Python version :

```
python --version
Python 3.10.4
```

## Run script 

```
python app.py
```


## Troubleshooting 

### Message: 'chromedriver' executable needs to be in PATH.

```
PS D:\src\python-netbank-scraper> python .\app.py
Traceback (most recent call last):
  File "C:\Users\xxx\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\common\service.py", line 71, in start
    self.process = subprocess.Popen(cmd, env=self.env,
  File "C:\Users\xxx\AppData\Local\Programs\Python\Python310\lib\subprocess.py", line 966, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "C:\Users\xxx\AppData\Local\Programs\Python\Python310\lib\subprocess.py", line 1435, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
FileNotFoundError: [WinError 2] The system cannot find the file specified

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\src\python-netbank-scraper\app.py", line 7, in <module>
    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
  File "C:\Users\xxx\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\chrome\webdriver.py", line 70, in __init__
    super(WebDriver, self).__init__(DesiredCapabilities.CHROME['browserName'], "goog",
  File "C:\Users\xxx\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\chromium\webdriver.py", line 89, in __init__
    self.service.start()
  File "C:\Users\xxx\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\common\service.py", line 81, in start
    raise WebDriverException(
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://chromedriver.chromium.org/home
```

### Fix :

Download and install latest stable chrome driver for your operating system :

https://chromedriver.chromium.org/home

Add the exe to your windows Path, or just copy to c:\windows directory :

C:\Windows\chromedriver.exe

