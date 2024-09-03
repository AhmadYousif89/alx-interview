# Starwars API Task

![Starwars image](https://ph-files.imgix.net/62758740-d453-4296-ac77-4eea57732bd5.png?auto=format&fit=crop)

## Introduction

- In this task, we will be using the [ALX Starwars API](https://swapi-api.alx-tools.com/api) to get information about the Starwars movies and their characters, one character name per line in the same order as the “characters” list in the [/films/ endpoint](https://swapi-api.alx-tools.com/api/films/).

- The script utilizes the [requests](https://docs.python-requests.org/en/master/) library to make HTTP requests to the API and fetch the required data and the **util** module to convert the request module into a promise-based module and handle the asynchronous nature of the requests using the **async/await** syntax.

## Usage

The script is written in JavaScript and can be run using the Node.js runtime environment.

The script can be executed using the following command:

```sh
$ node 0-starwars_characters.js [film_id]
```

or with direct execution permission:

```sh
$ ./0-starwars_characters.js [film_id]
```

## Example

```sh
$ node 0-starwars_characters.js 1

Luke Skywalker
C-3PO
R2-D2
Darth Vader
... // Remaining characters
```

### Programing Concepts Used

- **Working with APIs**: The script demonstrates how to work with APIs and fetch data from them using HTTP requests.

- **HTTP Requests**: The script uses the **requests** library to make HTTP requests to the API and fetch the required data. The **axios** library is used to make the HTTP requests.

- **JSON Parsing**: The script uses the **JSON.parse()** method to parse the JSON response received from the API and extract the required data.

- **Async/Await**: The **async/await** syntax is used to handle the asynchronous nature of the requests made to the API. The **await** keyword is used to pause the execution of the function until the promise is resolved.

- **Error Handling**: The script uses **try/catch** blocks to handle errors that may occur during the execution of the program. The **catch** block is used to catch any errors that occur during the execution of the **async** function.

- **Command-Line Arguments**: The script uses the **process.argv** array to access the command-line arguments passed to the script. The **film_id** is passed as a command-line argument to the script.

- **Array Manipulation and Iteration**: The script uses array manipulation and iteration to extract the character names from the JSON response and print them to the console.
