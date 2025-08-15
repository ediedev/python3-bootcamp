import requests

parameters = {
    "amount":10,
    "category":18,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
#
# question_data = [
#
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "Science &amp; Nature",
#         "question": "A person can get sunburned on a cloudy day.",
#         "correct_answer": "True",
#         "incorrect_answers": ["False"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
#      "question": "Hippopotomonstrosesquippedaliophobia is the irrational fear of long words.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
#      "question": "Scientists accidentally killed the once known world&#039;s oldest living creature, a mollusc, known to be aged as 507 years old.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
#      "question": "Like with the Neanderthals, Homo sapiens sapiens also interbred with the Denisovans.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
#      "question": "The planet Mars has two moons orbiting it.", "correct_answer": "True",
#      "incorrect_answers": ["False"]}, {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
#                                        "question": "&quot;Tachycardia&quot; or &quot;Tachyarrhythmia&quot; refers to a resting heart-rate near or over 100 BPM.",
#                                        "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
#      "question": "The Neanderthals were a direct ancestor of modern humans.", "correct_answer": "False",
#      "incorrect_answers": ["True"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature", "question": "Sugar contains fat.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
#      "question": "Shrimp can swim backwards.", "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
#      "question": "Steel is an alloy of Iron and Carbon.", "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
#      "question": "El Ni&ntilde;o pushes warm water to the coasts of the Western Pacific during winter.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
#      "question": "Male pandas do handstands while urinating on trees. ", "correct_answer": "True",
#      "incorrect_answers": ["False"]}, {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
#                                        "question": "The Doppler effect applies to light.", "correct_answer": "True",
#                                        "incorrect_answers": ["False"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
#      "question": "A defibrillator is used to start up a heartbeat once a heart has stopped beating.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
#      "question": "Polaris is the brightest star in the northern hemisphere night sky.", "correct_answer": "False",
#      "incorrect_answers": ["True"]}, {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
#                                       "question": "Anatomy considers the forms of macroscopic structures such as organs and organ systems.",
#                                       "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
#      "question": "Centripetal force is an apparent force that acts outward on a body moving around a center, arising from the body&#039;s inertia.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
#      "question": "Enthalpy is a measure of the energy that is not available for work during a thermodynamic process.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
#      "question": "Sound can travel through a vacuum.", "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
#      "question": "In the periodic table, Potassium&#039;s symbol is the letter K.", "correct_answer": "True",
#      "incorrect_answers": ["False"]}
# ]
