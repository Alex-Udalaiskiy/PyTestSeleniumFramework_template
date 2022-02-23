Introduction
------------

This repository contains common test framework for web automation.
It is implemented pageObject pattern with Selenium and Python (PyTest + Selenium).

Files
-----

[conftest.py] here implemented getting Web Driver from Web Driver Manager Pytest extension. 
Also this section contains all the required code to catch failed test cases and make screenshot
of the page in case any test case will fail.

[baseUtils/base_page.py] contains PageObject pattern
implementation for Python. This implemented  common methods to work with the page objects.

[baseUtils/elements.py] contains helper class to define and work with  web elements on the web pages.

[test] contains directly tests. All test files should start with 'test_'

How To Run Tests
----------------

1) Install all requirements:
    
   '''bash
   pip3 install -r requirements.txt
   '''
   ''' win cmd
   pip install -r requirements.txt
   '''
2) Run tests:
  2.1 You can run all test. Go to the project directory
       and type:
       ''' pytest -v ''' or 
       ''' python -m pytest -v '''
  2.2 Or you can Run only test you want:
      ''' pytest -v tests\test_....py
           
       