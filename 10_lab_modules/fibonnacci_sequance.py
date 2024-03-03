from lab_modules.fibo_functions import create_seq, locate_number
sequence = []

while True:
    command = input()
    if command == "Stop":
        break

    if "Create" in command:
        number = int(command.split()[2])
        sequence = create_seq(number)
        print(*sequence)
    else:
        num = int(command.split()[1])
        result = locate_number(num, sequence)
        print(result)
