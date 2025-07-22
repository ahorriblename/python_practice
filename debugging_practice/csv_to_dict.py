"""
def csv_to_dict(text):
    lines = text.split("\n")
    dkeys = []
    output = {}
    # Set up dictionary keys from the header row
    for word in lines[0].split(","):
        dkeys.append(word)
    # Create dictionary for each individual line
    for line_num in range(len(lines)):
        sample = {}
        line = lines[line_num].split(",")
        for index in range(len(dkeys)):
            sample[dkeys[index]] = line[index]
        output.append(sample)
    return output
    
"""

def csv_to_dict(text):
    lines = text.split("\n")
    dkeys = []
    # change output from dictionary to list
    output = []
    # Set up dictionary keys from the header row
    for word in lines[0].split(","):
        dkeys.append(word)
    # Create dictionary for each individual line
    for line_num in range(len(lines)):
        sample = {}
        line = lines[line_num].split(",")
        for index in range(len(dkeys)):
            sample[dkeys[index]] = line[index]
        # output.append(sample), no append method for dictionaries

        # do not append the first line, it's all headers
        if line_num != 0:
            output.append(sample)
    return output

print(csv_to_dict("id,color\n1,red\n2,blue\n3,green"))