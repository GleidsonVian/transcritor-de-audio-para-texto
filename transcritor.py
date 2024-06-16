import pyaudio
import wave
import speech_recognition as sr

# Configurações para gravação de áudio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "output.wav"

# Inicializar PyAudio
p = pyaudio.PyAudio()

# Abrir stream para gravação
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Gravando...")

frames = []

# Gravar áudio em pedaços
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Gravação finalizada.")

# Fechar stream
stream.stop_stream()
stream.close()
p.terminate()

# Salvar áudio em um arquivo WAV
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

# Inicializar o reconhecedor de fala
recognizer = sr.Recognizer()

# Carregar o áudio do arquivo WAV
with sr.AudioFile(WAVE_OUTPUT_FILENAME) as source:
    audio = recognizer.record(source)

# Tentar transcrever o áudio para pt-BR
try:
    text = recognizer.recognize_google(audio, language="pt-BR")
    print("Você disse: " + text)
except sr.UnknownValueError:
    print("Não foi possível entender o áudio.")
except sr.RequestError as e:
    print("Erro ao solicitar resultados do serviço de reconhecimento de fala; {0}".format(e))
