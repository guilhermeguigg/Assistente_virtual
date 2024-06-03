import pyttsx3
import datetime
import speech_recognition as sr


def falar(audio):
    texto_fala = pyttsx3.init()  # Inicializa o engine de texto para fala
    texto_fala.setProperty('rate', 170)  # Define a nova velocidade
    voices = texto_fala.getProperty('voices')  # Obtém as vozes disponíveis
    texto_fala.setProperty('voice', voices[2].id)  # Define a voz a ser usada (mude o índice se necessário)
    texto_fala.say(audio)  # Adiciona o texto para ser falado
    texto_fala.runAndWait()  # Executa a fala


def tempo():
    Tempo = datetime.datetime.now().strftime("%I:%M %p")
    falar("A hora atual é " + Tempo)

def data():
    agora = datetime.datetime.now()
    ano = agora.year
    mes = agora.month
    dia = agora.day
    falar('A data atual é:')
    falar(f"{dia} de {mes} de {ano}")

def bem_vindo():
    falar("Olá senhor. Bem vindo de volta!")
    tempo()
    data()
    hora = datetime.datetime.now().hour
    if 6 <= hora < 12:
        falar("Bom dia senhor!")
    elif 12 <= hora < 18:
        falar("Boa tarde senhor!")
    elif 18 <= hora <= 24:
        falar("Boa noite senhor!")
    else:
        falar("Olá!")
        falar("a sua disposição. como posso ajudalo")

bem_vindo()

def microfone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("reconhecendo...")
        comando = r.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {comando}")
    except Exception as e:
        print(e)
        falar("Desculpe, não consegui entender. Pode repetir, por favor?")
        return "None"
    return comando
microfone()
if __name__=="__main__":
    bem_vindo()
    while True:
        print("escutando")
        comando = microfone().lower()
