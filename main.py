from fastapi import FastAPI


app=FastAPI()
@app.get('/')
def index():
    return {'hiee':{"name":"ashwini"}}

@app.get('/about')
def about():
    return {"data":"this is the about page"}