str = 'X-DSPAM-Confidence: 0.8475 '
intr = str. find(":")
print(intr)
yt = str. find("5",intr)
print(yt)

st = str[intr + 1 : yt + 1]
float(st)
print(st)

