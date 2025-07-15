# 🛒 Wally - Smart Retail Assistant for Walmart

Wally is an intelligent, AI-powered personal shopping assistant designed specifically for Walmart users. It helps monitor purchase behavior, reminds users to restock essentials, and offers a personalized shopping experience by leveraging local data and smart prompts.

## 📌 One-Line Summary

Wally is a custom AI assistant that reminds users to restock frequently purchased items and enhances the Walmart shopping experience.


## 🚩 Problem Statement

Walmart customers often forget to restock daily-use or recurring items (like groceries, toiletries, etc.), leading to shopping delays or inefficiencies. Additionally, existing shopping apps lack personalized assistant features that predict user needs based on previous purchase behavior.


## 💡 Our Solution

RetailX uses a local AI assistant (powered by Ollama LLM) to:

- Track frequently bought items
- Set smart restock reminders
- Provide shopping suggestions
- Offer seamless integration with Walmart's ecosystem

All through a lightweight, private, and user-friendly interface.


## ⚙️ Features

- 🧠 AI-Powered Personal Assistant (Named **Wally**)
- ⏰ Smart Reminder System for Recurring Purchases
- 🛍️ Item Monitoring & History Tracker
- 📊 Custom Data Dashboard for User Insights
- 🌐 Built for Walmart Ecosystem


## 🧱 Tech Stack

| Component         | Technology             |
|------------------|------------------------|
| Frontend         | Streamlit (Python)     |
| Backend AI       | Ollama LLM (Local AI)  |
| Database         | Local JSON/CSV storage |
| Deployment       | Local/Desktop App      |
| Target Platform  | Walmart Shopping Users |


## 🧑‍💻 Installation & Setup

1. **Clone the repository**
   ```
   /retailx.git
   cd retailx
```

2. **Install dependencies**

   ```
   pip install -r requirements.txt
   ```

3. **Install Ollama and setup your LLM**

   * Follow instructions at [https://ollama.ai](https://ollama.ai) to install and run the model locally.

4. **Run the app**

   ```
   streamlit run app.py
   ```

## 🧠 Assistant – Wally

Wally is the smart AI persona integrated into RetailX. It understands user queries, offers product insights, and reminds users when they're about to run out of essentials. Trained on localized prompts for Walmart use cases.

## 🚀 Future Scope

* Integration with live Walmart APIs
* Voice-command support
* Cloud sync and login-based personalization
* Android/iOS companion app


* KK (Keerthi Kireeti) – Lead Developer & AI Integration
