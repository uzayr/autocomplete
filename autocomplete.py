from redisearch import TextField, NumericField, Query, AutoCompleter, Suggestion

ac = AutoCompleter('ac', 'localhost')

ac.add_suggestions(
  Suggestion('google', 5.0),
  Suggestion('goo', 1.0)
)
f= open("location-cnt.txt","r")
for line in f:
    keywords = line.split(" ")
    keywords[1] = keywords[1].replace("_", " ")
    ac.add_suggestions(Suggestion(keywords[1].rstrip("\n"), float(keywords[0])))

#res = ac.get_suggestions('goo')

#res = ac.get_suggestions('goo', fuzzy = True)

