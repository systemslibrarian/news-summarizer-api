# News Summarizer API

This is a simple FastAPI application that fetches top headlines related to "Rare Earth Materials" using the News API and summarizes them using the OpenAI API.

## Features

*   Fetches top news headlines on a specific topic.
*   Summarizes the fetched news articles using a language model.
*   Provides a simple API endpoint to access the summary.

## Prerequisites

Before running or deploying this application, you will need:

*   An API key from [News API](https://newsapi.org/).
*   An API key from [OpenAI](https://openai.com/).
*   Python 3.7+ installed.
*   `pip` for installing dependencies.

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Set environment variables:**

    ```env
    NEWS_API_KEY=your_news_api_key
    OPENAI_API_KEY=your_openai_api_key
    ```
    *Replace `your_news_api_key` and `your_openai_api_key` with your actual keys. For deployment, you will set these in your hosting provider's settings.*

4.  **Run the application locally:**

    ```bash
    uvicorn main:app --reload
    ```

## Deployment to Render

Follow the steps outlined previously, ensuring you set your `NEWS_API_KEY` and `OPENAI_API_KEY` as environment variables in your Render service settings.

## Usage

Once deployed, you can access the summary by sending a GET request to the `/summarize` endpoint of your service:

```bash
curl your_render_service_url/summarize
