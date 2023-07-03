import speech_recognition as sr
import pyttsx3
import openai

# Initialize the speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set the wake word
wake_word = "Eliot"

# Configure OpenAI API
openai.api_key = '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'

# Function to convert text to speech
def speak(text):
    print("Bot: " + text)
    engine.say(text)
    engine.runAndWait()

# Function to perform chat-based language completion using OpenAI API
def chat_completion(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    answer = response.choices[0].message.content
    return answer

# Main loop for speech recognition
while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        # Use the speech recognition engine to convert speech to text
        user_input = recognizer.recognize_google(audio)
        print("You said:", user_input)

        # Check if the wake word is present in the user's input
        if wake_word in user_input:
            # Remove the wake word from the user's input
            user_input = user_input.replace(wake_word, "")

            # Process the user's input and perform chat completion using OpenAI
            response = chat_completion(user_input)
            speak(response)

    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        print("An error occurred. Please check your internet connection.")