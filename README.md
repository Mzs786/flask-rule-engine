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
