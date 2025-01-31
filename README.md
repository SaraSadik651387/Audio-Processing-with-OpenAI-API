# Audio Processing with OpenAI API 🎤🤖

## Overview 📌
This project converts an audio file into text, sends the text to OpenAI's API to generate a response, and converts the response back into speech.

## Features 🌟
- Converts speech from an audio file to text using `speech_recognition`.
- Sends the text to OpenAI's `GPT-3.5-turbo` for processing.
- Converts OpenAI's response into audio and plays it.

## Installation & Setup ⚙️
### Prerequisites 📋
Ensure you have Python installed (recommended version: 3.8 or higher).

### Install Dependencies 📥
Run the following command to install the required libraries:
```bash
pip install openai pydub speechrecognition
```

## Usage 🚀
1. Place your audio file (e.g., `good_morning.wav`) in the project folder.
2. Set up your OpenAI API key inside `process_audio.py`:
   ```python
   openai.api_key = "your_openai_api_key_here"
   ```
3. Run the script:
   ```bash
   python process_audio.py
   ```

## Code Explanation 📝
- **`audio_to_text(file_path)`**: Converts audio to text using Google's speech recognition.
- **`get_openai_response(prompt)`**: Sends text to OpenAI and retrieves the AI-generated response.
- **`text_to_audio(text)`**: Converts OpenAI’s response into speech using `pydub`.
- **`main()`**: Coordinates the entire process.

## Errors & Troubleshooting 🔍
### Issue Faced ⚠️
I encountered an error due to exceeding the OpenAI API quota:
<img width="718" alt="Image" src="https://github.com/user-attachments/assets/3029c91e-f696-4c0e-9efa-66d32eb3d1b5" />

### Possible Solutions ✅
- Check OpenAI's quota and billing settings.
- Generate a new API key and replace it in `process_audio.py`.
- If the issue persists, try using an alternative API.

## Future Enhancements 🔮
- Implementing support for real-time speech recognition.
- Adding support for multiple languages.
- Enhancing text-to-speech output with more natural voices.
