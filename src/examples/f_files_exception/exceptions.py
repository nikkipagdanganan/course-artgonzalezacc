import logging

logging.basicConfig(filename='myapp.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

def test_config():
    return True

def divide_two_numbers(num1, num2):

    result = 0

    if(num2 != 0):
        result = num1 / num2
    else:
        return "Division by 0 not allowed"
    
    return result

def multiply_two_numbers():
    num1 = int(input("Enter num1: "))
    num2 = float(input("Enter num1: "))

    result = num1 * num2

    print(result)

def multiply_two_numbers_book_way_exception():

    try:
        num1 = int(input("Enter num1: "))
        num2 = float(input("Enter num1: "))

        result = num1 * num2
    except ValueError: 
        print("Values must be numeric.")

def multiply_two_number_validate():
    num1 = input("Enter num1: ")
    
    while(not num1.isdigit()):
        num1 = input("Enter num1: ")
    
    num2 = input("Enter num2: ")

    while(not num2.isdigit()):
        num2 = input("Enter num2: ")

    result = int(num1) * int(num2)

    print(result)

def open_file_for_reading(file_name):
    
    try:
        file = open(file_name, 'r')

        contents = file.read()

        print(contents)

        file.close
    except IOError:
        print("Cannot read the file, not found ...", file_name)

def open_sales_file_for_reading(file_name):

    try:
        file = open(file_name, 'r')

        total = 0

        for line in file:
            amount = int(line) 
            total += amount
        
        print(total)

        file.close()
    except IOError as err:
        print('Error reading file, not found')
        logger.error(err)
    except ValueError as err:
        print('File contains invalid data')
        logger.error(err)


    
