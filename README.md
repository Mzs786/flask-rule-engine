# Flask Rule Engine

A simple rule engine built with Flask and MongoDB to evaluate custom rules against user-defined data.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Design Choices](#design-choices)
- [Installation](#installation)
- [Usage](#usage)
- [Sample Rules](#sample-rules)
- [Sample Data for Evaluation](#sample-data-for-evaluation)
- [Expected Results for Each Rule](#expected-results-for-each-rule)
- [How to Test](#how-to-test)
- [Contributing](#contributing)
- [License](#license)

## Features

- Create and evaluate complex rules using a simple frontend.
- Store and retrieve rules in a MongoDB database.
- Support for logical operators (AND, OR) and comparisons (>, <, ==).
- Easy to use and extend with new features.

- 
## Technologies Used

- **Flask**: A micro web framework for Python, used for building the web application.
- **MongoDB**: A NoSQL database for storing rules and related data.
- **HTML/CSS/JavaScript**: For the frontend interface, providing a user-friendly experience.


## Design Choices

1. **Microservices Architecture**: The project is structured as a microservice using Flask, which allows for scalability and maintainability. Each component can be developed and tested independently.

2. **MongoDB for Storage**: MongoDB is chosen for its flexibility in handling unstructured data, which is essential for storing various rules. Its NoSQL nature allows for easy scaling and quick retrieval of documents.

3. **Rule Parsing Logic**: The rule evaluation engine uses a simple parser to convert rules from string format into a structured format (AST) for evaluation. This design allows for easy extensions in rule complexity.

4. **Frontend**: A straightforward HTML/CSS/JavaScript frontend is created for ease of use, enabling users to input rules and see evaluations without navigating through complex interfaces.

5. **RESTful API**: The application follows RESTful principles for its API design, making it intuitive for clients to interact with the backend.



## Installation

1. **Clone the repository**:
   ```
   https://github.com/user/repo.git
   ```
2.Navigate to the project directory:
```
cd flask-rule-engine
```
3.Set up a virtual environment:
```
python -m venv venv
```
4.Activate the virtual environment:

* On Windows:
  ```
  venv\Scripts\activate
  ```
* On macOS/Linux:
  ```
  source venv/bin/activate
  ```
5.Install the required packages:
```
pip install -r requirements.txt
```
6.Start MongoDB (make sure MongoDB is running):
```
mongod
```
7.Run the Flask application:
```
python app.py
```

The application will be available at http://127.0.0.1:5000.

Usage

Open your web browser and go to http://127.0.0.1:5000.
Input a rule in the text area provided.
Click the "Evaluate Rule" button to see the evaluation results.

Sample Rules
Rule 1
```
((age > 30 AND department == 'Sales') OR (age < 25 AND department == 'Marketing')) AND (salary > 50000 OR experience > 5)
```
Description: This rule checks if:

*The age is greater than 30 and the department is 'Sales', or
*The age is less than 25 and the department is 'Marketing', and
*Either the salary is greater than 50,000 or the experience is greater than 5 years.

Rule 2
```
((age > 30 AND department == 'Marketing')) AND (salary > 20000 OR experience > 5)
```
Description: This rule checks if:
The age is greater than 30 and the department is 'Marketing', and
Either the salary is greater than 20,000 or the experience is greater than 5 years.

Rule 3
```
(age < 30 AND department == 'Sales') OR (salary <= 40000 AND experience < 3)
```
Description: This rule checks if:
The age is less than 30 and the department is 'Sales', or
The salary is less than or equal to 40,000 and the experience is less than 3 years.

Sample Data for Evaluation
You can use the following sample data to evaluate the above rules:
json
```
{
    "age": 32,
    "department": "Sales",
    "salary": 60000,
    "experience": 6
}
```

Expected Results for Each Rule

For Rule 1:
Evaluation: True
Reason: The first part (age > 30 AND department == 'Sales') is true because the age is 32 and the department is 'Sales'. The second part (salary > 50000 OR experience > 5) is also true because the salary is 60000, so the entire rule evaluates to true.
For Rule 2:

Evaluation: False
Reason: The first part (age > 30 AND department == 'Marketing') is false because the department is 'Sales', so the whole rule evaluates to false.
For Rule 3:

Evaluation: False
Reason: The first part (age < 30 AND department == 'Sales') is false because the age is 32. The second part (salary <= 40000 AND experience < 3) is also false because the salary is 60000 and experience is 6. Therefore, the entire rule evaluates to false.

How to Test

Select or Input Rule: Choose one of the sample rules from the dropdown menu or input it manually into the textarea on the frontend.
Click Evaluate: Click the "Evaluate Rule" button to see the results displayed.

The application will run on http://127.0.0.1:5000.

Test the Endpoints: You can use curl or Postman to test the endpoints. Below are some examples:

Create a Rule:
```
curl -X POST http://127.0.0.1:5000/create_rule -H "Content-Type: application/json" -d "{\"rule\": \"age > 30 AND department == 'Sales'\"}"
```
Evaluate a Rule:
```
curl -X POST http://127.0.0.1:5000/evaluate_rule -H "Content-Type: application/json" -d "{\"ast\": { ... }, \"data\": { \"age\": 35, \"department\": \"Sales\", ... }}"
```
Combine Rules:
```
curl -X POST http://127.0.0.1:5000/combine_rules -H "Content-Type: application/json" -d
```

Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please make sure to follow the existing code style and include tests for any new features or bug fixes.

License
This project is licensed under the MIT License. See the LICENSE file for more information.
  
