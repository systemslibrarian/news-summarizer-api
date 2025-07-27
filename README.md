# 📰 News Summarizer API

A lightweight, FastAPI-based microservice that fetches the latest headlines on **AI news** from the GNews API and summarizes them using OpenAI’s language models.

---

## 🚀 Features

- 🔍 Fetches top news headlines related to a specific topic (`AI news` by default)
- 🧠 Generates concise summaries using the OpenAI API
- 📡 Exposes a simple REST API endpoint for summary retrieval

---

## 🧱 Prerequisites

Before running this project, you’ll need:

- ✅ A **GNews API Key** – [https://gnews.io](https://gnews.io)
- ✅ An **OpenAI API Key** – [https://platform.openai.com](https://platform.openai.com)
- ✅ Python 3.7+
- ✅ `pip` for managing dependencies

---

## ⚙️ Setup & Installation

Clone the repository:

```bash
git clone https://github.com/your-username/news-summarizer-api.git
cd news-summarizer-api
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file (or export environment variables directly):

```env
NEWS_API_KEY=your_gnews_api_key
OPENAI_API_KEY=your_openai_api_key
```

Replace `your_gnews_api_key` and `your_openai_api_key` with your actual keys.

---

## ▶️ Running Locally

Launch the FastAPI app using Uvicorn:

```bash
uvicorn main:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs) to explore the Swagger UI.

---

## 🌐 Deployment (e.g., Render.com)

1. Push your code to GitHub
2. Create a new **Web Service** on [Render.com](https://render.com)
3. Set your environment variables in the Render dashboard:
   - `NEWS_API_KEY`
   - `OPENAI_API_KEY`

Render will automatically detect and deploy your FastAPI service.

---

## 📡 Example Usage

Once deployed, retrieve the summarized AI news by sending a request to:

```bash
curl https://your-service.onrender.com/summarize
```

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE).
