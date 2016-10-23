def parse_row(header, delim=','):
    return [k.strip() for k in header.split(delim)]

def to_layers(data):
    layers = []
    for k in data:
        item = {
            "name": k,
            "values": []
        }
        for y in data[k]:
            item["values"].append({
                "x": y,
                "y": data[k][y]
            })
        layers.append(item)
    return layers

def main(file_in, count=5, delim=','):
    with open(file_in, 'r') as fd_in:
        header = fd_in.readline()
        keys = parse_row(header, delim)
        data = {}
        for line in fd_in.readlines()[0:count]:
            for i, v in enumerate(parse_row(line, delim)):
                if i == 0:
                    y = int(v)
                else:
                    k = keys[i]
                    data[k] = data.get(k,{})
                    data[k][y] = float(v) 
    fd_in.close()
    return to_layers(data)

if __name__ == '__main__':
    print main('energy.csv', 100, ';')