# create a method to replace a word in a string
def replace_word(s, old_word, new_word):
    slist = s.split()
    for i in range(len(slist)):
        if(slist[i] == old_word):
            slist[i] = new_word
    return " ".join(slist)

companies = "AliExpress, Amazon, Paypal..., Tesla, Facebook"
companies = companies.replace(',', '').replace('.', '')
print(companies)

companies = companies.replace('Facebook', 'Meta')

print(companies)

words = "hello, cava, gutentag, merhaba, hello, cava, hello"

print(words)

words = words.replace('hello', 'hi', 2)

print(words)

message = "how are you doing today?"
message = message.replace('123', '456')
print(message)


for i in range(0, 1000000):
    want_to_continue = input("Do you want to continue? (y/n)")
    print("Oke, let's continue")
    if(want_to_continue == 'n'):
        print("Oke, let's stop")
        break
    
    
    
    
# maak een atm app die vraagt om een pincode
# als de pincode niet klopt druk "Foutieve pincode"
# dan vraagt hij opnieuw tot 4de keer

# als de pincode klopt
# druk "Succesvol ingelogd"

for trial in range(1, 4):
    user_pincode = int(input("Voer je pincode hier toe: "))
    correct_pincode = 1234
    if(user_pincode == correct_pincode):
        print("Succesvol ingelogd")
        break
    else:
        if(trial > 3):
            print("Je card is geblokkeerd")
        else:
            print("Foutieve pincode, probeer opnieuw")