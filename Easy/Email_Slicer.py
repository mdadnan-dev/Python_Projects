
email = input("Enter your email: ")   # adn123@gmail.com

if '@' in email:
    username = email[: email.index('@')]
    domain = email[email.index('@') + 1 :]
    print(f"Your Username is {username}\nYour Domain is {domain}")
else:
    print("Your email is invalid.")