strf = 'X-DSPAM-Confidence: 0.8475 '
intr = strf. find(":")
print(intr)
yt = strf. find("5",intr)
print(yt)

st = strf[intr + 1 : yt + 1]
ut = float(st)
print(ut)
