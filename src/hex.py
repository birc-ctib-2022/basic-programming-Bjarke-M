import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]

match command:
    case "encode":
        y=[]
        for i in x:
            y.append(hex(ord(i)))
        encoding = ""
        encoding.join(y)
        print(encoding)

    case "decode":
        hexsplit=x.split('0x')
        hexlist=[i != '0x' for i in hexsplit]
        translation=[int(i,base=16) for i in hexlist]
        decoding = ""
        decoding.join(translation)
        print(decoding)
