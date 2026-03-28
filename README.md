Blame
🧠 AI News Navigator
Transforming overwhelming news streams into personalized AI-powered insights using FastAPI, Gemini AI, and real-time data processing.

🚀 Overview
AI News Navigator is an AI-powered web application that fetches real-time news based on user interests and generates concise AI summaries using Google Gemini.

Instead of reading long articles, users receive personalized, short, and intelligent summaries instantly.

This project was developed as part of an AI Hackathon to demonstrate the integration of:

Generative AI
REST APIs
Cloud Deployment
Modern Interactive UI
✨ Features
✅ Personalized news based on user interest
✅ AI-generated summaries using Gemini AI
✅ Real-time news fetching
✅ FastAPI backend (REST architecture)
✅ Premium Streamlit UI
✅ Cloud deployment on Render
✅ Error handling & timeout protection

🏗️ System Architecture
User Browser ↓ Streamlit Frontend ↓ HTTP Request FastAPI Backend (Render) ↓ News API + Gemini AI ↓ Processed JSON Response ↓ Interactive UI Display

🧩 Tech Stack
Frontend
Streamlit
Python Requests
Custom CSS UI
Backend
FastAPI
Uvicorn Server
REST API Design
AI
Google Gemini API (Generative AI)
Data Source
News API (Real-time headlines)
Deployment
Render (Cloud Hosting)
📁 Project Structure
AI-News-Navigator/ │ ├── main.py # FastAPI backend ├── News.py # News API integration ├── Ai.py # Gemini AI summarization ├── personalization.py # News filtering logic ├── frontend.py # Streamlit frontend UI ├── requirements.txt └── README.md

3️⃣ Backend Processing
Fetches live news articles
Filters relevant content
Sends article descriptions to Gemini AI
4️⃣ AI Summarization
Gemini generates short summaries.

5️⃣ Response
Backend returns structured JSON.

6️⃣ UI Rendering
Frontend displays premium news cards.

🔄 Workflow
Button Click → API Call → Fetch News → AI Summarization → JSON Response → Frontend Rendering
