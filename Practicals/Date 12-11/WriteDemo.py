
def main():
    outfile = open("info.txt", 'w')
    outfile.write("Bill Clinton\n")
    outfile.write("George Bush\n")
    outfile.write("Barack Obama")

    outfile.close()  #close the file


if __name__ == '__main__':
    main()