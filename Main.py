# Tayler Rae Bachmann

# This program is to help you when you are feeling sick but don't want to
# google your symptoms because the first result is always something extreme
# like DEATH, but instead of that, this program will give you a rational
# reason as to why you feel sick

# This section is the introductory section to the program
# and explains what it does and I put it in a function
# for every prompt that is asking for a 'yes' or 'no' answer I am adding a
# while loop that will re-prompt the user for a 'yes' or 'no' if they input
# something else
# for every prompt that is asking the user to rate their pain on a scale of
# 1-10 I'm adding a while loop re-prompting them for a number between 1 and 10
# if they input something else
print("Welcome to the Anti-WebMD program, a program that will take in your "
      "symptoms and NOT make you have a panic attack thinking you have brain "
      "cancer from a simple headache. This program also doubles as an "
      "optional math homework helper at the end!", end=' ')
print()
print("Disclaimer: I AM NOT A MEDICAL PROFESSIONAL, THIS IS NOT A "
      "DIAGNOSIS :)")
print()
print("Before we get started, for any yes or no questions please only "
      "respond with 'yes' or 'no'.")

# This section gathers some user information like name, age, and height
user_name = input("Let's get started! What's your name?")
print("Hi", user_name + "!", "Nice to meet you!")
user_age = input("Let's get started with some basics, how old are you?")
user_height = input("How tall are you?")
print("So it looks like you are,", user_age, "years old and,", user_height)

# In this section I am collecting information about the user's head pain and
# matching it with other possible ailments
head_pain = input("Are you feeling any head pain?")
while head_pain != "yes" and head_pain != "no":
    print("Looks like you didn't answer with a 'yes' or 'no'")
    head_pain = input("Let's try again. Are you feeling any head pain?")
if head_pain == 'yes':
    for x in range(1, 11):
        print(x)
    head_pain_level = int(input("On a scale of 1-10 how bad does your head "
                                "hurt?"))
    while head_pain_level not in range(1, 11):
        head_pain_level = int(input("Please rate your head pain level on a "
                                    "scale of 1-10 only:"))
    if head_pain_level <= 5:
        print("With a pain level of", head_pain_level,
              "you may have a type of headache "
              "(sinus, cluster, or tension), allergies, or eye strain.")
    elif head_pain_level == 6 or head_pain_level == 7:
        print("With a pain level of", head_pain_level,
              "you may have a more intense headache like a migraine, "
              "or you could have a cold or flu.")
    else:
        print("With a pain level of", head_pain_level,
              "you should probably seek medical care from a healthcare "
              "professional.")
else:
    print("Glad to hear your head isn't bothering you, lets move on!")

# In this section I am collecting information about the user's chest pain and
# matching it with other possible ailments
chest_pain = input("Are you feeling any chest pain?")
while chest_pain != "yes" and chest_pain != "no":
    print("Please only enter 'yes' or 'no'")
    chest_pain = input("Are you feeling any chest pain?")
if chest_pain == 'yes':
    for x in range(1, 11):
        print(x)
    chest_pain_level = int(input("On a scale of 1-10 how bad does your"
                                 " chest hurt?"))
    while chest_pain_level not in range(1, 11):
        chest_pain_level = int(input("Please rate your chest pain level on a "
                                     "scale of 1-10 only:"))
    if chest_pain_level <= 5:
        print("With a pain level of", chest_pain_level,
              "you may have a muscle strain, asthma, or allergies.")
    elif chest_pain_level == 6 or chest_pain_level == 7:
        print("With a pain level of", chest_pain_level,
              "you may have a flu, acid reflux, or heartburn.")
    else:
        print("With a pain level of", chest_pain_level,
              "you should probably seek medical care from a healthcare "
              "professional.")
else:
    print("Glad to hear you don't have any chest pain!")

# In this section I am collecting information about the user's stomach pain
# and matching it with other possible ailments
stomach_pain = input("Are you feeling any stomach pain?")
while stomach_pain != "yes" and stomach_pain != "no":
    print("Please only enter 'yes' or 'no'")
    stomach_pain = input("Are you feeling any stomach pain?")
if stomach_pain == 'yes':
    for x in range(1, 11):
        print(x)
    stomach_pain_level = int(input("On a scale of 1-10 how bad "
                                   "does your stomach hurt?"))
    while stomach_pain_level not in range(1, 11):
        stomach_pain_level = int(input("Please rate your stomach pain level "
                                       "on a scale of 1-10 only:"))
    if stomach_pain_level <= 5:
        print("With a pain level of", stomach_pain_level,
              "you may have food poisoning, menstrual cramps, constipation, "
              "or needing to pass gas.")
    elif stomach_pain_level == 6 or stomach_pain_level == 7:
        print("With a pain level of", stomach_pain_level,
              "you may have be having acid reflux, "
              "a muscle strain, or a hernia.")
    else:
        print("With a pain level of", stomach_pain_level,
              "you should probably seek medical care from a "
              "healthcare professional.")
else:
    print("No stomach pain? Nice!")

# This section is the math homework portion that the user can skip
skip_math = input("Do you need help with your math homework?")
while skip_math != "yes" and skip_math != "no":
    print("Please only respond with a 'yes' or 'no'")
    skip_math = input("Do you need help with your math homework?")
# In these sections I will be using remainders, multiplication,
# division, and exponents
if skip_math == 'yes':
    remain_first_num = int(input("Looks like you're working with remainders, "
                                 "go ahead and input the first number:"))
    remain_second_num = int(input("Great! Now input the number you want"
                                  " divide the first number by:"))
    remain_total = remain_first_num % remain_second_num
    print("Looks like the remainder of,", remain_first_num,
          "when evenly divided by,", remain_second_num, "is:",
          remain_total, sep='  ')
    print("Now we can do some more advanced math, like exponents!")
    exponent_first_num = int(input("Go ahead and input the number you'd "
                                   "like to be raised:"))
    exponent_second_num = int(input("Now input the number you'd like to "
                                    "raise the first number by:"))
    exponent_third_num = int(input("And finally, input the number you'd"
                                   " like to raise the previous equation by:"))
    exponent_total = (exponent_first_num ** exponent_second_num) \
                     ** exponent_third_num
    print("So the total of", exponent_first_num, "to the power of",
          exponent_second_num, "and then that to the power of,",
          exponent_third_num, "is:", exponent_total, sep='  ')
    print("Now we can help with multiplication and division!")
    multi_first_num = int(input("Go ahead and input the first number you'd "
                                "like multiplied:"))
    multi_second_num = int(input("Now input the second number you'd like "
                                 "multiplied:"))
    multi_third_num = int(input("And input the third number you'd like "
                                "multiplied:"))
    divide_first_num = int(input("Finally, input the number you'd like the "
                                 "whole thing to be divided by:"))
    total_multi_divide = (multi_first_num * multi_second_num *
                          multi_third_num) / divide_first_num
    print("So when", multi_first_num, "is multiplied by", multi_second_num,
          "and", multi_third_num, "and then the whole thing is divided by",
          divide_first_num, "you get:", total_multi_divide, sep='  ')
else:
    print("No problem!")

# Here I am putting a farewell to the user
print("Well", user_name, "it was very nice meeting you!")
