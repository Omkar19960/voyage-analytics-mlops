🏨 Voyage Analytics – Hotel Recommendation System

A Streamlit-based hotel/place recommendation system that recommends places based on similar travelers' preferences.

🚀 Features
Enter a user code
Finds users with similar preferences
Generates personalized place recommendations
Falls back to popular places for unknown users
Displays recommended place details in a table
🛠️ Tech Stack
Python
Streamlit
Pandas
Pickle
Collaborative Filtering
📂 Project Structure
voyage-analytics-mlops/
│
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── models/
│   └── hotel_recommender.pkl
│
└── README.md

⚙️ Installation

Clone the repository:

git clone https://github.com/Omkar19960/voyage-analytics-mlops.git
cd voyage-analytics-mlops

Install dependencies:

pip install -r requirements.txt
▶️ Run the Application
streamlit run app/app.py

The application will open in your browser.

📦 Requirements
streamlit==1.59.2
pandas==2.3.3
🧠 Recommendation Logic

The system uses user-user collaborative filtering:

User enters a user code.
The system checks whether the user exists.
Similar users are identified using the user similarity matrix.
Places preferred by similar users are scored.
Top recommended places are displayed.
For an unknown user, popular places are recommended.
📊 Model Artifacts

The trained recommender model is stored in:

models/hotel_recommender.pkl

The pickle file contains:

user_place_matrix
user_similarity_df
place_profile
top_popular_places
☁️ Streamlit Deployment

The application can be deployed using Streamlit Community Cloud.

Set the main file path as:

app/app.py

Make sure models/hotel_recommender.pkl is present in the repository.

👨‍💻 Author

Omkar

GitHub: Omkar19960

📄 License

This project is intended for educational and demonstration purposes.
