# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
spam1 = "Make a lot of money".lower();
spam2 = "buy now".lower();
spam3 = "subscribe this".lower();
spam4 = "click this".lower();
text = input("Enter a sentence:\n".lower());
if(spam1 in text or spam2 in text or spam3 in text or spam4 in text):
    # print(text);
    print("This is Hundred Percent Spam");
else:
    print("Its good to go not a spam");
