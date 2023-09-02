import win32com.client

# Create an instance of the SAPI voice object
speaker = win32com.client.Dispatch('SAPI.SpVoice')

# Get the voices available on the system
voices = speaker.GetVoices()

# Choose a specific female voice (you may need to adjust the index)
female_voice = voices.Item(1)  # You might need to adjust the index to choose the desired female voice

# Set the voice for the speaker
speaker.Voice = female_voice

# Speak a message with the selected voice
speaker.Speak("Hello, I'm speaking with a female voice!")
