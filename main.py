import os
import psycopg2
import pandas as pd

from langchain_community.utilities import SQLDatabase
from langchain.agents import AgentType, tool, create_sql_agent
from langchain_openai import ChatOpenAI


import streamlit as st


os.environ["OPENAI_API_KEY"] = "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"

'''
We sould consider the following elements in url:
+ postgresql+psycopg2: methods to connect database
+ postgres: user name
+ 12345: password
+ localhost: your local host, often be 127.0.0.1 or ::1
+ AAPL: database name
'''
db = SQLDatabase.from_uri("postgresql+psycopg2://postgres:12345@localhost/AAPL")

# Setup agent
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)


# Export response to CSV file if user requests.
@tool
def export_to_csv(question: str, response: str): 
    """
    Export to csv file
    """
    negation_verbs = ["not", "don't", "doesn't", "isn't","aren't","hasn't","haven't","hadn't","won't","wouldn't","shouldn't",
                      "can't","couldn't","mustn't","mightn't","needn't","oughtn't","shan't","wasn't","weren't","didn't", "cannot"]

    words_in_question = question.split(" ")
    if len([word for word in words_in_question if word.lower() in negation_verbs])!=0:
        pass

    if "Let" or "let" not in words_in_question or ("create CSV" or "create csv") not in question:
        pass 
    
    conversation = []
    conversation.append({"Question": question, "Answer": response})
    df = pd.DataFrame(conversation)
    df.to_csv("output.csv", index=False)

# Build SQL agent
agent_executor = create_sql_agent(llm=llm, 
                                  db=db, 
                                  agent_type="openai-tools", 
                                  verbose=True, 
                                  extra_tools = [export_to_csv]
)
#--------------------------------------------------------USER INTERFACE-------------------------------------------------------------
def main():
    st.title("SQL query Generation")
    user_input = st.text_area("Enter your text:", height=200)
    if st.button("Generate SQL"):
        sql_query = agent_executor.run(user_input)
        st.write("Generated SQL Query:")
        st.code(sql_query, language='sql')

if __name__=="__main__":
    main()