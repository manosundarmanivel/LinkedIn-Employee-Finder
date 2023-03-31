# from flask import Flask, render_template, request
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/submit', methods=['POST'])
# def submit():
#     name = request.form['name']
#     email = request.form['email']
#     return f"Hello {name}, your email is {email}"
#
# def input():
#     name = request.form['name']
#
#     return name
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def display_csv():
    with open('profile.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        rows = list(csv_reader)
        data = [[row['profile links'],row['image link']] for row in rows]

        return render_template('index.html', rows=rows, data =data )

if __name__ == '__main__':
    app.run()


















