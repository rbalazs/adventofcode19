import os
filepath = os.path.dirname(os.path.realpath(__file__)) + '/input'

module = []
sum = 0


with open(filepath) as fp:
    code = fp.readline().split(',')
    print(code)

    ## TO EASY TO MAKE A WHILE LOOP
    code[1] = 42
    code[2] = 59

    cursor = 0
    target = 0
    opcode = 0
    while cursor < 1000 and opcode != 99:
        try :
            print(code[0+cursor], int(code[1+cursor]), int(code[2+cursor]), int(code[3+cursor]))
            opcode = int(code[0+cursor])
            inputA = int(code[int(code[1+cursor])])
            inputB = int(code[int(code[2+cursor])])
            target = int(code[3+cursor])
            print(opcode, inputA, inputB, target)
            sum = 0
            if opcode == 1:
                sum = inputB + inputA
            elif opcode == 2:
                sum = inputA * inputB
            elif opcode == 99:
                print()
                print ("#################################")
                print (code[0])
                print ("#################################")
                break
            else:
                raise RuntimeError("Wrong opcode:" + opcode)

            code[target] = sum
            print(code)
        except IndexError:
            print("<>", opcode, inputA, inputB, target)
            break
        cursor += 4
    print()
    print("=FINISH=")

