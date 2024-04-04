# SQL_query_Generator
This project is about how to build an AI/LLM agent capable of understanding user's request and responsing to that by querying to SQL database.  
To accomplised this assessment, I referenced the following materials:
- [[SQL agent with Langchain](https://python.langchain.com/docs/use_cases/sql/agents?fbclid=IwAR1feCLF6ocWldzjBo8EeJakpzMdkTAMNManyZrYYcc0qpTN5ZUcGUUuP2A_aem_ATlqnACZkWhVpYBZwDfUc-cQ2SB9Ieo8vBASqm0hosw7Db6hURLY_VkJvwgeT4OswS9TWHL0u9ZC8FvJYwf9Ji_p)]
- [[My best friend - Stackoverflow](https://stackoverflow.com/)]

My solution is to use Langchain to build a SQL agent capable of generating queries and automatically retrieving data from the database to respond to customer requests. All functionalities are supported within the Langchain library with specialized functions for the task. In addition, I have added an extra attribute to my SQL agent, which automatically exports to a CSV file if the user requests it, providing convenience for the customer.

## Knowledge
You need to understand files in this project to better using the repository.
- **data.txt**: containing stock data (AAPL) in one year.
- **postgresql_query.sql**: Setting the environment and creating table for database.
- **main.py**: including the model and UI to interact with agent.
- **test.ipynb**: listing possible situations to test model's performance.
- **setup.txt**: including necessary libraries for executing the program.
- **Dockerfile**: deploying project

## Inference
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

## Configuration
In the **main.py**, you need to put your OpenAI API key to implement LLM from [this](https://openai.com/). Make sure that you have set your account into paid status to be able to request API. Unfortunately, my account has expired a year ago so that I cannot test model's performance. 

Second step is to assign your database url into **db** variable. You could use my url for example. I directly took note the architecture of url in file. 
