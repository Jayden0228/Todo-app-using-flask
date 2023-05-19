# Flask Todo App

This is a simple Todo app built using Flask, where users can manage their todos. The app provides functionality to add, read, update, and delete todos. Additionally, users can filter todos based on a substring they enter.



## Features

- Add a Todo: Users can add new todos by providing a title and description.
- Read a Todo: Users can view all existing todos, including their titles and descriptions.
- Update a Todo: Users can update the title and description of an existing todo.
- Delete a Todo: Users can delete a todo from the list.
- Filter Todos: Users can filter todos based on a substring they enter, allowing them to search for specific todos.

## Prerequisites

Python 3.x
Flask framework
Flask SQLAlchemy (for database integration)

## Getting Started

- Clone the repository: git clone https://github.com/Jayden0228/flask-todo-app.git
- Install the required dependencies: pip install -r requirements.txt
- Start the Flask development server: flask run
- Access the Todo app in your web browser at http://localhost:5000.

## Project Structure

The project directory contains the following main files and directories:
- app.py: The main Flask application file that defines the routes, Todo model and database schema using Flask SQLAlchemy.
- templates/: Contains HTML templates for rendering the web pages.
- static/: Stores static files like CSS stylesheets and JavaScript files.

## Usage

- Add a Todo: On the homepage, enter the title and description of the todo in the provided input fields. Click the "Add Todo" button to create the todo.
- Read a Todo: The homepage displays a list of all existing todos. Each todo shows its title, description, and options to update or delete it.
- Update a Todo: To update a todo, click the "Update" button next to the todo you wish to modify. Update the title and description, then click "Save Changes".
- Delete a Todo: To delete a todo, click the "Delete" button next to the todo you want to remove.
- Filter Todos: Enter a substring in the filter input field at the top of the homepage. The list of todos will be filtered based on the entered substring.

You can also access the live demo of the app at [http://jaydenviegas.pythonanywhere.com](http://jaydenviegas.pythonanywhere.com).

## License

This project is licensed under the MIT License.

## Acknowledgements

This Todo app was inspired by the Flask framework and the need for a simple task management tool. Special thanks to the Flask community for their valuable resources and support.

Feel free to customize and enhance the app as per your requirements. Happy coding!
