import sys

fileList = sys.argv[1:]

# input: [string1, string2]
# // output: [[key1, key2], []]

print([
    [fileList[0][:5], fileList[0][5:10]],
    [fileList[1][:5], fileList[1][5:10]]
    ])
sys.stdout.flush()
