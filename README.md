# Test_Metric_Conversions
UI tests with Selenium and Python

Inside this repo is a script that automates 3 UI test cases to test https://www.metric-conversions.org/. Selenium Web driver and Python were used for this purpose.

Here is the instruction on how to launch the script:

1. Download Python3 installation file from the official site. If you already have Pyhton installed please make sure you are using version 3.6 or higher. Update your Python in case you have older version. Important! During installation make sure you have chosen "Add Python 3.x to PATH" option.

2. Download ChromeDriver: https://sites.google.com/a/chromium.org/chromedriver/downloads. Make sure you download the correct version for your browser. Create a new directory      called "chromedriver" on disk C: and unpack downloaded chromedriver.exe file to this directory (C:\chromedriver). Add C:\chromedriver dir to your PATH system variable. You may check how to do it for different Windows versions here: https://www.computerhope.com/issues/ch000549.htm.

3. Installing Python libraries:

You may create a separate virtual environment for this step but it is not a requirement.
Open cmd terminal:
Type: "pip install selenium" and press enter. This will install selenium library.
Type: "pip install pytest" and press enter. This will install pytest library.
To start execution of tests type "pytest -v -rA test_task_3.py" from project directory and press enter in terminal. It is recommended to close all other programs and browsers on your computer before executing the test suite.

