print ("Welcome to the Avenger Personality Quiz!")
print ("Answer to following questions to see which Avenger you are.")
    
score = 0

Question1 = input("How do you typically recharge your energy?\n(a) time alone\n(b) go to the gym\n(c) work on a group project\n(d) go clubbing\n")
if Question1 == "a":
    score += 1
elif Question1 == "b":
    score += 2
elif Question1 == "c":
    score += 3
elif Question1 == "d":
    score += 4
else:
    print("invalid answer.")
    
Question2 = input("How do you approach meeting new people?\n(a) I don't meet new people\n(b) with reluctance and avoidance\n(c) hesitation but willing to engage\n(d) excitementand ready to party!\n")
if Question2 == "a":
    score += 1
elif Question2 == "b":
    score += 2
elif Question2 == "c":
    score += 3
elif Question2 == "d":
    score += 4
else:
    print("invalid answer.")
    
Question3 = input("How do you feel about being the center of attention?\n(a) I refuse it\n(b) I avoid it when possible\n(c) uncomfortable with it but tolerant\n(d) love it; it's energizing!\n")
if Question3 == "a":
    score += 1
elif Question3 == "b":
    score += 2
elif Question3 == "c":
    score += 3
elif Question3 == "d":
    score += 4
else:
    print("invalid answer.")
    
Question4 = input("How do you typically handle conflict?\n(a) Avoid it hoping it will go away\n(b) reflect on issue before addressing it\n(c) address it head on for quick resolution\n(d) the fight is on!\n")
if Question4 == "a":
    score += 1
elif Question4 == "b":
    score += 2
elif Question4 == "c":
    score += 3
elif Question4 == "d":
    score += 4
else:
    print("invalid answer.")
    
Question5 = input("Which of the following best describes your communication style?\n(a) Quiet and reclusive\n(b) Thoughtful and introspective\n(c) Analytical and thoughtful\n(d) Talkative and outgoing\n")
if Question5 == "a":
    score += 1
elif Question5 == "b":
    score += 2
elif Question5 == "c":
    score += 3
elif Question5 == "d":
    score += 4
else:
    print("invalid answer.")
    
Question6 = input("In a social setting, would you rather:\n(a) Go alone\n(b) be with one close friend\n(c) be in a small group\n(d) be with a large crowd\n")
if Question6 == "a":
    score += 1
elif Question6 == "b":
    score += 2
elif Question6 == "c":
    score += 3
elif Question6 == "d":
    score += 4
else:
    print("invalid answer.")
    
Question7 = input("What are you more passionate about?\n(a) Technology\n(b) the preservation of your culture\n(c) country and patriotism\n(d) being left alone\n")
if Question7 == "a":
    score += 1
elif Question7 == "b":
    score += 2
elif Question7 == "c":
    score += 3
elif Question7 == "d":
    score += 4
else:
    print("invalid answer.")
    
Question8 = input("What type of activities would you prefer to do most?\n(a) laying on a beach\n(b) Hiking in the mountains\n(c) going to a sporting event\n(d) skydiving\n")
if Question7 == "a":
    score += 1
elif Question7 == "b":
    score += 2
elif Question7 == "c":
    score += 3
elif Question7 == "d":
    score += 4
else:
    print("invalid answer.")
    
Question9 = input("When working on a project, what would you prefer?\n(a) working alone somewhere quiet\n(b) colaborating with a team\n(c) working with a few trusted friends\n(d) working with state of the art equipment\n")
if Question9 == "a":
    score += 1
elif Question9 == "b":
    score += 2
elif Question9 == "c":
    score += 3
elif Question9 == "d":
    score += 4
else:
    print("invalid answer.")
    
Question10 = input("When making a decision, what do you rely more on?\n(a) how it might affect others\n(b) orders or directions from someone else\n(c) your gut/personal intuition\n(d) immediate action with some impulsiveness\n")
if Question10 == "a":
    score += 1
elif Question10 == "b":
    score += 2
elif Question10 == "c":
    score += 3
elif Question10 == "d":
    score += 4
else:
    print("invalid answer.")
    

if score >= 35:
    print("You are Iron Man!")
elif score >= 25:
    print("You are Thor!")
elif score >= 15:
    print("You are Captain America!")
elif score >= 5:
    print("You are Hulk!")
else:
    print("You are Nick Fury!")
