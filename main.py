from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) # decorator
def index():
  name = None
  unit = None
  who = None
  if request.method == "POST":
    name = request.form['name']
    unit = request.form['unit']
    who = request.form.getlist('who')
    who_txt = ''
    for who_txt in who:
      who_txt = who_txt + ','
    with open('database.txt', 'a') as file:
      file.write(name + ',' + unit + ',' + who_txt + '\n')   
    return f"Thank you for your submission, {name}!"
  return render_template("index.html", name=name, unit=unit, who=who)
  

app.run(host='0.0.0.0', port=81) 
