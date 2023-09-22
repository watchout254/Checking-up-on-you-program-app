#daily check on you program
import sys

print("\t\t\t\t😊 😇WELCOME TO CHECK ON YOU APP 🙂 🙃.")
print("\t\t\t\t🤙🏼🤙🏼Developed by DANIEL MUKENYA🙌🏼 👐🏼")
print("Let's find out how life's sailing on your end (great, fine, quite well, bad) 🙏🏼💪🏼\n")

greeting = input("Your name: ").lower()
print("👋🏼Hey",greeting)
doing = input("🤞🏼How you doing today?: ").lower()
if doing == "great":
    print("That's great🤜🏼🤛🏼.")
    sailing = input("🤞🏼How is your week so far(good/bad)?🙂 🙃").lower()
    if sailing == "good":
        print(f"Lovely, Blessed week ahead {greeting}👏🏼")
    elif sailing == "bad":
        print(f"Don't worry, sometimes we all need a break. Take a nap {greeting}🙃")

elif doing == "fine":
    print(f"You sure everything is fine {greeting} 🙃?")
    fine = input("Wanna talk about it maybe?").lower()
    if fine == "yes":
        print("It's a safe place, talk to me.🙂")
        wrong = input("Vent here: ").lower()
        for i in wrong:
            print(f"Everything's gonna be alright {greeting} 🙂 ")
            print(f"Take a deep breathe and pray about it. Bless. Love. In a bit yeah.")
    elif fine == "no":
        print(f"Have a lovely day {greeting} 👏🏼")

elif doing == "quite well":
    print(f"What's the occasion {greeting}?🙂")
    occassion = input("You are psyched up what's the rada? 🙂 ")
    for a in occassion:
        print(f"I'm happy for you {greeting} 👏🏼👏🏼👏🏼. Bless up yeah. Ciao")

elif doing == "bad":
    print(f"{greeting} 🙃, not sure what you want to hear right now but you will be okay with time\n"
          f"Trust me, we've all been there. You are doing great. Chin up mandem.")
else:
    print(f"Byeee  {greeting} 🙃🙃")
    sys.exit()



