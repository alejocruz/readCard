import RPi.GPIO as GPIO
import SimpleMFRC522
import pyrebase

def leerCard():
	
	reader = SimpleMFRC522.SimpleMFRC522()

	#Welcome Message
	print ('Buscando Tarejtas...')
	print('Presiona Ctrl-C para detener')

	try: 
		ID, text = reader.read()
		
		textnuevo= text.strip(' ')
					
	finally:
			GPIO.cleanup()
	return textnuevo
textN= leerCard()
print (str(textN))

def comparar(llave):

	if llave=='123':
		email= "luisalejo@unicauca.edu.co"
		password= "yoelaleejo123"
		config = {
		"apiKey": "AIzaSyA8z1ZSK50myGH-jyN2BRMhkEleHzo3AwE",
		"authDomain": "testpy-69f51.firebaseapp.com",
		"databaseURL": "https://testpy-69f51.firebaseio.com",
		"projectId": "testpy-69f51",
		"storageBucket": "testpy-69f51.appspot.com",
		"messagingSenderId": "755521623259"
		}

		firebase= pyrebase.initialize_app(config)

		auth = firebase.auth()
		#user = auth.create_user_with_email_and_password(email,password)
		user= auth.sign_in_with_email_and_password(email,password)
		if (user):
			print("Ingreso valido")
		else:
			print("Ocurrio un error")
			print(auth.get_account_info(user['idToken']))
	else: 
		print("Usuario no valido")
comparar(textN)
