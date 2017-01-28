zoo = ['lion', "elephant", 'monkey']

if __name__ == "__main__":
    with open('output.txt', 'a') as f:
        for i in zoo:
            f.write(i + '\n')
