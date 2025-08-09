from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from config import CONTEXT_COLUMNS

def get_llm_chain():
    prompt = PromptTemplate(
        input_variables=["store", "date", "sales", "context"],
        template="""
You are a retail analytics expert helping to explain unusual sales patterns.

Store ID: {store}
Date: {date}
Sales: {sales}

Context:
{context}

Explain why this data point might be an outlier.
"""
    )

    llm = Ollama(model="llama3")  # You must have llama3 running via `ollama run llama3`
    return LLMChain(llm=llm, prompt=prompt)

def explain_outliers(df):
    chain = get_llm_chain()
    explanations = []

    for _, row in df[df['is_outlier']].iterrows():
        context_info = "\n".join([f"{col.capitalize()}: {row[col]}" for col in CONTEXT_COLUMNS])
        context_info += f"\nInventory: {row['inventory']}\nPrice: {row['price']}"

        explanation = chain.run(
            store=row['store_id'],
            date=row['date'].strftime('%Y-%m-%d'),
            sales=row['sales'],
            context=context_info
        )
        explanations.append(explanation.strip())

    df.loc[df['is_outlier'], 'llm_reason'] = explanations
    return df
