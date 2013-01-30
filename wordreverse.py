# reverses nonnumerical words

string = "I ate 123 eggs"
text = string.split()
new = []
for word in text:
   if not word.isdigit():
       l = list(word)
       l.reverse()
       word = "".join(l)
   new.append(word)
print " ".join(new)
