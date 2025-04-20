print("🏝️ Welcome to Treasure Island! 🏝️\n")
print("💰 Your mission is to find the hidden treasure! 💰\n")

# First Choice: Dirt Trail
dirt_trail = input("🚶 You arrive at a dirt trail and see two paths. Where will you go? (left/right) \n").lower()
if dirt_trail == "left":
    print("\n🌊 You arrive at a lake. \n")
    
    # Second Choice: Lake
    lake = input("⛵ Will you swim across it or wait for a boat? (swim/wait) \n").lower()
    if lake == "wait":
        print("\n🏔️ You arrive at a mysterious cave with three different-colored entrances.\n")
        
        # Third Choice: Cave
        cave = input("🟠 Which one will you choose: red, yellow, or blue? \n").lower()
        if cave == "yellow":
            print("\n🎉 Congratulations! You found the treasure and won! 🎉")
        else:
            print("\n💀 You entered a dark room full of undead skeletons... Game over! 💀")
    else:
        print("\n🐊 You got eaten by crocodiles in the lake. Game over! 💀")
else:
    print("\n⚠️ You fell off the dirt trail into a deep hole... Game over! 💀")
