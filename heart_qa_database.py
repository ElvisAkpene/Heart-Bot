import random

heart_faq = {
    "basics": {
        "What does the heart do?": {
            "answer": "The heart is a powerful muscle that pumps blood throughout your body. It works like a super-efficient pump that never stops!",
            "fun_fact": "Your heart beats about 100,000 times every day!",
            "difficulty": "easy",
            "related_topics": ["circulation", "heart anatomy"],
            "category_image": "heart_basic"
        },
        "How many chambers does the heart have?": {
            "answer": "The heart has four chambers: two upper chambers (atria) and two lower chambers (ventricles). The right side pumps blood to the lungs, while the left side pumps blood to the rest of the body.",
            "fun_fact": "The left ventricle is the strongest chamber because it has to pump blood to the whole body!",
            "difficulty": "medium",
            "related_topics": ["heart anatomy", "blood flow"],
            "category_image": "chambers"
        },
        "What is the size of a human heart?": {
            "answer": "An adult heart is about the size of a closed fist and weighs about 8-10 ounces (226-283 grams).",
            "fun_fact": "A blue whale's heart can be as big as a small car!",
            "difficulty": "easy",
            "related_topics": ["heart anatomy"],
            "category_image": "heart_size"
        },
        "What is the cardiac muscle made of?": {
            "answer": "The heart is made of a special type of muscle called cardiac muscle or myocardium. These cells are unique because they can contract rhythmically on their own!",
            "fun_fact": "Cardiac muscle cells can communicate with each other electrically!",
            "difficulty": "medium",
            "related_topics": ["heart anatomy", "cellular biology"],
            "category_image": "cardiac_muscle"
        },
        "What is the average heart rate?": {
            "answer": "The average resting heart rate for adults is 60-100 beats per minute. Athletes often have lower resting heart rates due to better cardiovascular fitness.",
            "fun_fact": "A newborn baby's heart beats much faster, at about 70-190 beats per minute!",
            "difficulty": "easy",
            "related_topics": ["heart rate", "fitness"],
            "category_image": "heart_rate"
        },
        "What is the pericardium?": {
            "answer": "The pericardium is a protective sac that surrounds the heart. It has two layers and contains fluid to reduce friction as the heart beats.",
            "fun_fact": "The pericardium is so tough that it can protect the heart from infections!",
            "difficulty": "medium",
            "related_topics": ["heart anatomy"],
            "category_image": "pericardium"
        },
        "What is the septum?": {
            "answer": "The septum is a wall of tissue that separates the left and right sides of the heart. It ensures oxygen-rich and oxygen-poor blood don't mix.",
            "fun_fact": "A hole in the septum is called a septal defect and is a common congenital heart condition.",
            "difficulty": "medium",
            "related_topics": ["heart anatomy", "congenital conditions"],
            "category_image": "septum"
        },
        "What is the role of the coronary arteries?": {
            "answer": "The coronary arteries supply oxygen-rich blood to the heart muscle itself. Without them, the heart wouldn't get the energy it needs to pump.",
            "fun_fact": "Blockage in the coronary arteries is the main cause of heart attacks!",
            "difficulty": "medium",
            "related_topics": ["circulation", "heart anatomy"],
            "category_image": "coronary_arteries"
        },
        "What is the sinoatrial (SA) node?": {
            "answer": "The SA node is the heart's natural pacemaker. It generates electrical impulses that start each heartbeat.",
            "fun_fact": "The SA node can fire impulses 60-100 times per minute at rest!",
            "difficulty": "hard",
            "related_topics": ["electrical system", "heart rhythm"],
            "category_image": "sa_node"
        },
        "What is the atrioventricular (AV) node?": {
            "answer": "The AV node is a cluster of cells that delays the electrical signal from the atria to the ventricles, ensuring the heart chambers contract in the right order.",
            "fun_fact": "The AV node is like a 'gatekeeper' for electrical signals in the heart!",
            "difficulty": "hard",
            "related_topics": ["electrical system", "heart rhythm"],
            "category_image": "av_node"
        }
    },
    "circulation": {
        "How does blood circulation work?": {
            "answer": "Blood circulation is like a highway system. Arteries carry oxygen-rich blood from your heart to your body, while veins return oxygen-poor blood back to your heart.",
            "fun_fact": "If laid end to end, your blood vessels would circle the Earth 2.5 times!",
            "difficulty": "medium",
            "related_topics": ["blood flow", "cardiovascular system"],
            "category_image": "circulation"
        },
        "What is the difference between arteries and veins?": {
            "answer": "Arteries carry blood away from the heart and have thick, elastic walls. Veins carry blood back to the heart and have thinner walls with valves to prevent backward flow.",
            "fun_fact": "You can see veins through your skin but not arteries because veins are closer to the surface!",
            "difficulty": "medium",
            "related_topics": ["blood vessels", "circulation"],
            "category_image": "vessels"
        },
        "What is pulmonary circulation?": {
            "answer": "Pulmonary circulation is the part of the circulatory system that carries blood between the heart and lungs. It oxygenates the blood and removes carbon dioxide.",
            "fun_fact": "Pulmonary circulation is the only place where arteries carry oxygen-poor blood and veins carry oxygen-rich blood!",
            "difficulty": "medium",
            "related_topics": ["circulation", "lungs"],
            "category_image": "pulmonary_circulation"
        },
        "What is systemic circulation?": {
            "answer": "Systemic circulation carries oxygen-rich blood from the heart to the rest of the body and returns oxygen-poor blood back to the heart.",
            "fun_fact": "Systemic circulation is the longest part of the circulatory system!",
            "difficulty": "medium",
            "related_topics": ["circulation", "blood flow"],
            "category_image": "systemic_circulation"
        },
        "What are capillaries?": {
            "answer": "Capillaries are tiny blood vessels that connect arteries and veins. They deliver oxygen and nutrients to tissues and remove waste products.",
            "fun_fact": "Capillaries are so small that red blood cells must pass through them in single file!",
            "difficulty": "medium",
            "related_topics": ["blood vessels", "circulation"],
            "category_image": "capillaries"
        },
        "What is blood pressure?": {
            "answer": "Blood pressure is the force of blood pushing against the walls of your arteries. It's measured as systolic (when the heart beats) over diastolic (when the heart rests).",
            "fun_fact": "Normal blood pressure is around 120/80 mmHg!",
            "difficulty": "medium",
            "related_topics": ["circulation", "health"],
            "category_image": "blood_pressure"
        },
        "What is the role of the aorta?": {
            "answer": "The aorta is the largest artery in the body. It carries oxygen-rich blood from the left ventricle to the rest of the body.",
            "fun_fact": "The aorta is about as wide as a garden hose!",
            "difficulty": "medium",
            "related_topics": ["circulation", "heart anatomy"],
            "category_image": "aorta"
        },
        "What is the vena cava?": {
            "answer": "The vena cava is the largest vein in the body. It carries oxygen-poor blood from the body back to the heart.",
            "fun_fact": "There are two vena cavae: the superior (upper body) and inferior (lower body)!",
            "difficulty": "medium",
            "related_topics": ["circulation", "heart anatomy"],
            "category_image": "vena_cava"
        },
        "What is the role of the pulmonary artery?": {
            "answer": "The pulmonary artery carries oxygen-poor blood from the right ventricle to the lungs for oxygenation.",
            "fun_fact": "The pulmonary artery is the only artery that carries oxygen-poor blood!",
            "difficulty": "medium",
            "related_topics": ["circulation", "lungs"],
            "category_image": "pulmonary_artery"
        },
        "What is the role of the pulmonary vein?": {
            "answer": "The pulmonary vein carries oxygen-rich blood from the lungs back to the left atrium of the heart.",
            "fun_fact": "The pulmonary vein is the only vein that carries oxygen-rich blood!",
            "difficulty": "medium",
            "related_topics": ["circulation", "lungs"],
            "category_image": "pulmonary_vein"
        }
    },
    "health": {
        "Why is exercise good for the heart?": {
            "answer": "Exercise strengthens your heart muscle, improves blood flow, and helps maintain healthy blood pressure and cholesterol levels. Regular exercise can also help prevent heart disease.",
            "fun_fact": "Just 30 minutes of moderate exercise each day can significantly improve heart health!",
            "difficulty": "medium",
            "related_topics": ["prevention", "lifestyle"],
            "category_image": "exercise"
        },
        "What foods are good for heart health?": {
            "answer": "Heart-healthy foods include fruits, vegetables, whole grains, lean proteins, and foods rich in omega-3 fatty acids like fish. These foods help maintain healthy cholesterol levels and blood pressure.",
            "fun_fact": "Dark chocolate contains flavonoids that can help protect your heart!",
            "difficulty": "medium",
            "related_topics": ["nutrition", "prevention"],
            "category_image": "healthy_food"
        },
        "How does stress affect the heart?": {
            "answer": "Stress can increase heart rate and blood pressure, and long-term stress may contribute to heart disease. Managing stress through relaxation techniques can help protect your heart.",
            "fun_fact": "Laughter is great medicine - it can help reduce stress and improve heart health!",
            "difficulty": "medium",
            "related_topics": ["mental health", "prevention"],
            "category_image": "stress"
        },
        "What is cholesterol?": {
            "answer": "Cholesterol is a waxy substance found in your blood. While your body needs it to build cells, too much can lead to plaque buildup in arteries, increasing heart disease risk.",
            "fun_fact": "Your liver produces about 80% of the cholesterol in your body!",
            "difficulty": "medium",
            "related_topics": ["nutrition", "prevention"],
            "category_image": "cholesterol"
        },
        "What is a healthy blood pressure range?": {
            "answer": "A healthy blood pressure range is less than 120/80 mmHg. High blood pressure (hypertension) is 130/80 mmHg or higher.",
            "fun_fact": "Blood pressure can vary throughout the day and is lowest during sleep!",
            "difficulty": "easy",
            "related_topics": ["health", "prevention"],
            "category_image": "blood_pressure"
        },
        "What is a heart-healthy diet?": {
            "answer": "A heart-healthy diet includes plenty of fruits, vegetables, whole grains, lean proteins, and healthy fats. It limits salt, sugar, and saturated fats.",
            "fun_fact": "The Mediterranean diet is often recommended for heart health!",
            "difficulty": "easy",
            "related_topics": ["nutrition", "prevention"],
            "category_image": "diet"
        },
        "How does smoking affect the heart?": {
            "answer": "Smoking damages blood vessels, increases blood pressure, and reduces oxygen in the blood, all of which increase the risk of heart disease.",
            "fun_fact": "Quitting smoking can cut your risk of heart disease in half within a year!",
            "difficulty": "medium",
            "related_topics": ["prevention", "lifestyle"],
            "category_image": "smoking"
        },
        "What is the DASH diet?": {
            "answer": "The DASH diet (Dietary Approaches to Stop Hypertension) is a heart-healthy eating plan that focuses on reducing sodium and increasing nutrients that lower blood pressure.",
            "fun_fact": "The DASH diet is ranked as one of the best diets for heart health!",
            "difficulty": "medium",
            "related_topics": ["nutrition", "prevention"],
            "category_image": "dash_diet"
        },
        "What is the role of fiber in heart health?": {
            "answer": "Fiber helps lower cholesterol levels and improve heart health by binding to cholesterol in the digestive system and removing it from the body.",
            "fun_fact": "Oats are a great source of soluble fiber, which is especially good for heart health!",
            "difficulty": "medium",
            "related_topics": ["nutrition", "prevention"],
            "category_image": "fiber"
        },
        "What is the role of omega-3 fatty acids in heart health?": {
            "answer": "Omega-3 fatty acids help reduce inflammation, lower triglycerides, and may reduce the risk of heart disease. They are found in fatty fish, flaxseeds, and walnuts.",
            "fun_fact": "Eating fish twice a week can significantly boost your omega-3 intake!",
            "difficulty": "medium",
            "related_topics": ["nutrition", "prevention"],
            "category_image": "omega_3"
        }
    },
    "conditions": {
        "What is a heart attack?": {
            "answer": "A heart attack occurs when blood flow to part of the heart muscle is blocked, usually by a blood clot. This can damage or destroy part of the heart muscle.",
            "fun_fact": "Heart attack symptoms can be different in women than in men!",
            "difficulty": "hard",
            "related_topics": ["emergency", "prevention"],
            "category_image": "heart_attack"
        },
        "What is heart failure?": {
            "answer": "Heart failure doesn't mean the heart stops - it means the heart isn't pumping blood as well as it should. This can cause fatigue and breathing problems.",
            "fun_fact": "People can live many years with proper heart failure treatment!",
            "difficulty": "hard",
            "related_topics": ["conditions", "treatment"],
            "category_image": "heart_failure"
        },
        "What is arrhythmia?": {
            "answer": "Arrhythmia is an irregular heartbeat. It can be too fast (tachycardia), too slow (bradycardia), or irregular.",
            "fun_fact": "Some arrhythmias are harmless, while others can be life-threatening!",
            "difficulty": "hard",
            "related_topics": ["heart rhythm", "conditions"],
            "category_image": "arrhythmia"
        },
        "What is atrial fibrillation?": {
            "answer": "Atrial fibrillation (AFib) is a type of arrhythmia where the upper chambers of the heart beat irregularly and out of sync with the lower chambers.",
            "fun_fact": "AFib increases the risk of stroke by five times!",
            "difficulty": "hard",
            "related_topics": ["heart rhythm", "conditions"],
            "category_image": "afib"
        },
        "What is coronary artery disease?": {
            "answer": "Coronary artery disease (CAD) occurs when the coronary arteries become narrowed or blocked by plaque, reducing blood flow to the heart muscle.",
            "fun_fact": "CAD is the most common type of heart disease!",
            "difficulty": "hard",
            "related_topics": ["conditions", "prevention"],
            "category_image": "cad"
        },
        "What is angina?": {
            "answer": "Angina is chest pain or discomfort caused by reduced blood flow to the heart muscle. It's often a symptom of coronary artery disease.",
            "fun_fact": "Angina can feel like pressure, squeezing, or burning in the chest!",
            "difficulty": "hard",
            "related_topics": ["conditions", "symptoms"],
            "category_image": "angina"
        },
        "What is a congenital heart defect?": {
            "answer": "A congenital heart defect is a problem with the heart's structure that's present at birth. It can affect the heart's walls, valves, or blood vessels.",
            "fun_fact": "Congenital heart defects are the most common type of birth defect!",
            "difficulty": "hard",
            "related_topics": ["conditions", "pediatrics"],
            "category_image": "congenital"
        },
        "What is cardiomyopathy?": {
            "answer": "Cardiomyopathy is a disease of the heart muscle that makes it harder for the heart to pump blood. It can lead to heart failure.",
            "fun_fact": "Cardiomyopathy can be inherited or caused by other conditions like high blood pressure!",
            "difficulty": "hard",
            "related_topics": ["conditions", "heart failure"],
            "category_image": "cardiomyopathy"
        },
        "What is endocarditis?": {
            "answer": "Endocarditis is an infection of the inner lining of the heart chambers and valves. It's often caused by bacteria entering the bloodstream.",
            "fun_fact": "Endocarditis can damage heart valves and lead to heart failure!",
            "difficulty": "hard",
            "related_topics": ["conditions", "infections"],
            "category_image": "endocarditis"
        }
    }
}

def get_all_questions():
    """Return a list of all questions in the database"""
    return [(category, question) for category in heart_faq for question in heart_faq[category]]

def get_question_by_difficulty(difficulty):
    """Return all questions of a specific difficulty level"""
    questions = []
    for category in heart_faq:
        for question, data in heart_faq[category].items():
            if data["difficulty"] == difficulty:
                questions.append((category, question))
    return questions

def get_questions_by_topic(topic):
    """Return all questions related to a specific topic"""
    questions = []
    for category in heart_faq:
        for question, data in heart_faq[category].items():
            if topic in data["related_topics"]:
                questions.append((category, question))
    return questions

def get_random_question(category=None, difficulty=None):
    """Return a random question, optionally filtered by category and/or difficulty"""
    eligible_questions = []
    for cat in heart_faq:
        if category and cat != category:
            continue
        for question, data in heart_faq[cat].items():
            if difficulty and data["difficulty"] != difficulty:
                continue
            eligible_questions.append((cat, question))
    return random.choice(eligible_questions) if eligible_questions else None