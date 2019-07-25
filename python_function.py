newdic = {
"ping" :  1,
"bass" :  3
}
def test(newdic):
  for key, val in newdic.items():
    if key == "bass":
      i = 0
      print(val)

test(newdic)
