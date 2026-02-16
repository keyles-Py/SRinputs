import sys
from faker import Faker
from time import sleep
import io

"""Name, Url, Mail, Date, PhoneNumber, Id, Handle"""
wait = 0.4

fake = Faker()

GENDERS = {
        'male' : fake.name_male,
        'female' : fake.name_female,
        'nonbinary' : fake.name_nonbinary,
        'default' : fake.name
    }

def FRNameInput(msg : str = 'Write a name: ', gender : str = 'default'):
    temp_stdin = sys.stdin
    try:
        clean_gender = gender.lower()
        sys.stdin = io.StringIO(GENDERS.get(clean_gender)())
        name = input(msg)
        sleep(wait)
        print(name)
        return name
    
    except TypeError as e:
        print(f'Error: {e}')
    finally:  
        sys.stdin = temp_stdin

def FRUrlInput(msg : str = 'Write your link: '):
    temp_stdin = sys.stdin
    try:
        sys.stdin = io.StringIO(fake.url())
        url = input(msg)
        sleep(wait)
        print(url)
        return url 
    
    except Exception as e:
        print(f"Error {e}")
    finally:
        sys.stdin = temp_stdin

def FREmailInput(msg : str = "Write your Email: "):
    temp_stdin = sys.stdin
    try:
        sys.stdin = io.StringIO(fake.email())
        email = input(msg)
        sleep(wait)
        print(email)
        return email
    
    except Exception as e:
        print(f"Error {e}")
    finally:
        sys.stdin = temp_stdin

def FRDateInput(msg : str = "Write your birthday: ", format : str = '%d/%m/%y'):
    temp_stdin = sys.stdin
    try:
        sys.stdin = io.StringIO(fake.date(format))
        date = input(msg)
        sleep(wait)
        print(date)
        return date
    
    except Exception as e:
        print(f"Error {e}")
    finally:
        sys.stdin = temp_stdin

def FRPhoneNumInput(msg :  str = "Write your phone number: ", prefix : str = "+1"):
    temp_stdin = sys.stdin
    try:
        sys.stdin = io.StringIO(fake.phone_number())
        phoneNumber = input(msg)
        sleep(wait)
        print(phoneNumber)
        return phoneNumber
    
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sys.stdin = temp_stdin

def FRIdInput(msg : str = "Write your id: "):
    temp_stdin = sys.stdin
    try:
        sys.stdin = io.StringIO()
        phoneNumber = input(msg)
        sleep(wait)
        print(phoneNumber)
        return phoneNumber
    
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sys.stdin = temp_stdin

def FRHandleInput(msg : str = ""):
    temp_stdin = sys.stdin
    try:
        sys.stdin = io.StringIO(fake.phone_number())
        phoneNumber = input(msg)
        sleep(wait)
        print(phoneNumber)
        return phoneNumber
    
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sys.stdin = temp_stdin