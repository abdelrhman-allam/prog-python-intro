# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
confidence = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") : 
        pos = line.find(":")
        confidence += float((line[pos+1:len(line)]).strip())
        count = count +1
avg = confidence / count

print("Average spam confidence: " + str(avg) )
