import openai
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr

# Set your OpenAI API key
openai.api_key = "sk-proj-........"

# Function to convert audio to text
def audio_to_text(file_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            print("Processing audio...")
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            print(f"Converted Text: {text}")
            return text
    except Exception as e:
        print(f"Error converting audio to text: {e}")
        return None

# Function to get a response from OpenAI
def get_openai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Ensure this is the correct model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return None

# Function to convert text to audio
def text_to_audio(text):
    try:
        # Save the audio response
        audio = AudioSegment.from_file("response_audio.mp3", format="mp3")
        audio.export("response_audio.mp3", format="mp3")
        print("Playing response audio...")
        play(audio)
    except Exception as e:
        print(f"Error generating audio: {e}")

# Main function
def main():
    # Step 1: Audio input file
    audio_file = "good_morning.wav"  # Replace with your file path

    # Step 2: Convert audio to text
    text = audio_to_text(audio_file)

    if text:
        # Step 3: Send text to OpenAI and get response
        ai_response = get_openai_response(text)

        if ai_response:
            print(f"AI Response: {ai_response}")

            # Step 4: Convert AI response to audio
            text_to_audio(ai_response)
        else:
            print("Failed to get response from OpenAI.")
    else:
        print("Failed to process the audio file.")

# Run the program
if __name__ == "__main__":
    main()
