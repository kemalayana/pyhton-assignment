import random

def rockscipap():
    user_choice = None
    user_score = 0
    comp_score = 0
    
    
    while user_choice != "exit": # kullanıcı exit yazdığında döngü sona erecek
        choices = ["r", "s", "p"]
        user_choice = input("What's your choice? Rock(r), Scissors(s) or Paper(p): ").lower().strip()
        while user_choice not in choices and user_choice != "exit": # farklı karakter yazma ihtimaline karşı
            user_choice = input("Invalid choice..")
        if user_choice == "exit": # çıkış komutu
            print("You ended the game...")
            break
        comp_choice = random.choice(choices)
        if comp_choice == user_choice: # beraberlik
            print("Tie!")
        elif (user_choice == "p" and comp_choice == "r") or (user_choice == "r" and comp_choice == "s") \
            or (user_choice == "s" and comp_choice == "p"): # kullanıcı kazanırsa
            print("You won!!")
            user_score += 1
        else: # bilgisayar kazanırsa
            print("You lost...")
            comp_score += 1
        if user_score == 3:
            print("Congrats.... You deserved a chocolate...")
            break
        elif comp_score == 3:
            print("Sorry.. You lost the game...")
            break
       
        print(f"Your choice: {user_choice}", f"Computer choice: {comp_choice}", sep=" || ") # elin sonuçları
        print(f"Your score: {user_score}", f"Computer score: {comp_score}", sep="\n")


rockscipap()
