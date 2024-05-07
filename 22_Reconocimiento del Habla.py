#Pablo Dario Jimenez Nu*o 21310143

import speech_recognition as sr

def recognize_speech():
    # Crear un objeto recognizer
    recognizer = sr.Recognizer()

    # Utilizar el micrófono como fuente de entrada de audio
    with sr.Microphone() as source:
        print("Di algo...")
        recognizer.adjust_for_ambient_noise(source)  # Ajustar al ruido ambiental
        audio = recognizer.listen(source)  # Escuchar el audio desde el micrófono

    try:
        # Utilizar el reconocimiento de voz de Google
        text = recognizer.recognize_google(audio, language="es-ES")
        print("Has dicho:", text)
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        print("Error al solicitar resultados; {0}".format(e))

# Llamar a la función para reconocer el habla
recognize_speech()



