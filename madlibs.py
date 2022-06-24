# youtuber = "Jayed"# some string variable

# print("Subscribe to " + youtuber)
# print("Subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")
# print("Subscribe to %s" %youtuber)

import hp, code, zombie, hungergames
import random


if __name__ == "__main__":
    m = random.choice([hp, code, zombie, hungergames])
    m.madlib()
