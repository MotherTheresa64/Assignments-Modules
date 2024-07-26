# mood_responses.py
def mood_response(mood):
    mood = mood.lower()  # Convert input to lowercase to handle case insensitivity
    responses = {
        'happy': "That's great to hear! Keep smiling!",
        'sad': "I'm sorry to hear that. I hope things get better soon.",
        'excited': "Awesome! Enjoy the excitement and have a great time!",
        'angry': "It's okay to feel angry sometimes. Take a deep breath and relax.",
        'bored': "Sometimes boredom can be an opportunity to try something new or creative."
    }
    return responses.get(mood, "I don't have a response for that mood. But I hope you have a good day!")
