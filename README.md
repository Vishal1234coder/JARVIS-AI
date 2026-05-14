# JARVIS AI - Voice-Controlled Virtual Assistant

A voice-controlled virtual assistant that uses speech recognition, a web-based chatbot backend, and text-to-speech to create an interactive AI experience.

## How It Works

1. **Voice Input**: Captures microphone input via SpeechRecognition
2. **Chat Backend**: Sends queries to a Botpress webchat chatbot (AVA) using Selenium
3. **Response**: Scrapes the chatbot reply and speaks it aloud via edge-tts

## Files

| File | Purpose |
|------|---------|
| \`main.py\` | Entry point - voice loop: listen → send → speak response |
| \`bot_scrapper.py\` | Selenium automation for Botpress webchat interaction |
| \`test.py\` | Standalone TTS test with edge-tts + pygame |
| \`test2.py\` | Standalone TTS test with pyttsx3 (offline) |
| \`ope.py\` | Utility to open system applications |

## Requirements

\`\`\`bash
pip install pygame SpeechRecognition selenium edge-tts pyttsx3
\`\`\`

Requires Chrome/Chromium and matching chromedriver.

## Usage

\`\`\`bash
python main.py
\`\`\`

Speak into your microphone and JARVIS will respond through the AVA chatbot.

## License

MIT