import time


class Triangle:
    def __init__(self):
        self.test = ""
        self.i = 0

    def run(self):
        while True:
            self.test += "*"
            print(self.test)
            time.sleep(0.1)
            self.i += 1
            if self.i == 9:
                while True:
                    self.test = self.test.replace(self.test[-1], "", 1)
                    print(self.test)
                    time.sleep(0.1)
                    self.i -= 1
                    if self.i == 1:
                        self.i = 1
                        self.test = "*"
                        break


test = Triangle()
test.run()
