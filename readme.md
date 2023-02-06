# The following video shows the working of bot:

https://user-images.githubusercontent.com/65712331/217036148-222fe7ad-b5c2-497e-a664-029c2a73f681.mp4

# Task Manager Documentation

This script uses the Firebase Realtime Database to store and manage task information.

## Initialization

The script starts by importing the firebase_admin library, as well as two sub-libraries from it: credentials and db. It then loads the credentials from a key.json file and initializes a Firebase app with the provided `databaseURL`.

A reference to the root of the database is created and checked to see if it is empty. If it is, a default value of `{"Tasks":[]}` is set. Finally, a reference to the `/Tasks` node is created.

## Functionality

The script provides several functions to interact with the Firebase database:

- `addTasks(tasks)`: Adds tasks to the database. The `tasks` argument should be a string of comma-separated task names. The function splits the string into separate tasks, removes any whitespace, and stores each task as a dictionary in the Firebase database under the `/Tasks` node.
- `showData()`: Returns a string of all the tasks in the database, grouped by whether they have been completed or not.
- `DeleteData(number)`: Deletes the task with the specified number (1-based).
- `MarkTask(num)`: Marks the task with the specified number (1-based) as done.
- `QueryResponse(query)`: A function that serves as the main interface for using the script. The function takes a string query and performs the corresponding action based on the first word in the query. Valid commands are "ADD", "SHOW", "DELETE", "MARK", and "HELP".

## Usage

To use the script, simply call the `QueryResponse` function with a string containing the desired command and any necessary arguments.
