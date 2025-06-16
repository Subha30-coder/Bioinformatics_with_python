from DNA_toolkit import *    # import * ie import everything

# rndDNAStr = "ATTTCGT"
# print(validateSeq(rndDNAStr))

# rndDNAStr = "ATTTCGTX"
# print(validateSeq(rndDNAStr))

# rndDNAStr = "aTtTCgT"
# # print(validateSeq(rndDNAStr))

import random
rnd = ''.join(random.choices(["A","C","G","T"], k=50))
print(validateSeq(rnd))
print(countNucFrequency(rnd))