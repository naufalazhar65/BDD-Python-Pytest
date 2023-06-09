- Pytest BDD is a library used to write and run automated acceptance tests using natural language. The test cases are written in Gherkin format, which follows the given-when-then structure. There are two feature files, login.feature and checkout.feature, each containing several test cases. These test cases verify various functions on the Saucedemo.com website, such as login, adding items to the cart, checkout, and ensuring that orders are successfully placed or errors occur when entering invalid personal information.

## RUN
```
pytest -s ./tests/test.py    = run with debug
pytest -v ./tests/test.py    = run all test with desc
pytest ./tests/test.py       = run all test
```

<img width="939" alt="Screenshot 2023-04-12 at 17 04 38" src="./assets/test.png">