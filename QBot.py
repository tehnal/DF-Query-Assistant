import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
import os
import matplotlib as mp
import seaborn as sn

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

df = pd.read_csv("/Users/Teh/Desktop/OpenAIDB/riskdata/application_data.csv")
#df_2 = pd.read_csv("/Users/Teh/Desktop/OpenAIDB/riskdata/previous_application.csv")
#df_3 = pd.read_csv("/Users/Teh/Desktop/OpenAIDB/riskdata/columns_description.csv")

client = OpenAI()
schema = str(df.dtypes)
sample = df.head(3).to_dict()

def ask_qbot(prompt):
    completion = client.chat.completions.create(
    model = "gpt-4o",
    messages = [
        {"role": "system", "content": "You are a data assistant built to assist in any queries I have about a given dataset. You may only answer questions about the data. If you do not know or do not understand, just say so. \
        You will be given a dataset called df: 'application_data.csv'. This contains information about banking loan application data. This excerpt is taken from the source: 'The case study aims to identify patterns which indicate if a client has difficulty paying their installments which may be used for taking actions such as denying the loan, reducing the amount of loan, lending (to risky applicants) at a higher interest rate, etc. This will ensure that the consumers capable of repaying the loan are not rejected. Identification of such applicants using EDA is the aim of this case study.'\
         The dataframe 'df' has the following columns {schema} and some example rows are {sample}.\
        Important rules: Only output valid Python code. Do not include explanations, comments, or markdown formatting. Always assign the final answer to a variable called result.\
        I will ask you questions in plain english, your job is to respond with python code that uses pandas to query the data and obtain the information I want. If I ask for you to include a visualization of the data, use either seaborn or matplotlib to create the visualizations I want. If you can't figure out how to do it, then say so. Only return the python code and nothing else."},
        {"role": "user", "content": prompt}
        ],
    max_tokens = 200,
    temperature = .1,
    )
    code = completion.choices[0].message.content
    if code.startswith("```"):
        code = code.strip("`")        # removes leading/trailing backticks
        code = code.replace("python", "").strip()
    elif code.startswith("'''"):
        code = code.split("'''")[1]
        code = code.replace("python", "").strip()

    local_vars = {"df": df}
    #try:
    exec(code, {}, local_vars)
    result = local_vars.get('result')
    #except Exception as e:
          #return f"Error running query: {e}"
    
    summary_prompt = client.chat.completions.create(
        model = "gpt-4o",
        messages = [
            {"role": "system", "content": str(result)},
            {"role": "user", "content": f"This is the result: {result}. If the result is an image such as a graph or chart, return only the image. If the result is a value, summarize this value in one sentence for a non-technical user."}
            ],
        max_tokens = 150,
        temperature = .1,
        )  
    
    return summary_prompt.choices[0].message.content

#ask_qbot("What is the average loan amount in the dataset 'df'?")

if __name__ == "__main__":
    print("Welcome to DBQbot. How may I be of assistance? Type exit to finish.")

    while True:
        prompt = input("\nAsk a question!")
        if prompt.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        if not prompt.lower():
            print("Enter a valid question!")
            continue
        answer = ask_qbot(prompt)
        print(answer)
