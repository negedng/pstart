# for I/O functions
import sys
import collections

def main():
    """Asks for a row and count its letters in str and unicode"""
    # python version
    print(sys.version)
    # read stdin
    print("Enter input value: ")
    alma = u"hét"
    korte = "hét"
    # inputvalue for io is automatically unicode
    inputvalue_u = sys.stdin.readline().rstrip()
    inputvalue_s = inputvalue_u.encode()
    # write stdout
    print("alma: " + inputvalue_u + "\n" + "Count_utf8: " + str(len(inputvalue_u)))
    # print doesnt accept inputvalue_s
    print("alma: " + inputvalue_u + "\n" + "Count_str: " + str(len(inputvalue_s)))

    print(alma + " as unicode " + str(len(alma)))
    print(alma + " encode " + str(len(alma.encode())))
    print(alma + " decode " + str(len(alma.encode().decode())))

    print(korte + " as str " + str(len(korte)) + " acts like above")




#runs only if called directly
if __name__ == '__main__':
    main()
