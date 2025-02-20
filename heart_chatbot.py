import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from difflib import get_close_matches
import random
import pandas as pd
from heart_qa_database import heart_faq, get_all_questions, get_question_by_difficulty, get_questions_by_topic, get_random_question

# Download required NLTK data
nltk.download('punkt')

# Define heart parts and their functions
heart_parts = {
    "From Upper Body": "Deoxygenated blood from the upper body returns to the heart.",
    "Superior Vena Cava": "Carries deoxygenated blood from the upper body to the right atrium.",
    "To Right Lung": "Blood is transported from the right ventricle to the right lung for oxygenation.",
    "From Right Lung": "Oxygenated blood returns from the right lung to the heart.",
    "Pulmonary Veins": "Return oxygenated blood from the lungs to the left atrium.",
    "Right Atrium": "Receives deoxygenated blood from the body and sends it to the right ventricle.",
    "Atrioventricular Node": "Delays electrical impulses to allow the atria to contract before the ventricles.",
    "Tricuspid Valve": "Prevents backflow of blood between the right atrium and right ventricle.",
    "Right Ventricle": "Pumps deoxygenated blood to the lungs via the pulmonary artery.",
    "Inferior Vena Cava": "Transports deoxygenated blood from the lower body to the right atrium.",
    "From Lower Body": "Deoxygenated blood from the lower body returns to the heart.",
    "To Lower Body": "Oxygenated blood is sent to the lower body via the aorta.",
    "Chordae Tendineae": "Thin tendons that support the heart valves, preventing them from flipping inside out.",
    "To Upper Body": "Oxygenated blood is sent to the upper body via the aorta.",
    "Arteries": "Blood vessels that carry oxygen-rich blood away from the heart.",
    "Arch of Aorta": "Curved portion of the aorta that distributes blood to the head and arms.",
    "Pulmonary Artery": "Carries deoxygenated blood from the heart to the lungs.",
    "To Left Lung": "Blood is transported from the right ventricle to the left lung for oxygenation.",
    "From Left Lung": "Oxygenated blood returns from the left lung to the heart.",
    "Left Atrium": "Receives oxygenated blood from the lungs and passes it to the left ventricle.",
    "Mitral (Bicuspid) Valve": "Prevents backflow of blood between the left atrium and left ventricle.",
    "Left Ventricle": "Pumps oxygenated blood to the entire body via the aorta.",
    "Purkinje Fibers": "Conduct electrical impulses that coordinate heart contractions.",
    "Septum": "Divides the left and right sides of the heart to prevent oxygen-rich and oxygen-poor blood from mixing.",
    "Aortic Valve": "Prevents blood from flowing back into the left ventricle from the aorta.",
    "Pulmonary Valve": "Prevents blood from flowing back into the right ventricle from the pulmonary artery."
}



def create_learning_game():
    """Create an interactive learning game about heart facts"""
    st.subheader("🎮 Heart Hero Challenge")
    
    if 'score' not in st.session_state:
        st.session_state.score = 0
        st.session_state.completed_questions = set()
    
    game_modes = ["Multiple Choice", "True/False", "Flash Cards", "Memory Match"]
    game_mode = st.selectbox("Choose your game mode:", game_modes)
    
    if game_mode == "Multiple Choice":
        difficulty = st.select_slider("Select difficulty:", ["easy", "medium", "hard"])
        questions = get_question_by_difficulty(difficulty)
        
        if questions:
            category, question = random.choice(questions)
            correct_answer = heart_faq[category][question]["answer"]
            
            options = [correct_answer]
            while len(options) < 4:
                _, random_q = get_random_question()
                if category in heart_faq and random_q in heart_faq[category]:
                    wrong_answer = heart_faq[category][random_q]["answer"]
                else:
                    wrong_answer = "Unknown answer"

                if wrong_answer not in options:
                    options.append(wrong_answer)
            
            random.shuffle(options)
            st.write(f"Question: {question}")
            user_answer = st.radio("Choose your answer:", options)
            
            if st.button("Submit Answer"):
                if user_answer == correct_answer:
                    st.session_state.score += 1
                    st.session_state.completed_questions.add(question)
                    st.balloons()
                    st.success(f"Correct! 🎉 Score: {st.session_state.score}")
                else:
                    st.error(f"Try again! The correct answer was: {correct_answer}")
    
    elif game_mode == "Flash Cards":
        category = st.selectbox("Choose a category:", list(heart_faq.keys()))
        if st.button("Draw Card"):
            question, data = random.choice(list(heart_faq[category].items()))
            st.info(f"Question: {question}")
            with st.expander("Show Answer"):
                st.write(data["answer"])
                st.write(f"Fun fact: {data['fun_fact']}")
                
    elif game_mode == "Memory Match":
        if 'memory_cards' not in st.session_state:
            questions = get_all_questions()
            selected_pairs = random.sample(questions, 6)  # 6 pairs = 12 cards
            cards = [(q, 'question') for _, q in selected_pairs] + [(heart_faq[cat][q]["answer"], 'answer') for cat, q in selected_pairs]
            random.shuffle(cards)
            st.session_state.memory_cards = cards
            st.session_state.flipped = set()
            st.session_state.matched = set()
        
        cols = st.columns(4)
        for i, (content, card_type) in enumerate(st.session_state.memory_cards):
            col = cols[i % 4]
            if i in st.session_state.matched or i in st.session_state.flipped:
                col.info(content[:50] + "..." if len(content) > 50 else content)
            else:
                if col.button(f"Card {i+1}"):
                    st.session_state.flipped.add(i)

