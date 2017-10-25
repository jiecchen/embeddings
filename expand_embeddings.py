import sys


def build_dict(map_file):
    mp = {}
    with open(map_file, 'r') as fin:
        for line in fin.readlines():
            line = [x.strip() for x in line.split()]
            if len(line) < 2:
                break
            mp[line[0]] = line[1:]
    return mp

def process(emb_file, map_dict):
    # TODO: check the input format
    tmp = 'dafdasfadfasdf'
    ftmp = open(tmp, 'w')
    with open(emb_file, 'r') as fin:
        line = fin.readline()
        _, dim = [x.strip() for x in line.split()]
        dim = int(dim)
        num_line = 0
        for line in fin.readlines():
            line = [x.strip() for x in line.split()]
            assert len(line) == dim + 1
            name = line[0]
            line = ' '.join(line[1:])
            for x in map_dict[name]:
                print >> ftmp, x, line
                num_line += 1
    ftmp.close()
    print num_line, dim
    with open(tmp, 'r') as fin:
        for line in fin.readlines():
            print line,
    

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'usage: this_script map_file embeddings_file'
    map_file = sys.argv[1]
    emb_file = sys.argv[2]
    map_dict = build_dict(map_file)
    process(emb_file, map_dict)
