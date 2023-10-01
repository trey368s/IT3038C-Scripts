import datetime
def getSecondsSinceBirth(birthDate):
    now = datetime.datetime.now()
    total = now - birthDate
    return int(total.total_seconds())
birthdateInput = input("Enter your birthdate (MM-DD-YYYY): ")
birthDate = datetime.datetime.strptime(birthdateInput, "%m-%d-%Y")
totalSeconds = str(getSecondsSinceBirth(birthDate))
print("It has been " + totalSeconds + " seconds since your birth.")