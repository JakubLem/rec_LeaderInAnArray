#Searching leader in an array -- rec || Jakub Lemiesiewicz 
def checkertab(tab):
    checker = tab[0]
    for i in tab:
        if checker!=i:
            return False
    return True

def lider(tab):
    l = len(tab)
    if l==0:
        return False
    if checkertab(tab)==False:
        i = 0
        while i<l-1:
            if tab[i]!=tab[i+1]:
                tab.pop(i)
                tab.pop(i)
                l-=2
            i+=1
    else:
        return tab
    return lider(tab)

#main() {
tab = [1]
lid = lider(tab)
if lid == False:
    print("There is no leader")
else:
    if len(lid)>=((len(tab)/2)+1):
        print(lid[0])
    else:
        print("There is no leader")
#}
