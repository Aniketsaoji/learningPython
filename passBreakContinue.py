# pass, break and continue are used to control or get out of loops.
# Takeaways here
# 1. you can have a global variable (names)
# 2. can't name a function after syntax (pass)
# 3. I keep forgetting colons. is this the java semicolon?
# 4. order of functions matter. unlike java.

names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']

def tryPass():
    for name in names:
        if "j" in name.lower():
            pass
        else:
            print(name)

def tryBreak():
    for name in names:
        if "h" in name.lower():
            break
        else:
            print(name)

def tryContinue():
    for name in names:
        if "m" in name.lower():
            continue
        else:
            print(name)

def main():
    tryPass()
    tryBreak()
    tryContinue()


if __name__ == '__main__':
    main()

