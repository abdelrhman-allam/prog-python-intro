text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(':')
num = text[pos+1:len(text)];
striped = num.strip();
fnum = float(striped)
print(fnum)

                
