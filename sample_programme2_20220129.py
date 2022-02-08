import yaml
import csv
import sys

def main():
    h = 0
    n = len(sys.argv) - 1
    while ( h < n):
        h +=1
        file = sys.argv[h]
        try:
            with open(file) as s:
                with open("file.csv", 'w') as f:
                    obj = yaml.safe_load(s)
                    #writer = csv.writer(f)
                    for k, v in obj.items():
                       writer = csv.writer(f) 
                       writer.writerow([k, v])
                #print(type(obj))
                #print(obj)
        except:
            sys.stderr.write('error: failed to open %s\n' % (file))

if __name__ == '__main__':
    res = main()
    exit(res)
