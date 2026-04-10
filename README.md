# 🧠 Opinion AI: Public Opinion Tracker

**Opinion AI** is a sophisticated, AI-powered sentiment analysis tool that leverages Google's **Gemini** to provide deep insights into public opinion on any given topic. By synthesizing data from multiple sources, it offers a comprehensive view of sentiment, social impact, and key arguments.

---

## ✨ Features

- **📊 Real-time Sentiment Analysis**: Get an instant breakdown of positive, negative, and neutral sentiments visualized with dynamic Chart.js doughnut charts.
- **🚀 Key Insights Extraction**: Automatically identifies the most significant positive outcomes and critical concerns related to your topic.
- **🌍 Social Impact Analysis**: Provides a detailed 150-word report on the broader societal implications of the public's stance.
- **📝 Executive Summary**: A concise, AI-generated conclusion summarizing the current landscape of public opinion.
- **🔗 Verified Sources**: Includes links and names of primary sources used to synthesize the analysis, ensuring transparency.
- **💎 Premium Design**: A modern, glassmorphic UI built with vanilla CSS, featuring smooth animations and a responsive layout.

---

## 🛠️ Technology Stack

### Frontend
- **HTML5 & CSS3**: Custom-built responsive layout with glassmorphism effects.
- **JavaScript (ES6+)**: Core logic and asynchronous API handling.
- **Chart.js**: Dynamic data visualization.
- **Google Fonts**: Poppins for a modern typography feel.

### Backend
- **Python**: Core backend language.
- **Flask**: Lightweight web framework for the API.
- **Flask-CORS**: Handling cross-origin requests.
- **Google Generative AI SDK**: Powering the analysis with Gemini 1.5 Pro.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js (for serving the frontend)
- A Google Gemini API Key

---

## 📂 Project Structure

```text
.
├── backend/
│   ├── app.py              # Flask API entry point
│   ├── gemini_helper.py    # AI logic and Gemini integration
│   ├── .env                # API Keys (Git ignored)
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── index.html          # Main landing page
│   ├── styles.css          # Premium glassmorphic styling
│   ├── script.js           # Frontend logic & API calls
│   └── assets/             # Images and icons
├── netlify.toml            # Deployment configuration
├── package.json            # NPM scripts for building/serving
└── README.md               # Project documentation
```

---
