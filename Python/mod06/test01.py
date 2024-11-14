# funtkio esimerkkejä
""""
def do_something():
    print("Doing ")
    print("something")
    return None

return_value = do_something()
print(return_value)


def combine_strings(string1, string2):
    combination = f"{string1}, {string2}"
    print(combination)

combine_strings("auto", "ajaa")
combine_strings("kuski", "jarruttaa")

def calculate(calc_type, number1,number2):
    if calc_type == "sum":
        return number1+number2
    elif calc_type == "division":
        return number1/number2

print(calculate("sum",2.9, 7.7,))
print(calculate("division", 2.9, 7.7,))

def calculate_sum(numbers):
    total_sum = 0
    for num in numbers:
        total_sum = total_sum + num
    return total_sum

nums = [3,4,5]
print(calculate_sum(nums))
print(calculate_sum([3,4,5,10]))


def calculate_sum2(*numbers):
    total_sum = 0
    for num in numbers:
        total_sum = total_sum + num
        return total_sum
print(calculate_sum2([3,4,5]))

"""



def tervehdi(kerrat):
    for i in range(kerrat):
        print ("Hyvää päivää " + str(i+1) + ". kerran")
    return

print ("Päivä alkaa tervehdyksillä.")
tervehdi(5)
print ("Tervehditään lisää.")
tervehdi(2)


