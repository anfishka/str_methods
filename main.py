

txt = "However, the development team believed a change in drive format could enhance the flexibility of frame design and packaging. " \
      "Therefore, the focus of research was to be to an underfloor, midship-engine rear-wheel drive (UMR) format. " \
      "This could combine higher packaging efficiency along with the sporting characteristics with which rear drive was associated." \
      "The potential in such a change also presented numerous obstacles. " \
      "It was Honda’s first experience to design a car with the engine in the rear half of the vehicle. " \
      "In February of the same year, with that in mind, and to expedite their research, the development team constructed a UMR test vehicle from a first-generation City." \
      "During the test drive, the team members were amazed by the unique handling of the car, which differed greatly from the original FF specification. " \
      "The UMR-version City, in fact, demonstrated superior performance characteristics." \
      " Unfortunately, further development had to be set aside because the level of technology then available to Honda placed certain limits on the car’s ability to present any real advantage over the normal FF version." \
      "However, although the project was shelved, the team members simply could not forget the exhilaration they had experienced with the UMR experiment. " \
      "Moreover, comments had been raised by supporters at the evaluation meetings that the rear-drive City’s dynamic performance should somehow be replicated." \
      "The emphasis in research was therefore modified from drive format to dynamic performance - that which was typically achieved with a vehicle having a lower center of gravity, meaning a sportscar." \
      "It’s the dream of every development engineer to create a sportscar, said Shigeru Uehara, who was engaged in the development project as LPL." \
      "The people who proposed changing the research direction at the evaluation meetings must also have had that dream." \
      "In 1983, another step was taken, in the form of a prototype car fashioned from a CR-X as a means of testing dynamic performance from various perspectives." \
      " This was also the year Honda made its much-heralded return to the F-1 Series. " \
      "Thus, of course, spirits were high at the R&D Center, in anticipation of the possibility that Honda might indeed build sportscars." \
      " Coincidentally, this had often been a subject of discussion at board meetings." \
      "I think the company wanted a car that could bridge its mass production FF models and F-1 cars, Uehara recalled." \
      "They needed a car that would become the new face of Honda. " \
      "Plus, we’d been contacted several times by those who were planning the Acura Division at American Honda concerning similar requests." \
      "Honda’s development engineers finally found an outlet for the passions when in the fall of 1985 the creation of a new sportscar began in earnest."


# 1) Найти и вывести все позиции  -Honda-
# 2) Найти и вывести все позиции  -Honda- В ЛЮБОМ РЕГИСТРЕ
print("\n\n#1,2 Find and print all the positions the word 'Honda', ignore case.\n")

isHonda = "honda"
pos_honda = []

if len(txt) > 0 and len(isHonda) > 0:
      words = txt.lower()
      index = words.find(isHonda)
      if index != -1:
            while index != -1:
                pos_honda.append(index)
                index = words.find(isHonda, index + len(isHonda))

      for i in pos_honda:
            if i + len(isHonda) <= len(txt):
                  word = txt[i:i + len(isHonda)]
                  print(word, "position in txt -> ", i)
else:
      print("Text and isHonda needs to have values!")
# 3) Вывести исходный текст каждое предложение реверсом
print("\n\n#3 Print original text and each sentence needs to be reversed.\n")


rev_sentences = []
if len(txt) > 0:
      sentences = txt.split(".")
      if len(sentences) > 0:
            for i in sentences:
                  rev_sentence = " ".join(reversed(i.split()))
                  rev_sentences.append(" \n| " + rev_sentence)
if len(rev_sentences) >0:
      for i in rev_sentences:
            print(i, end=" ")

# 4) Посчитать и вывести позиции и количество каждого из разделителей
print("\n\n#4 Count and print positions and amounts each of separator.\n")
separator = ["'", "(", ")", "[", "]", ":", "-", "!","@","/","\\","%","*","~",",",".","|"]
pos_separator = []

if len(txt) > 0:
      for i in separator:
            if i in txt:
                  index = txt.find(i)
                  while index != -1:
                        pos_separator.append(index)
                        index = txt.find(i, index+1)
      if len(pos_separator) > 0:
            for i in pos_separator:
                  w = txt[i]
                  print("Symbol ", w, "position in txt ", i )
      else:
            print("No separators found in txt")

      for i in separator:
            print("Symbol -> ",i, "used", txt.count(i), "times")
else:
      print("The text is empty!")

