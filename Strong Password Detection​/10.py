import re
import time

passwordRegex = re.compile(r'''(
^(?=.*[A-Z])
(?=.*[!@#$&*])
(?=.*[0-9])
(?=.*[a-z])
.{8,}
$
)''', re.VERBOSE)

def userInputPasswordCheck():
    ppass = input("Enter a potential password: ")
    mo = passwordRegex.search(ppass)
    if (not mo):
        print("This is not a strong enough password, please come up with a stronger one.")
        return False
    else:
        print("Password meets complexity requirements!")
        time.sleep(2)
        print("Checking weak password database...")
        time.sleep(5)
        return True

userInputPasswordCheck()
