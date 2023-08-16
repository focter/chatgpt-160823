#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
import openai

openai.api_key = "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"

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        q = request.form.get("question")
        r=openai.ChatCompletion.create( 
            model="gpt-3.5-turbo", 
            messages = [
                {
                "role": "user",
                "content":q
                }
            ]
   
        )
        return(render_template("Untitled-1.html",result=r["choices"][0]["message"]["content"]))
    else:
        return(render_template("Untitled-1.html",result="waiting"))
if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:




