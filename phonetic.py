import sys
from functions import parse, hackerLingo, phonetic, usage

def main():
	mode, data = parse()
	if len(sys.argv) > 1:
		if '-h' in sys.argv or '-hacker' in sys.argv:
			hackerLingo(mode, data)
		else:
			phonetic(mode, data)
	else:
		usage()
	

if __name__ == '__main__':
	main()