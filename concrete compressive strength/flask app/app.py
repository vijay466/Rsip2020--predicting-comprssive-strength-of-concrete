from flask import Flask, render_template,request
import pickle
app = Flask(__name__)

model = pickle.load(open('concrete (1).pkl','rb'))
print(model)
@app.route('/')
def hello_world():
    return render_template('apply.html')
@app.route('/login')
@app.route('/', methods=['POST'])
def login():
    a = request.form["cement"]
    b = request.form["Blast furnace slag"]
    c = request.form["fly ash"]
    d = request.form["water"]
    e = request.form["super plastisizer"]
    f = request.form["coarse Aggregate"]
    g = request.form["fine Aggregate"]
    h = request.form["Age"]
    total = [[int(a),int(b),int(c),int(d),int(e),int(f),int(g),int(h)]]
    
    p = model.predict(total)
    p =p[0]

    return render_template('apply.html',label = "concrete compressive strength is="+str(p))
if __name__=='__main__':
    app.run(debug = True)
    