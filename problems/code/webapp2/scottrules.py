from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    #assert 0
    return '<a href="/scott_rules">Click me!</a>'

# adding a new page
@app.route('/scott_rules')
def scott_rules():
    content = ''
    # generate some content
    for i in xrange(1000):
        content += 'scott rules! '
    return render_template('template.html', content=content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085, debug=True)