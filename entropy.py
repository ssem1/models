from collections import Counter
import numpy as np

# collect and clean data
file1 = open("entropydata.txt", "r")
text = file1.readlines()
file1.close()
cleaned_text = list(map(lambda x:x.strip(),text))

# create distribution
print(Counter(cleaned_text))
distribution = Counter(cleaned_text)

# calculate probabilities and store in list
distvals = distribution.values()
listdistvals = list(distvals)
sumvals = sum(listdistvals)
x = 0
y = 0 
probabilities = []
while x < len(listdistvals): 
    y = listdistvals[x]/sumvals
    probabilities.append(y)
    x+=1 
print(probabilities)
 
# calculate entropy 
lenholder = 0
w = 0 
while lenholder < len(probabilities): 
    w = w + (-(probabilities[lenholder]*np.log2(probabilities[lenholder])))
    lenholder +=1
print(w)