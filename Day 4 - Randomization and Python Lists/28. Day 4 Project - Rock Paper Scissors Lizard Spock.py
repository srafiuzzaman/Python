# Sahad Rafiuzzaman
# Date: 12/27/2024

# Rock Paper Scissors Lizard Spock
# You are going to build a Rock, Paper, Scissors, Lizard, Spock game.
# You will need to use what you have learned about randomization and Lists to achieve this.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Raw string
# Prefix the string with r to make it a raw string, which tells Python to ignore escape sequences.
lizard = r"""
                      )/_
               _.--..---"-,--c_
          \L..'           ._O__)_
  ,-.     _.+  _  \..--( /        
    `\.-''__.-' \ (     \_      
      `'''       `\__   /\
                  ')
"""

spock = '''
                            .ss$$$$$$$$$$$$$$$ss.
                       .s$$$$$$$$$$$$$$$$$$$$$$$$$$ss.
                   .s$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$s
                 .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
               .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$s
             .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$s.
            $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
          .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$                                  $$
        $$$$$$$$$$$$$$$$$$     .
       s$$$$$$$$$$$$$$$$$     sssss.                           s
      ss $$$$$$$$$$$$$$$          ssss                      ss$s
     sss   $$$$$$$$$$$            ssss$$$$ss              $$$$s.
    sssss   $$$$$$$$   s.      .sss$$$$$$$$sss      sss$$$$$$s
    ss$ssss  $$$$$$$  sss.  .ss$$$$$$ss$ss     .         s$$$$s.
    ss$s   s  $$$$$$ ss.ss           ..        ss           .sss
     ss   s $s $$$$$ ss..s.                   ss
      s ss$$$$s $$$$ ssssss.                 .ss
    ss     s$$$s $$$ ssssssssss..           ssss.              .
    ss      $$  s $$ ss..ss$$$$sss        .sssss              ..
     s      s$$ss  $ ssss.sss$$$sss       .sssss.     ss..
      s.     $     $ .sss . .ss$sss        .  sssssss...   ss$
        ss   sssss$$ ..ss   ...sssss            .sss.       s
          ss    $$ $ .ss..s .sssssss
            ss$$  $$  .ssssss .sssss              ..       $
                $$$$  .ss$$ssss...s.s        ..sss$$ssss.
               $$.$$$  .ss$$sss.. sss.    .ssss$$s..s$ss. s
               ss ssss  .sssssss...sss.      .ssss$$ss..  .
               ss  ssss   .ssssssss.sss.        .sss.
               ss    .ssss    .sssssssss.               s
               ss      .sssss.  .sssssss.s .. ..ss$s. .s
              ss         sssssss.  .sssssssssssss$$s. .ss
            $ss           ssssssss.   ..sssssssssss  .ss.
          $$$$.            .sssssssss.     ssssss ssss.$s
      s$$$$$$$$s.             ..ssssssssss......ssss. s$$$s
    .s$$$$$$$$$$$s.              .ssssssssssssssss. s$$$$$ss.
       s$$$$$$$$$$$$$$ss..          .ssssssssss. .s$$$$$$$$s
         s$$$$$$$$$$$$$$$$$$$ssss...   ...ss.. s$$$$$$$$$s
           s$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$s
              .s$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$s
                    .s$$$$$$$$$$$$$$$$$$$$$$$$$$$$$s
                          .s$$$$$$$$$$$$$$$$$$$$s
                                ..s$$$$$$$$$$s
'''
game_images = [rock, paper, scissors, lizard, spock]

print("Welcome to Rock Paper Scissor Lizard Spock\n"
      "Rules of RPSLS:\n"
      "Scissors cuts Paper\n"
      "Paper covers Rock\n"
      "Rock crushes Lizard\n"
      "Lizard poisons Spock\n"
      "Spock smashes Scissors\n"
      "Scissors decapitates Lizard\n"
      "Lizard eats Paper\n"
      "Paper disproves Spock\n"
      "Spock vaporizes Rock\n"
      "Rock crushes Scissors\n")

# Reasons for winning
reasons = {
    (0, 2): "Rock crushes Scissors",
    (0, 3): "Rock crushes Lizard",
    (1, 0): "Paper covers Rock",
    (1, 4): "Paper disproves Spock",
    (2, 1): "Scissors cuts Paper",
    (2, 3): "Scissors decapitates Lizard",
    (3, 1): "Lizard eats Paper",
    (3, 4): "Lizard poisons Spock",
    (4, 0): "Spock vaporizes Rock",
    (4, 2): "Spock smashes Scissors",
}

user_choice = int(input("What do you choose?\n"
                        "Type 0 for Rock,\n"
                        "Type 1 for Paper,\n"
                        "Type 2 for Scissors,\n"
                        "Type 3 for Lizard,\n"
                        "Type 4 for Spock.\n"))

if user_choice < 0 or user_choice > 4:
    print("You typed an invalid number, You Lose!")
else:
    print("You chose:")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 4)
    print("Computer chose:")
    print(game_images[computer_choice])

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice, computer_choice) in reasons:
        print("You Win!")
        print(reasons[(user_choice, computer_choice)])
    else:
        print("You Lose!")
        print(reasons[(computer_choice, user_choice)])


