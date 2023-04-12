- Pytest BDD is a library used to write and run automated acceptance tests using natural language. The test cases are written in Gherkin format, which follows the given-when-then structure. There are two feature files, login.feature and checkout.feature, each containing several test cases. These test cases verify various functions on the Saucedemo.com website, such as login, adding items to the cart, checkout, and ensuring that orders are successfully placed or errors occur when entering invalid personal information.

#RUN
- pytest -p no:warnings -s -v ./tests/test.py

<img width="939" alt="Screenshot 2023-04-12 at 17 04 38" src="https://user-images.githubusercontent.com/123730742/231425775-fa845290-369f-4892-8749-d5dd4566cf06.png">