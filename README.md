
🎓 AI-Powered E-Learning FAQ Chatbot
An intelligent FAQ assistant built with Python, Flask, and Natural Language Processing (NLP). This chatbot helps students get instant answers about courses, exams, fees, and technical issues using Cosine Similarity to understand intent rather than just keywords.

🌟 Key Features
Semantic Search: Uses TF-IDF Vectorization and Cosine Similarity to find the closest match to a user's question.

Confidence Scoring: Includes a threshold mechanism (0.2) to identify when a question is outside the bot's knowledge base.

RESTful API: The backend serves as a JSON API, making it compatible with Postman or mobile apps.

Responsive UI: A clean, modern chat interface for a seamless student experience.

🏗️ The Tech Stack
Language: Python 3.10+

Web Framework: Flask

Machine Learning: Scikit-learn (for text vectorization)

Frontend: HTML5, CSS3, JavaScript (Fetch API)

Data Storage: JSON

⚙️ How It Works
The chatbot follows a "Vector Space Model" approach:

Dataset: Questions are stored in faq_data.json.

Vectorization: Text is converted into numerical vectors using TF-IDF (Term Frequency-Inverse Document Frequency).

Comparison: When a user types a query, it is compared against all stored questions using Cosine Similarity.

Selection: The bot picks the answer with the highest mathematical similarity.

🚀 Installation & Setup
1. Prerequisites
Ensure you have Python installed. Check using python --version.

2. Clone and Install
Bash

# Clone the repository
git clone https://github.com/PruthvirajMane-10/Basic-AI-ChatBot.git
cd Basic-AI-ChatBot

# Install required libraries
pip install flask scikit-learn numpy
3. Project Structure
Ensure your files are arranged as follows:

Plaintext

├── app.py              # Flask Server & NLP Logic
├── faq_data.json       # FAQ Dataset
├── templates/          
│   └── index.html      # UI View
└── static/             
    └── style.css       # Custom Styling
4. Run the Project
Bash

python app.py
Open your browser and navigate to http://127.0.0.1:5000.

🧪 API Testing (Postman)
You can test the bot without the frontend by sending a POST request to: http://127.0.0.1:5000/ask

Body (JSON):

JSON

{
    "question": "How do I register for the exam?"
}
📝 Example Dataset
The bot currently answers questions like:

"What courses are available?"

"How long does each course take?"

"Is there a refund policy?"

"I can't log into my account!"

🤝 Contributing
Feel free to fork this project, open issues, or submit pull requests to improve the NLP logic!
