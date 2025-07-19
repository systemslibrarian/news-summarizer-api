
from fastapi import FastAPI
import requests
import openai
import json
from google.colab import userdata

app = FastAPI()

# Include your get_headlines and summarize_news functions here
def get_headlines():
    api_key = userdata.get('NEWS_API_KEY') # Assuming you named your secret NEWS_API_KEY
    if not api_key:
      # In a deployed environment, you would typically read from environment variables
      import os
      api_key = os.getenv('NEWS_API_KEY')
      if not api_key:
        raise Exception("NEWS_API_KEY not found in environment variables.")

    url = f"https://newsapi.org/v2/top-headlines?q=rare earth materials&apiKey={api_key}" # Use the API key from secrets and 'q' for keyword search
    res = requests.get(url)
    data = res.json()

    if data["status"] == "error":
        raise Exception(f"Error fetching headlines: {data['message']}")

    return [article["title"] + ": " + article["description"] for article in data["articles"]]

def summarize_news(news_items):
    openai_api_key = userdata.get('OPENAI_API_KEY') # Assuming you named your secret OPENAI_API_KEY
    if not openai_api_key:
      # In a deployed environment, you would typically read from environment variables
      import os
      openai_api_key = os.getenv('OPENAI_API_KEY')
      if not openai_api_key:
        raise Exception("OPENAI_API_KEY not found in environment variables.")

    prompt = "Summarize these tech news items:

" + "
".join(news_items[:5])
    client = openai.OpenAI(api_key=openai_api_key) # Initialize the OpenAI client with the API key
    response = client.chat.completions.create( # Use the new chat completions method
        model="gpt-3.5-turbo", # Changed model to gpt-3.5-turbo
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content


@app.get("/")
def read_root():
    return {"message": "Welcome to the news summarizer API!"}

@app.get("/summarize")
def get_summary():
    try:
        headlines = get_headlines()
        summary = summarize_news(headlines)
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}
