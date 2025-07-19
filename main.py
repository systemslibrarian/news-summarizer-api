from fastapi import FastAPI
import requests
import openai
import json
import os # Import os for environment variables

app = FastAPI()

# Function to fetch headlines from GNews API
def get_headlines():
    api_key = os.getenv('NEWS_API_KEY') # This variable should now hold your GNews API key
    if not api_key:
        raise Exception("NEWS_API_KEY (GNews API Key) not found in environment variables. Please set it on Render.")

    # Refined GNews API endpoint for top headlines, searching for "AI" specifically
    # Using "artificial intelligence" or "AI" directly might yield better results.
    # We can also try excluding common non-AI tech terms if they keep appearing.
    # For now, let's try a more direct "artificial intelligence" query.
    # GNews 'q' parameter supports exact phrases with quotes.
    url = f"https://gnews.io/api/v4/top-headlines?q=\"artificial intelligence\" OR \"AI\"&lang=en&max=10&token={api_key}"
    
    res = requests.get(url)
    data = res.json()

    if "errors" in data:
        raise Exception(f"Error fetching headlines from GNews: {data['errors']}")

    if not data.get("articles"):
        return []

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

    # We are still sending up to 5 news items to the LLM for summarization
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
        
        # --- REVERTED TO ORIGINAL FUNCTIONALITY ---
        summary = summarize_news(headlines)
        return {"summary": summary}
        # --- END REVERTED CHANGE ---

    except Exception as e:
        return {"error": str(e)}

