# ATM app

# maak een keer een vast-pincode aan
correct_pincode = 1234
correct_card_number = "1111 2222 3333 4444"

user_card_number = input("Voer je card nummer toe: ")

for trial in range(1, 4):
    
    print("Trial: {0}".format(trial))
    
    user_pincode = int(input("Voer je pincode hier toe: "))
    
    if(user_pincode != correct_pincode and trial < 3):
        print("Foutieve pincode, probeer opnieuw")
        
    elif(user_card_number != correct_card_number):
        print("Foutieve card nummer, probeer opnieuw")

    elif(user_pincode != correct_pincode and trial >= 3):
        print("Je card is geblokkeerd! Probeer om contact op te nemen met de bank..")
        break
    
    elif(user_card_number == correct_card_number and user_pincode == correct_pincode):
        print("Succesvol ingelogd")
        break
    
    else:
        print("Onbekende fout")
        break