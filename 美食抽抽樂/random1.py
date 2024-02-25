import random
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def my_choice():
    if request.method =='POST':
        courses = request.form['courses'].split(',')
        course = '最終幸運兒： '+ random.choice(courses)

        return render_template('1.html',food=course)
    return render_template('1.html')

if __name__ == '__main__':
    app.run(debug=True)