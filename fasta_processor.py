def read_file(file_name):
    with open(file_name,"r") as f:
        dataset = f.read().splitlines()
    return dataset

def get_labels(file_name):
    all_labels = []
    dataset = read_file(file_name)
    for data in dataset:
        if(data[0] == '>'):
            all_labels.append(data[1:])
    return all_labels

def get_sequence(file_name):
    all_sequence = []
    dataset = read_file(file_name)
    prevStr = ""
    for data in dataset:
        if(data[0] != '>'):
            prevStr += data
        else:
            all_sequence.append(prevStr)
            prevStr = ""
    all_sequence.append(prevStr)
    return all_sequence

def get_sequence_label(file_name):
    dataset = read_file(file_name)
    all_sequence = []
    all_label = []
    prevStr = ""
    for data in dataset:
        if(data[0] != '>'):
            prevStr += data
        else:
            if(prevStr != ""):
                all_sequence.append(prevStr)
                prevStr = ""
            all_label.append(data[1:])
    all_sequence.append(prevStr)
    return all_sequence,all_label

