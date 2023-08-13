import win32com.client as wincom
speak = wincom.Dispatch("SAPI.Spvoice")
text = "hello aniket how are you"
speak.Speak(text)
# time.sleep(3)
# text = "This text is read after 3 seconds"
# speak.Speak(text)