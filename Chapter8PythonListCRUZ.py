block = input('Enter file name:')
black = open(block)
count = 0
for line in black:
        if line.startswith('stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008') :
            count = count + 1
            print('There were', count, 'subject lines in', block)





