# MultiLingo Chat Assistant

The MultiLingo Chat Assistant is a Python program that integrates OpenAI ChatGPT and Google Translate to provide a seamless and user-friendly experience for global communication. It aims to break down language barriers and foster cross-cultural understanding by enabling users to converse in multiple languages effortlessly.

## Features

- **Voice Input:** Utilizes the SpeechRecognition library to convert voice input into text, making it convenient for users to ask questions or engage in conversations.
- **Text-to-Speech:** Employs the pyttsx3 library to convert text responses into speech, enhancing accessibility and user experience.
- **Language Translation:** Integrates the Googletrans library to detect and translate text between different languages, enabling multilingual conversations.
- **AI-Powered Responses:** Leverages the OpenAI GPT-3 model (text-davinci-003) to generate intelligent and contextually relevant responses to user queries.

## Setup

1. Clone the repository to your local machine.
2. Install the required libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```
3. Replace the OpenAI API key (`openai.api_key`) with your own API key obtained from the OpenAI platform.
4. Run the `main.py` script to start the MultiLingo Chat Assistant.

## Usage

1. Launch the program and grant microphone access for voice input.
2. Speak your query or message in any supported language.
3. The program will convert your speech to text, translate it to English for processing, and generate a response using ChatGPT.
4. The response will be translated back to your detected language and spoken aloud using text-to-speech technology.

## Dependencies

- openai (OpenAI API for ChatGPT integration)
- googletrans (Google Translate API for language detection and translation)
- pyttsx3 (Text-to-speech library for audio output)
- SpeechRecognition (Library for voice input processing)

## Disclaimer

This project is for demonstration purposes and may require appropriate API keys or credentials for full functionality. Use responsibly and in compliance with API usage policies and guidelines.

## Contributors

YASH 
TULSI SHARMA
VISHNU SINGH

Feel free to contribute, report issues, or suggest improvements by submitting pull requests or opening issues in the GitHub repository. Your feedback is valuable in enhancing the MultiLingo Chat Assistant.
