import sys

for line in sys.stdin:
    data = line.strip().split()
    
    if len(data) > 6:
        request = data[6]
        
        if request.startswith('/images/smilies/'):
            print("images_smilies\t1")
