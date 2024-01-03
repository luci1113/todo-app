# To-Do List with GraphQL API calls

This is a simple To-Do Flask web application that uses Keycloak for authentication. Users can log in and add a to-do with a title, description, and time. All API calls are handled by GraphQL. There is also an option to buy a Pro license that enables users to upload images in To-Do as well.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have the following installed on your system:

- Python 3.6+
- pip

### Installing

Clone the repository:

```
git clone https://github.com/yourusername/todo-app.git
```



Install the required packages:

```
pip install -r requirements.txt
```

### Running the application

To run the application, execute:

```
python run.py
```

## Project Structure

The project has the following structure:

- `requirements.txt`: Contains all the python packages that need to be installed.
- `app.py`: The main entry point of the application.
- `models.py`: Contains the SQLAlchemy models.
- `auth.py`: Handles the authentication using Keycloak.
- `schema.py`: Contains the GraphQL schema.
- `resolvers.py`: Contains the GraphQL resolvers.
- `pro_features.py`: Handles the Pro features.
- `config.py`: Contains the configuration variables.
- `run.py`: Script to run the application.
- `README.md`: Documentation of the project.

## Built With

- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
- [GraphQL](https://graphql.org/) - API query language
- [Keycloak](https://www.keycloak.org/) - Open Source Identity and Access Management

## Authors

- Nirmal Avhad

