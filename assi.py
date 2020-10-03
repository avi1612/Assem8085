fname = input("Enter file name: ")
count = 0.0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    a = line.find("a")
    b = float(line[a+2:])
    count = count + b + c
print("Done")
d ="hello_world"
#this is optimised code
