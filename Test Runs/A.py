mps_list = [
     "MPS145",
     "MPS111",
     "MPS235",
     "MPS521",
     "MPS019",
     "MPS800",
     "MPS442",
     "MPS333",
     "MPS612",
     "MPS222"
 ]
req_words=[]
for item in mps_list:
     sum_words=0
     for i in item[3:]:
          sum_words+=int(i)
     if sum_words==10:
          req_words.append(item)
     else:
          continue
print(req_words)