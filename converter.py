from gtts import gTTS
import os


text = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
output = gTTS(text=text, lang='en', slow=False)
output.save("output.mp3")


# text = "Trois tortues trottaient sur trois trottoirs tres etroits."
# output = gTTS(text=text, lang='fr', slow=False)
# output.save("output.mp3")


os.system("afplay output.mp3")