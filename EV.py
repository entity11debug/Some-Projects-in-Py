#Conditions
#C-1) EMAIL HAS TO HAVE AT LEAST 6 CHARACTERS.
#C-2) EMAIL HAS TO START TO AN ALPHABET.
#C-3) EMAIL HAS TO HAVE 1 "@" AND NOT MORE THAN 1.
#C-4) EMAIL HAS TO HAVE "." IN -3 OR -4 INDEX (THAT MEANS RIGHT BEFORE THE .IN / .COM)
#C-5) EMAIL MUST BE IN LOWER CASE
user_email = input("Enter Email : ")
if len(user_email) >=6:
  if user_email[0].isalpha():
    if "@" in user_email and user_email.count("@")==1:
      if user_email[-4]=="." or user_email[-3]==".":
        if user_email == user_email.lower():
          pass
        else:
          print("Wrong Email! Email You must use lowercase")
      else:
        print("Wrong Email! (you used dot in wrong place OR didn't use it!)")
    else:
      print("Wrong Email! (Either no @ or more than 1)")
  else:
    print("Wrong Email (You must start with an alphabet)")
else:
  print("Wrong Email (character is lower than 6)")
