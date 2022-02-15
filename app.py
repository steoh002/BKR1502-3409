#!/usr/bin/env python
# coding: utf-8

# In[21]:


from flask import Flask


# In[22]:


app=Flask(__name__)


# In[23]:


from flask import request, render_template
from keras.models import load_model

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        NPTA=request.form.get("NPTA")
        TLTA=request.form.get("TLTA")
        WCTA=request.form.get("WCTA")
        print(NPTA,TLTA,WCTA)
        model=load_model("BKRNN")
        pred = model.predict([[float(NPTA),float(TLTA),float(WCTA)]])
        print(pred)
        s="The predicted bankruptcy score is: "+ str(pred)
        return(render_template("index.html",result="1"))
    else:
        return(render_template("index.html",result="2"))
    
    


# In[ ]:


#if __name__=="__main__":
   # app.run(host=os.getenv('IP', '0.0.0.0'), 
            #port=int(os.getenv('PORT', 4444)))
    
if __name__=="__main__":
    app.run()

    


# In[ ]:




