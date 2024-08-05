# Python API Automation Framework
### Tech Stack - Libraries
- Python 3.12
- Requests - HTTP Requests
- PyText - Testing Framework
- Reporting - Allure Report, PyTest HTML
- Test Data - CSV, Excel, JSON, Faker (for dummy data, a python library)
- Advance API Testcase - jsonschema
- Parallel Execution - x distribute (xdist) - parallel execution

### How to Install Packages
```pip install requests pytest pytest-html faker allure-pytest jsonschema```

### How to run your Testcases in Parallel
```pip install pytest-xdist```

### How to add the -gitignore file?

Copy the content from this to .gitignore file
https://www.toptal.com/developers/gitignore/api/pycharm+all

### How to run the basic test case with allure report before pushing code to github
 ``` pytest tests/test_create_booking.py  --alluredir=allure_result -s ```
