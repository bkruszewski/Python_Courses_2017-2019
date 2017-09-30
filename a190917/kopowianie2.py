import copy

nabial = ["mleko", "jajka", "ser"]
chemia = ["domestos", "plyn do naczyn"]

zakupy_wrzesien = [nabial, chemia]
print ("wrzesien:", zakupy_wrzesien)


zakupy_pazdziernik = zakupy_wrzesien.copy()
print ("pazdziernik:", zakupy_pazdziernik)

zakupy_listopad = [x for x in zakupy_wrzesien]
print ("listopad:", zakupy_listopad)

zakupy_grudzien = copy.deepcopy(zakupy_wrzesien)


zakupy_wrzesien.append("gabki")
print ("wrzesien:", zakupy_wrzesien)
print ("pazdziernik:", zakupy_pazdziernik)
print ("listopad:", zakupy_listopad)
print ("grudzien:", zakupy_grudzien)

#print hex((id(zakupy_wrzesien)))


