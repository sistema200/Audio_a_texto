import speech_recognition as sr
import random
try:
    print("✏️Transcripcion de 💿audio.wav a texto📋")
    filename = input("Ruta y nombre del 💿achivo.wav: ")
    nombre_a = input("Nombre a 💾guardar: ")
    numero = random.randint(10, 99)
    output_file = f"/data/data/com.termux/files/home/casa/A00/{nombre_a}_{numero}.txt"

    r = sr.Recognizer()
except KeyboardInterrupt:
    print("\n\nEl programa fue cerrado por el usuario")
try:
   with sr.AudioFile(filename) as source:
       duration = int(source.DURATION)
       full_transcription = ""
       print("🛸Procesando audio...⏰⏰")
       for i in range(0, duration, 10):
           try:
               audio_data = r.record(source, duration=10)
               text = r.recognize_google(audio_data, language="es-ES")
               full_transcription += text + "\n"
               print(f"🟢Fragmento {i // 10 + 1}: {text}")
           except sr.UnknownValueError:
               print(f"🔴Fragmeto {i // 10 + 1}:😢No se pudo entender esta parte de el audio.")
               full_transcription += "[😥No se pudo enteder esta parte de el audio]\n"
           except sr.RequestError as e:
               print(f"Erro al comunicarce con el servidor: {e}")
               break
       with open(output_file, "w", encoding="utf-8") as f:
           f.write(full_transcription)
   print(f"trancripcion lista 🎇 🎇 🎇 🎇 en {output_file}")
   print("🎉 🎉 🎉 🎉 🎉 🎉 🎉 🎉 🎉 🎉 🎉 🎉")

except FileNotFoundError:
    print(f"Achivo no encontrado {filename} 😰")
except ValueError as e:
    print(f"Error con el achivo: {e} 🙁")
except Exception as e:
    print(f"Ocurrio un error inesperado: {e} 😭")
