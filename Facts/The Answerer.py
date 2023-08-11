# Facts, A project made by sakthisubha
# Used to learn facts
# Note : It ONLY works IF you install wikipedian in terminal

# Create the source
import wikipedia

# Create the Question
question = str(input('Ask your question : '))

# Create the answering engine
print('If you do not get your answer, search the full name...')
info = wikipedia.summary(question)
print(info)

# Create the source
import wikipedia

# Create the Question
question = str(input('Ask your question : '))

# Create the answering engine
print('If you do not get your answer, search the full name...')
info = wikipedia.summary(question)
print(info)