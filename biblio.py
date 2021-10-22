import re

# input file
filename = 'biblio.txt'

file_input = open(filename, 'r')
# output file
file_output = open('outfile.txt', 'w')

while True:
    # Get next line from file
    line = file_input.readline()
 
    # if line is empty
    # end of file is reached
    if not line:
        break
    
    if len(line.strip()) > 0:
        # find line with title
        x =  re.search('.*title={.*},', line.strip())
        if x:
            new_line = []
            for i,lit in enumerate(line):
                if lit.isupper() and not(line[i-1].isupper()):
                    if line[i-1] == '{' and line[i-2] == '=':
                        new_line.append('{')
                    elif line[i-1] != '{':
                        new_line.append('{')
                if lit.isupper() and not(line[i+1].isupper()):
                    new_line.append(lit)
                    if line[i+1] == '}' and line[i+2] == ',':
                        new_line.append('}')
                    elif line[i+1] != '}':
                        new_line.append('}')
                else:
                    new_line.append(lit)
                
            file_output.writelines(new_line)
        else:
            file_output.writelines(line)
    else:
            file_output.writelines(line)
file_input.close()
file_output.close()
