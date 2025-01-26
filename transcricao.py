from google.cloud import speech

# Configuração do cliente
client = speech.SpeechClient()

# Configuração do áudio
audio = speech.RecognitionAudio(uri="C:/Users/likas/OneDrive/Documentos/lidia-news-app/audio1.mp3")
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.MP3,
    sample_rate_hertz=16000,
    language_code="pt-BR"
)

# Transcrição
response = client.recognize(config=config, audio=audio)
for result in response.results:
    print(f"Texto transcrito: {result.alternatives[0].transcript}")
