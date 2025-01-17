# basic-chatbot-python
J.A.R.V.I.S - Voice Assistant
J.A.R.V.I.S is a simple voice assistant built using Python with text-to-speech and speech recognition functionalities. It utilizes the Tkinter GUI for displaying the conversation and offers interaction via voice commands. The assistant uses the OllamaLLM model for processing natural language input and provides intelligent responses.

Features
Voice Interaction: Speaks and listens to the user.
Text-to-Speech: Provides spoken responses using pyttsx3.
Speech Recognition: Recognizes speech input using the speech_recognition library.
GUI: Interactive interface with Tkinter displaying the conversation.
Llama3 Model: Uses the OllamaLLM to process natural language input and return meaningful responses.
Requirements
Before running this program, ensure you have the following dependencies installed:

Python 3.x
pyttsx3: Text-to-speech engine
speech_recognition: Speech recognition library
tkinter: GUI library for Python
langchain_ollama: For using the OllamaLLM model
PyAudio: Required by the speech_recognition library for microphone input
You can install the necessary libraries using pip:

bash
Copy
pip install pyttsx3 SpeechRecognition tkinter langchain_ollama pyaudio
Installation and Setup
Clone this repository to your local machine:

bash
Copy
git clone https://github.com/GaussianIntuition/jarvis-voice-assistant.git
cd jarvis-voice-assistant
Install the necessary dependencies as mentioned above.

Make sure that your microphone is connected and configured properly.

Usage
To start the voice assistant, simply run the Python script:

bash
Copy
python jarvis.py
Once the application starts, click on the Start Listening button, and the assistant will listen to your voice commands. You can speak commands such as:

"What is the weather like today?"
"Tell me a joke"
"Who won the game last night?"
The assistant will process your input and provide a response, speaking it aloud as well as displaying it in the GUI.

To exit the assistant, simply click on the Exit button, and the assistant will say "Goodbye" before closing the application.

Example Conversation
You: "Tell me a joke"
J.A.R.V.I.S: "Why don't scientists trust atoms? Because they make up everything!"
How it Works
Speech Recognition: The assistant listens for voice input via the microphone, which is processed by the speech_recognition library.
Natural Language Processing: The OllamaLLM model processes the recognized speech and generates appropriate responses.
Text-to-Speech: The assistant speaks the response back to you using the pyttsx3 engine.
GUI: The conversation is displayed in a Tkinter-based text box, with scroll functionality.
Contributing
Feel free to fork this repository and create pull requests to add new features or fix bugs. You can contribute by:

Improving speech recognition accuracy
Adding more functionalities or integrations
Enhancing the user interface
License
This project is open source and available under the MIT License.

Acknowledgments
Pyttsx3 - Text-to-speech engine
SpeechRecognition - Speech recognition library
Tkinter - GUI library
OllamaLLM - Natural Language Model used for processing responses
Enjoy interacting with J.A.R.V.I.S!



