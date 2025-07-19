from fastapi import FastAPI
import requests
import openai
import json
import os # Import os for environment variables

app = FastAPI()

# Function to fetch headlines from GNews API
def get_headlines():
    # Retrieve GNews API key from environment variables
    api_key = os.getenv('NEWS_API_KEY') # This variable should now hold your GNews API key
    if not api_key:
        raise Exception("NEWS_API_KEY (GNews API Key) not found in environment variables. Please set it on Render.")

    # GNews API endpoint for top headlines, searching for "AI news"
    # The 'lang' parameter specifies the language (en for English)
    # The 'max' parameter specifies the maximum number of articles to return
    url = f"https://gnews.io/api/v4/top-headlines?q=AI news&lang=en&max=10&token={api_key}"
    
    res = requests.get(url)
    data = res.json()

    # GNews API uses 'errors' key for error messages, not 'status' == 'error'
    if "errors" in data:
        raise Exception(f"Error fetching headlines from GNews: {data['errors']}")

    # GNews API returns articles under the 'articles' key
    if not data.get("articles"):
        return []

    # Extract title and description from GNews articles
    # GNews articles have 'title' and 'description' fields directly
    headlines = []
    for article in data["articles"]:
        title = article.get("title", "")
        description = article.get("description", "")
        if title and description: # Only add if both title and description exist
            headlines.append(f"{title}: {description}")
    
    return headlines

# Function to summarize news using OpenAI API (remains the same)
def summarize_news(news_items):
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        raise Exception("OPENAI_API_KEY not found in environment variables. Please set it on Render.")

    prompt = "Summarize these tech news items:\n" + "\n".join(news_items[:5])
    
    client = openai.OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content

# FastAPI endpoints
@app.get("/")
def read_root():
    return {"message": "Welcome to the news summarizer API!"}

@app.get("/summarize")
def get_summary():
    try:
        headlines = get_headlines()
        if not headlines:
            return {"summary": "No news items found to summarize."}
        summary = summarize_news(headlines)
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}

