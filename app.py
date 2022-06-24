from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def first_page():  # put application's code here
    return render_template('index.html')


@app.route('/world')
def hello_world():  # put application's code here
    return 'Hello World! For everybody!'


@app.route('/news')
def news():  # put application's code here
    return 'I\'ve got Jetbrains license'


@app.route('/blue')
def blue():  # put application's code here
    return render_template('blue.html')


@app.route('/yellow')
def yellow():  # put application's code here
    return render_template('yellow.html')


@app.route('/green')
def green():  # put application's code here
    background_color = 'green'
    page_title = 'Green'
    cool_news = 'dhsajgfjflsaffgajshgfjlasfgsljgflsjagfljasgflsagdflgsafgsljdfgsajlfgajlsf'
    return render_template('multicolor.html', page_title=page_title, background_color=background_color,
                           news=cool_news)


@app.route('/purple')
def purple():  # put application's code here
    background_color = 'purple'
    page_title = 'Purple'
    cool_news = 'I\'ve got it!'
    return render_template('multicolor.html', page_title=page_title, background_color=background_color,
                           news=cool_news)


if __name__ == '__main__':
    app.run()
