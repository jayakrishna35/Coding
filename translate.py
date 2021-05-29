def trans(pr):
   trans=""
   for let in pr:
       if let.lower() in "aeiou":
           if let.isupper():
               trans=trans+"G"
           else:
               trans=trans+"g"
       else:
          trans=trans+let
   return trans
print(trans(input("Enter text: ")))
