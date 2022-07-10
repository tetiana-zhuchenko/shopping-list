# export FLASK_ENV=development
# export FLASK_APP=app.py
# flask run
# [--port=5002]
# *(port optional)

# To make a bar with: background color: magenta, dimensions 100x250 pixels,
# with centered text inside it "Centered Text !!!" using css class (at least 2 classes You need)

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


if __name__ == '__main__':
    app.run()