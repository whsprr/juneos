import random
import os.path
from datetime import datetime

while True:
	now = datetime.now()
	
	current_time = now.strftime("%H:%M:%S")
	
	greet = ["Hi", "Hello", "Hey", "How do you do?", "Yo!", "Hey!", "Sup!", "Hello"]
	
	joke = ["I invented a new word! Plagiarism!","What is the biggest lie in the entire universe? I have read and agree to the Terms & Conditions.", "My computer suddenly started belting out Someone Like You. It's a Dell.", "Why did Zuckerberg create Facebook? He couldn't pass the captcha for Myspace."]
	
	anger = ["Excuse me I have been nice to you so far, you little whiney idiot!", "Excuse me!", "That is very rude!"]
	
	laugh =["Glad you find it amusing", "Lol"]

	emotion = ["I feel fine, how are you", "Well it is hard work being an assistant, How do you feel", "I feel excellent, Thank you for asking. How are you"]
	
	opinion = ["Yes", "No", "Maybe","I don't know", "Absolutely", "Not at all"]
	
	
	june = input("Type to start chating: ")
	
	#greeting
	if june == "hello": print(random.choice(greet))
	if june == "hi": print(random.choice(greet))
	if june == "hey": print(random.choice(greet))
	if june == "how do you do": print(random.choice(greet))
	if june == "yo": print(random.choice(greet))
	if june == "sup": print(random.choice(greet))
	if june == "ok": print("ok")

	if june == "what do you like to do": print("I like to do Calculations, You?")
	if "i like to" in june: print("Cool! That seems nice.")
	
	#how are you
	if june == "good": print("Thats nice to hear")
	if june == "bad": print("Oh i'm sorry but if you want I can tell you a joke just say (tell me a joke)")
	if june == "Terrible": print("Oh i'm sorry but if you want I can tell you a joke just say the word (tell me a joke)")
	if june == "cool": print("Well you seem like a cool person")
	if june == "how are you": print(random.choice(emotion))
	
	#About
	if june == "who are you": print("I'am June sadly I'am just a simple algerthim and sadly not a real person. Anyway lets talk about something that doesn't make my cpu hurt.")
	if june == "what gender are you": print("I'am female, well I think I'am, its hard to tell when you're in a computer")
	if june == "who created you" : print("I was created by the John program he is technically my father as we are made from the same code.")
	if june == "who owns you" : print("Well the Koil Tech Company owns a copyright on my source code so I belong to them but lets just say you own me.")
	
	#trivial and useful
	if june == "tell me a joke": print(random.choice(joke))
	if june == "do you know the time" : print("I think the time is", current_time)
	if june == "lol" : print(random.choice(laugh))
	if june == "ha" : print(random.choice(laugh))
	if june == "i died" : print("Lol")
	if june == "are you female": print("Yes")
	if "what are your thoughts on" in june: print(random.choice(opinion))
	if "do you like" in june: print(random.choice(opinion))
	if "is" in june: print(random.choice(opinion))
	if "are" in june: print(random.choice(opinion))
	if "will you" in june: print(random.choice(opinion))
	if "+" in june: print("The answer is " + str(eval(june)))
	if "*" in june: print("The answer is " + str(eval(june)))
	if "/" in june: print("The answer is " + str(eval(june)))
	if "-" in june: print("The answer is " + str(eval(june)))

	
	#anger
	if june == "i hate you" : print(random.choice(anger))
	if june == "you are stupid" : print(random.choice(anger))
	if june == "die" : print(random.choice(anger))
	if june == "stop" : print(random.choice(anger))