from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        link = request.form['link']
        try:
            yt = YouTube(link)
            title = yt.title
            views = yt.views
            channel = yt.author
            yd = yt.streams.get_highest_resolution()
            yd.download('C:/Users/ajink/OneDrive/Desktop/Power Of Python/YouTube Videos')
            return render_template('index.html', title=title, views=views,channel=channel, message='Downloaded Successfully!')
        except Exception as e:
            return render_template('index.html', error=str(e))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
