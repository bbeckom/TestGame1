def Uanswer(optionstotal):
    # Output a number for answer to question. Checking to ensure number is chosen.
    while True:
        answer = input(": ")
        try:
            val = int(answer)
            if val in range(1, optionstotal + 1):
                print("")
                return val
            else:
                print("not an option")
                continue
        except:
            print("put in a number")
            continue


class branch1(object):
    # First question branch
    def __init__(self, value):
        self.value = value

    def output(self):
        if self.value == 1:
            return "You are shot at once!"
        if self.value == 2:
            return "You're shot at twice!"
        if self.value == 3:
            return "You're shot at three times!"
        if self.value == 4:
            return "You're shot at four times!"


class branch2(object):
    # Second question branch
    def __init__(self, value, value2):
        self.value = value
        self.value2 = value2

    def output(self):
        if self.value == 1:
            return "You die"
        if self.value == 2 and self.value2 == 1:
            return "You dodged the bullet!"
        if self.value == 2 and self.value2 > 1:
            return "You dodge " + str(self.value2) + " bullets!"
