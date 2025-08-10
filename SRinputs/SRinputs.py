emptymsg = 'Write something'
msgs = ["That's not funny!", "This is not correct!"]

def IntInput(msg: str = 'Write an integer value: ', ermsg: str = 'is not integer.') -> int:
    """
    Prompts the user for input and validates it as an integer.

    The function repeatedly asks for input until a valid integer is provided.
    It does not allow empty inputs.

    Args:
        msg (str): The message to display to the user.
        ermsg (str): The error message to display on invalid input.
    Returns:
        int: The integer value of the valid input.
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
    Prompts the user for input and validates it as a non-empty string.

    The function repeats the prompt until a non-empty string is provided.

    Args:
        msg (str): The message to display to the user.
    Returns:
        str: The validated non-empty input string.
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
    Prompts the user for input and validates it as a float.

    The function repeatedly asks for input until a valid float is provided.
    It does not allow empty inputs.

    Args:
        msg (str): The message to display to the user.
        ermsg (str): The error message to display on invalid input.
    Returns:
        float: the float value of the input.
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
    Prompts the user for a specified number of inputs and returns them as a list.

    This function asks for 'n' inputs and collects them into a list.
    Empty inputs are allowed.

    Args:
        msg (str): the message display for each input prompt.

    Returns:
        list[str]: A list containing all the input strings.
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