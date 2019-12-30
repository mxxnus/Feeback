from flask import Flask, render_template, request

app = Flask(__name__)

# homepage
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # define data with 'name' in html form
        customer = request.form['customer']
        source = request.form['source']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(customer,source,rating,comments)
        if customer == '' or source == '':
            return render_template('index.html', message='Please enter reqired fields')
        return render_template('success.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
