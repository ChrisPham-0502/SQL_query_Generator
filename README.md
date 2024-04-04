# SQL_query_Generator
This project is about how to build an AI/LLM agent capable of understanding user's request and responsing to that by querying to SQL database.  
To accomplised this assessment, I referenced the following materials:
- [[SQL agent with Langchain](https://python.langchain.com/docs/use_cases/sql/agents?fbclid=IwAR1feCLF6ocWldzjBo8EeJakpzMdkTAMNManyZrYYcc0qpTN5ZUcGUUuP2A_aem_ATlqnACZkWhVpYBZwDfUc-cQ2SB9Ieo8vBASqm0hosw7Db6hURLY_VkJvwgeT4OswS9TWHL0u9ZC8FvJYwf9Ji_p)]
- [[My best friend - Stackoverflow](https://stackoverflow.com/)]

## Installization
1. Clone the repository

  If you just want to run it locally, you only git clone this repo first.
```sh
https://github.com/ChrisPham-0502/SQL_query_Generator.git
```
  Then, install some necessary libraries:
```sh
pip install -r setup.txt
```
  Finally, run the main file
```sh
python main.py
```
2. Build with Docker

  First, you still need git clone the repository by the above command. Then, you run the following command:
 ```sh
docker build -t sql_generation .
```
  Make sure that you have already installed Docker desktop to smootly execute the above command. After finishing creating docker image, you will run the docker to start the program: 
```sh
docker run -p yourlocalhost:8080 sql_generation
```
