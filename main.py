from time import sleep
import sys
#test
import answer

intro = ('----------\n'
          'Test  Game\n'
          '----------\n')

for x in intro:
      print(x, end='')
      sys.stdout.flush()
      sleep(0.03)
print('\n')

#start game
while True:
      #question 1
      print("select:\n"
            "1. Go left\n"
            "2. Go right\n"
            "3. Go forwards\n"
            "4. Go backwards\n")
      value1 = answer.Uanswer(4)
      answer1 = answer.branch1(value1)
      print(answer1.output())

      #question 2
      print("Get shot?:\n"
            "1. Yes\n"
            "2. No\n")
      value2 = answer.Uanswer(2)
      answer2 = answer.branch2(value2,value1)
      print(answer2.output())

      #finished
      break