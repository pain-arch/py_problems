# Temperature Converter:

def celsius_to_fahrenheit():
    tmp_c =input("Enter the temperature in Celsius: ")

    tmp_f = (9/5 * float(tmp_c)) + 32

    print(f"The temperature in Fahrenheit is: {tmp_f}")


# Simple Interest Calculator:
def simple_interest():
    p = input("Enter the principal amount: ")
    r = input("Enter the rate of interest: ")
    t = input("Enter the time period in years: ")

    si = (float(p) *float(r) * float(t)) / 100

    print(f"The simple interest is: {si}")
    print(f"The total amount is: {float(p) + si}")


# BMI Calculator:
def bmi_calculator():
    weight = input("Enter the weight in kg: ")
    height = input("Enter the height in meters: ")
    the_bmi = float(weight)/ (float(height) ** 2)
    print(f"The BMI is: {the_bmi}")

