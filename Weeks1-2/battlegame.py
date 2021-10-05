while True:  
    while True:
        wizard = "Wizard"
        elf = "Elf"
        human = "Human"
        orc = "Orc"

        wizard_hp = 70
        elf_hp = 100
        human_hp = 150
        orc_hp = 250
        dragon_hp = 300

        wizard_damage = 150
        elf_damage = 100
        human_damage = 20
        orc_damage = 120
        dragon_damage = 50

        print('1) Wizard\n2) Elf\n3) Human\n4) Orc\n5) Quit')
        character = (input("Choose your character: ")).lower()

        if character == '1' or character == 'wizard':
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break

        if character == '2' or character == 'elf':
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break

        if character == '3' or character == 'human':
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break

        if character == '4' or character == 'orc':
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break

        if character == '5' or character == 'quit':
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break

        print("Unknown Character!")

    print('\n' + character + ': HP = ' + str(my_hp) + ' Damage = ' + str(my_damage))
    print('Dragon: HP = ' + str(dragon_hp) +
          ' Damage = ' + str(dragon_damage) + '\n')

    while True:
        if character == '5' or 'quit':
          break
        dragon_hp -= my_damage
        print("The", character, "damaged the Dragon!")
        print("Dragon HP = " + str(dragon_hp) + '\n')
        my_hp -= dragon_damage
        print("The Dragon damaged the you!")
        print("Dragon HP = " + str(my_hp) + '\n')
        if dragon_hp <= 0:
            print("The Dragon has lost the battle")
            break
        if my_hp <= 0:
            print("The " + character + " lost the battle")
            break
    restart = input("Play again? ")
    if restart == 'yes':
        continue
    else:
        break  
