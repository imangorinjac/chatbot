def read_coins():
    coin_file = open("coins.txt", "r")
    lines = coin_file.readline()
    print(f"Deposit successful! (You have {lines} coins remaining in your account).")
    coin_file.close()
    return int(lines)


def read_data():
    users = {}
    data_file = open("data.txt")
    for i in data_file:
        print(f"Line: {i}")
        splitted_string = i.strip().split(":")
        print(f"Splitted string: {splitted_string}.")
        if len(splitted_string) != 2:
            continue
        username = splitted_string[0]
        password = splitted_string[1]
        users[username] = password
    return users


while True:
    data = read_data()
    bot = "Halt! Welcome to the Doors of Destiny. Should you wish to proceed, you must identify yourself within the Book of Records. "
    print(bot)
    question1 = input("Is your name present in our book?")
    if question1 == "yes":
        question2 = input("What is your passphrase?")
        print("Welcome through, peaceful soul!")
    elif question1 == "no":
        print(
            "Psst! I'm... not supposed to tell you this, but for a small... compensation... I might be able to add you to the Book of Records without the Warden noticing. "
        )
        new_question = input("Would you like to be added to the Book of Records?")
        print(
            "Perfect! I've added you - but I don't come cheap! I charge 100 coins for my services. "
        )
        new_question2 = input("Can you make the deposit?")
        if new_question2 == "yes":
            coins = read_coins()
            username = input("What is your name, then, traveller?")
            password = input("What is your passphrase?")
            if data.get(username, None) == password:

                print(
                    "Welcome through the Doors of Destiny! And it's been a pleasure doing business with you."
                )
            else:
                print(
                    "The passphrase you presented does not match our records! Guards - arrest this intruder!"
                )
