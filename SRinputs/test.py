import SRinputs as i

print(f'Tests for {i.__name__}')

number = i.IntInput("ingrese el numero: ", "entrada ni valida")

print(f'{number}')