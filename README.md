### Project Structure

![Settings Window](https://github.com/MandaGayatri/WebScraping_Assignment/blob/main/assignment.PNG)


### Approach:

## Project Structure:

### Python Files:

LinkTest.py: Extracts all links present in the given Web Page.

ModelUsed.py: Extracts the model used data from givenWebPage.

Generationparameters.py:Extracts the GenerationParameters data from givenWebPage .

PromptContent.py: Extracts all lines where the line contains prompt word from givenWebPage.

UserName.py : Extracts UserName from given WebPage.

ExtractedFile.py: Contains functions to extract information from files.

LoginPage.py: Implements user login functionality for givenWebPage

### Pytest Files

test_GenerationParameters.py: Contains pytest test cases for Generationparameters.py.

test_LinkTest.py: Contains pytest test cases for LinkTest.py.

test_ModelUsed.py: Contains pytest test cases for ModelUsed.py.

test_PromptContent.py: Contains pytest test cases for PromptContent.py.

test_UserName.py: Contains pytest test cases for UserName.py.

## Automation Process:

For each module (generation parameters, link testing, model used, prompt content, and user name), there are corresponding Python files containing functions to interact with the web application and perform the 

required actions.

For each module, there are also separate test files that use pytest to run test cases against the functions in the corresponding Python files.

Selenium is used to interact with the web application, simulate user actions, and validate expected outcomes.

### Challenges Faced and Solutions Implemented:

Dynamic Content: The web application  has dynamically changing content, making it challenging to write stable tests.

Solution:  Used waits in Selenium to ensure elements are loaded before interacting with them.

Test Data Management: Managing test data and configuration files for different modules  are complex.

Solution: Keeping sample data or configuration files separate and version-controlled. Used proper file-naming conventions for clarity.

Conclusion:

 The automation project successfully utilizes Python, pytest, and Selenium to automate testing for various modules of the web application. 
 
 By structuring the project effectively and using proper automation techniques, challenges related to dynamic content and test data management are addressed.

### Output
![Settings Window]( https://github.com/MandaGayatri/WebScraping_Assignment/blob/main/testpass.PNG)
