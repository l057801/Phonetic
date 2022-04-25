from pathlib import Path
from dictionaries import codes, hack
import time
import sys


def phonetic(mode, data):
	if mode == 'file':
		for line in data:
			for word in line:
				for n in word:
					n = str(n).lower()
					if n in codes:
						print(f'{n} - {codes[n]}')
						time.sleep(0.2)
					else:
						pass
				print('\n')
	elif mode == 'text':
		for word in data:
				for n in word:
					n = str(n).lower()
					if n in codes:
						print(f'{n} - {codes[n]}')
						time.sleep(0.2)
					else:
						pass
				print('\n')


def hackerLingo(mode, data):

	if mode == 'file':
		for line in data:
			out = f''
			for word in line:
				for n in word:
					n = str(n).lower()
					if n in hack:
						out += hack[n]
					else:
						out += n
					print(out ,end='\r')
					time.sleep(0.05)
				out += f' '
			print('')
	elif mode == 'text':
		out = f''
		for word in data:
			for n in word:
				n = str(n).lower()
				if n in hack:
					out += hack[n]
				else:
					out += n
				print(out ,end='\r')
				time.sleep(0.2)
			out += f' '


def read_file(name):

    """ only setup for txt files at the moment 
        returns a list of lists in which each 
        list is a line  """
    
    p = Path(name)
    absPath = p.absolute()

    allWords = []

    if absPath.suffix == '.txt':
        with open(absPath,mode='r')  as f:
            for line in f.readlines():
                lineList = []
                for word in line.split(' '):
                    lineList.append(word.rstrip('\n'))
                allWords.append(lineList)
    
    return allWords

def parse():
	""" parses input and returns a list of words """
	
	if '-f' in sys.argv:
		mode = 'file'
		data = read_file(sys.argv[sys.argv.index('-f') + 1])
		
	else:
		mode = 'text'
		data = [word for word in sys.argv[1:] if word not in ['-h','-hacker']]
	
	return [mode, data]



def usage():
	print('General usage: phonetic <flag> <words>\nNOTE: flags can be concurrently used -h -f but not combined -hf')
	print('\nFlags:\n\t-f:\tto specify file (.txt currently supported)\n\t\t e.g. phonetic -f test.txt')
	print('\t-h:\tto specify leetmode\n\t\t e.g. phonetic -h mr.robot')

