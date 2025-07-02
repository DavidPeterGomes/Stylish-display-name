letter = ''' Dear <|name|>,
          You are selected!
          <DATE>'''
print(letter.replace("<name>","David").replace("DATE","23/6/25"))