def get_answer(user_question):
    """Enhanced answer matching with related topics and difficulty rating"""
    all_questions = []
    for category in heart_faq:
        all_questions.extend(heart_faq[category].keys())
    
    matches = get_close_matches(user_question.lower(), [q.lower() for q in all_questions], n=1, cutoff=0.6)
    
    if matches:
        matched_question = all_questions[[q.lower() for q in all_questions].index(matches[0])]
        for category in heart_faq:
            if matched_question in heart_faq[category]:
                response = heart_faq[category][matched_question]
                return {
                    "answer": response["answer"],
                    "fun_fact": response["fun_fact"],
                    "difficulty": response["difficulty"],
                    "related_topics": response["related_topics"]
                }
    
    return {
        "answer": "I'm not sure about that. Try asking another heart-related question!",
        "fun_fact": "Did you know? The heart is about the size of your fist!",
        "difficulty": "easy",
        "related_topics": ["basics"]
    }

# Main Streamlit UI
st.set_page_config(page_title="Heart Education Bot", page_icon="❤️", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #fff1f1;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 20px;
        padding: 10px 25px;
        font-weight: bold;
    }
    .fun-fact {
        background-color: #ffe4e1;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .difficulty-badge {
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 0.8em;
        margin: 5px;
    }
    .easy { background-color: #90EE90; }
    .medium { background-color: #FFD700; }
    .hard { background-color: #FFB6C1; }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'learning_path' not in st.session_state:
    st.session_state.learning_path = []
if 'achievements' not in st.session_state:
    st.session_state.achievements = set()

# Main layout with tabs
tab1, tab2, tab3, tab4 = st.tabs(["Learn 📚", "Play 🎮", "Explore ❤️", "Progress 📊"])

with tab1:
    st.title("❤️ Interactive Heart Learning Bot")
    st.write("Learn about your heart in a fun and interactive way! Ask me anything!")

    # Search and auto-complete
    all_questions = [q for cat in heart_faq.values() for q in cat.keys()]
    user_input = st.text_input("Your question:", placeholder="Type your question here...")
    
    if user_input:
        response = get_answer(user_input)
        
        # Display difficulty badge
        st.markdown(f"""
            <span class='difficulty-badge {response["difficulty"]}'>
                Difficulty: {response["difficulty"].title()}
            </span>
        """, unsafe_allow_html=True)
        
        st.success(response["answer"])
        
        # Fun fact with animation
        with st.container():
            st.markdown(f"""
                <div class='fun-fact'>
                    💡 Fun Fact: {response["fun_fact"]}
                </div>
            """, unsafe_allow_html=True)
        
        # Related topics
        st.write("Related topics:", ", ".join(response["related_topics"]))
        
        # Add to learning path
        st.session_state.learning_path.append(user_input)

with tab2:
    create_learning_game()

with tab3:
    st.subheader("Interactive Heart Model")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        # Embed the Sketchfab model
        st.markdown("""
            <div style="text-align: center;">
                <iframe title="Human Heart Anatomy Labeled" 
                frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" 
                allow="autoplay; fullscreen; xr-spatial-tracking" 
                src="https://sketchfab.com/models/1b7bfb07e6b24dd891099395ed98e989/embed" 
                width="100%" height="500"></iframe>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        
        # Add heart parts explorer
        st.markdown("### Heart Parts Explorer")
        st.write("Click on a part to learn its function:")
        
        # Create a scrollable container for the buttons
        with st.container():
            # Use columns to create a more compact layout
            cols = st.columns(2)
            for idx, (part, function) in enumerate(heart_parts.items()):
                with cols[idx % 2]:
                    if st.button(part, key=f"heart_part_{idx}"):
                        st.info(f"**{part}**")
                        st.write(function)

with tab4:
    st.subheader("Your Learning Journey")
    
    # Progress overview
    total_questions = sum(len(category) for category in heart_faq.values())
    completed = len(st.session_state.completed_questions)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Questions Completed", f"{completed}/{total_questions}")
    col2.metric("Current Score", st.session_state.score)
    col3.metric("Achievements", len(st.session_state.achievements))
    
    # Learning path
    st.subheader("Recent Topics Explored")
    for question in st.session_state.learning_path[-5:]:
        st.write(f"• {question}")

# Sidebar with additional features
st.sidebar.title("💡 Learning Tools")

# Category explorer
st.sidebar.subheader("Topic Explorer")
selected_category = st.sidebar.selectbox("Choose a category:", list(heart_faq.keys()))
if selected_category:
    for question in heart_faq[selected_category]:
        if st.sidebar.checkbox(question, key=question):
            st.session_state.completed_questions.add(question)
            with st.sidebar.expander("Learn More"):
                st.write(heart_faq[selected_category][question]["answer"])
                st.write(f"Fun fact: {heart_faq[selected_category][question]['fun_fact']}")

# Achievements system
if len(st.session_state.completed_questions) >= 5:
    st.session_state.achievements.add("Beginner Heart Explorer")
if len(st.session_state.completed_questions) >= 10:
    st.session_state.achievements.add("Heart Knowledge Champion")
if st.session_state.score >= 10:
    st.session_state.achievements.add("Quiz Master")

# Footer
st.markdown("""
    ---
    Created with ❤️ for heart health education | Stay healthy, stay happy!
""")