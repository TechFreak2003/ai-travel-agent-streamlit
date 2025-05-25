# 🌍 AI Travel Agent

Your personalized AI-powered travel companion that recommends destinations, plans itineraries, and answers travel-related queries in real time.

<p align="center">
  <img src="https://github.com/TechFreak2003/ai-travel-agent-streamlit/blob/main/public/header_image.png" alt="AI Travel Agent Banner" />
</p>

<p align="center">
  <a href="https://github.com/TechFreak2003/ai-travel-agent-streamlit/issues"><img src="https://img.shields.io/github/issues/TechFreak2003/ai-travel-agent-streamlit"></a>
  <a href="https://github.com/TechFreak2003/ai-travel-agent-streamlit/stargazers"><img src="https://img.shields.io/github/stars/TechFreak2003/ai-travel-agent-streamlit"></a>
  <a href="https://github.com/TechFreak2003/ai-travel-agent-streamlit/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg">
  </a>
</p>

<p align="center">
  <a href="#-features">Features</a> |
  <a href="#%EF%B8%8F-tech-stack">Tech Stack</a> |
  <a href="#-installation">Installation</a> |
  <a href="#-project-structure">Project Structure</a> |
  <a href="#-contributing">Contributing</a> |
  <a href="#%EF%B8%8F-author">Author</a>
</p>

<p align="center">
  <img src="https://github.com/TechFreak2003/ai-travel-agent-streamlit/blob/main/public/demo.gif" alt="Usage Demo">
</p>

## 🌟 Features

* Interactive chat-based travel assistant powered by OpenAI GPT-4
* Destination discovery and suggestions with real-time input
* Personalized itinerary planning
* Real-time conversational memory using LangChain
* Clean and responsive Streamlit interface

## 🛠️ Tech Stack

* **Frontend Framework**: Streamlit
* **AI Model**: OpenAI GPT-4
* **LLM Framework**: LangChain
* **Environment Handling**: `python-dotenv`
* **Backend Logic**: Python

## 🚀 Installation

### Requirements 📋

* Python 3.9+
* OpenAI API Key

### Getting Started 📜

1. **Clone the repository**:

```bash
git clone https://github.com/TechFreak2003/ai-travel-agent-streamlit.git
cd ai-travel-agent-streamlit
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Set up environment variables**:

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your-openai-api-key
```

4. **Run the application**:

```bash
streamlit run app.py
```

## 📁 Project Structure

```
ai-travel-agent-streamlit/
├── app.py
├── .env                # (not pushed to GitHub)
├── requirements.txt
├── agents/
│   ├── agent.py
│   └── tools/
│       ├── flights_finder.py
│       └── hotels_finder.py
```

## 👥 Contributing

Contributions are welcome! Please fork this repo and open a pull request with your changes.

* Bug fixes
* New travel features (e.g., budget estimation, weather integration)
* UI/UX enhancements

## 👨‍💻 Author

| Avatar                                                                       | Name          | GitHub                                            | Role                 | Contributions                                    |
| ---------------------------------------------------------------------------- | ------------- | ------------------------------------------------- | -------------------- | ------------------------------------------------ |
| <img src="https://github.com/TechFreak2003.png" width="50px" height="50px"/> | Suvrodeep Das | [TechFreak2003](https://github.com/TechFreak2003) | Creator & Maintainer | Core logic, Streamlit integration, Documentation |

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> Crafted with ❤️ by Suvrodeep Das
