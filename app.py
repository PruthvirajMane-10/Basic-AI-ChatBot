import json
from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

with open('faq_data.json', 'r') as f:
    data = json.load(f)
    faq_list = data['faq']

# 1. Extract questions from the FAQ data
faq_questions = [item['question'] for item in faq_list]

def find_best_match(user_query):
    # 2. Add user query to the list of questions for comparison
    temp_questions = faq_questions + [user_query]
    
    # 3. Vectorize the text (Convert text to numbers)
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(temp_questions)
    
    # 4. Compute Cosine Similarity between user query and FAQ questions
    # Similarity of the last item (user input) against all previous items
    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    # 5. Get the index of the most similar question
    best_match_idx = cosine_sim.argsort()[0][-1]
    confidence_score = cosine_sim[0][best_match_idx]
    
    # 6. Threshold check (if score < 0.2, the question is likely unrelated)
    if confidence_score < 0.2:
        return "I'm sorry, I couldn't find an answer to that. Please contact support@chatbot.com."
    
    return faq_list[best_match_idx]['answer']

@app.route('/')
def home():
    # This looks inside the /templates folder automatically
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_query = request.json.get('question')
    # Use your existing cosine similarity function here
    bot_response = find_best_match(user_query) 
    return jsonify({"answer": bot_response})

if __name__ == '__main__':
    app.run(debug=True)