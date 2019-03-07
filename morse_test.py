from morse import Morse
import sys
import argparse

def convert(iFile, oFile, mode):

    try:
        with open(iFile) as i, open(oFile, 'w') as o:
            for line in i:
                line = line.strip()
                if mode == 'decode':
                    m = Morse(line).decode()
                elif mode == 'encode':
                    m = Morse(line).encode()
                else:
                    print('Unknown mode. Exiting')
                    sys.exit()
                o.write('{}\n'.format(m))
    except TypeError:
        print("Could not open files")
        parser.print_help()

def main():
    
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.epilog = "Convert text to morse:\npython {} -i path/to/text -o path/to/morse encode\n\n".format(sys.argv[0])
    parser.epilog += "Convert morse to text:\npython {} -i path/to/morse -o path/to/text decode\n".format(sys.argv[0])
    parser.add_argument("-i", metavar="input file", help="input file")
    parser.add_argument("-o", metavar="output file", help="output file")
    parser.add_argument("mode", help="decode/encode")
    args = parser.parse_args()

    iFile = args.i
    oFile = args.o
    mode = args.mode
    convert(iFile, oFile, mode)


if __name__ == '__main__':
    main()
