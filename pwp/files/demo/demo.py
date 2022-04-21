# writing files
with open('/home/sean/Programming/python-projects/pwp/files/demo/first.txt', 'r') as f:
    print(f.read())
 
# reading files
with open('/home/sean/Programming/python-projects/pwp/files/demo/write.txt', 'w') as f:
    f.write('Hello\n')
    f.write('World')

# reading files with rstrip
with open('/home/sean/Programming/python-projects/pwp/files/demo/write.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        print(line)