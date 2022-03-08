import pickle
import json
from flask import Flask, render_template, request, jsonify   

@app.route("/submitjSON", methods=["POST"])
def processjSON():
    global p

    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    l1=jsonObj['List1']
    lst1=l1.split(',')
    l2=jsonObj['List2']
    lst2=l2.split(',')
    for i in range((len(lst2))):
        lst2[i]=int(lst2[i])
    d=False
    for i in lst1:
        if i not in p:
            d=True
            break
    if d==False:
        for i in range((len(lst2))):
            if lst1[i] in p:
                if p[lst1[i]]>lst2[i]:
                    p[lst1[i]]-=lst2[i]
                else:
                    p[lst1[i]]=0
        myfile=open("S.txt","wb")
        pickle.dump(p,myfile)
        myfile.close()
        myfile=open("S.txt","rb")
        p=pickle.load(myfile)
        myfile.close()
        s="Items Removed From Stock Successfully"
        return str(s)
    else:
        return "Process Cancelled Because One Of The items You Tried To Remove Not Found"


if __name__=="__main__":
    app.run()
