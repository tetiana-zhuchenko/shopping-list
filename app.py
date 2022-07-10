# export FLASK_ENV=development
# export FLASK_APP=app.py
# flask run --port=5002

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<color>')
def first_page(color):
    # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    color_list = ['red', 'orange', 'yellow', 'green', 'lightblue', 'blue', 'magenta', 'black', 'white']

    background_color = color
    page_title = background_color.capitalize()
    news_color = background_color.capitalize()

    return render_template('multicolor.html', background_color=background_color, page_title=page_title,
                           news_color=news_color, color_list=color_list)


""" def green():  # put application's code here
     background_color = 'green'
     return render_template('multicolor.html', page_title=page_title, background_color=background_color,
                            news=cool_news)


# return render_template('index.html')


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
                           news=cool_news)"""

if __name__ == '__main__':
    app.run()
