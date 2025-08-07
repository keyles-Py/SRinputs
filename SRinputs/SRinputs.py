emptymsg = 'Write something'
msgs = ["That's not funny!", "This is not correct!"]

def IntInput(msg: str = 'Write an integer value: ', ermsg: str = 'is not integer.') -> int:
    """
    Asks for an input and validates if the input is an integer.
    Returns the integer value if valid,
    otherwise repeates.
    doesn't allow empty inputs.
    """
    while True:
        try:
            text = input(msg)
            if len(text) == 0:
                print(emptymsg)
                continue
            text = int(text)
            break
        except ValueError:
            print(f'{text} {ermsg}')
            continue
        except KeyboardInterrupt:
            print(msgs[0])
            continue
        except EOFError:
            print(msgs[1])  
            continue       
    return text

def StrInput(msg: str = 'Write any string: ') -> str:
    """
    Asks for an input and validates if the input is a string.
    Returns the string if valid,
    otherwise repeates.
    doesn't allow empty inputs.
    """
    while True:
        try:
            text = input(msg)
            if len(text) == 0:
                print(emptymsg)
                continue
            break
        except KeyboardInterrupt:
            print(msgs[0])
            continue
        except EOFError:
            print(msgs[1])  
            continue       
    return text

def FloatInput(msg: str = 'Write a float value: ', ermsg: str = 'is not float.') -> float:
    """
    Asks for an input and validates if the input is a string.
    Returns the string if valid,
    otherwise repeates.
    doesn't allow empty inputs.
    """
    while True:
        try:
            text = input(msg)
            if len(text) == 0:
                print(emptymsg)
                continue
            text = float(text)
            break
        except ValueError:
            print(f'{text} {ermsg}')
            continue
        except KeyboardInterrupt:
            print(msgs[0])
            continue
        except EOFError:
            print(msgs[1])  
            continue       
    return text

def multiInput(num: int, msg: str = 'Write any string: ') -> list:
    """
    Asks for n inputs and returns them in a list.
    allows empty inputs.
    """
    inputs: list[str] = []
    aux : int = 0
    while True:
        try:
            while aux < num:
                text = input(msg)
                inputs.append(text)
                aux += 1
        except KeyboardInterrupt:
            print(msgs[0])
            continue
        except EOFError:
            print(msgs[1])
            continue
        return inputs