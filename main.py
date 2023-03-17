from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) # decorator
def index():
  name = None
  unit = None
  who = None
  if request.method == "POST":
    name = request.form['name']
    unit = request.form['class']
    who = request.form.getlist('who')
    who_txt = ''
    for who in who:
      who_txt = ' ' + who
    with open('database.txt', 'a') as file:
      file.write(name + ',' + unit + ',' + who_txt + '\n')   
  return render_template("index.html", name=name, unit=unit, who=who)
  

app.run(host='0.0.0.0', port=81) 
