from flask import Flask, render_template, send_file

app = Flask(__name__ ,static_folder='./templates/images')

@app.route('/')
def index():
    profile={
        '名前':'木村 彰杜(きむら あきと)',
        '生年月日':'1999年10月20日(24歳)',
        '血液型':'B型',
        '趣味':'ゲーム'
    }
    return render_template('index.html',profile=profile)

@app.route('/')
def home():
    return index()

@app.route('/garary')
def garary():
    return render_template('garary.html')

@app.route('/syuron')
def syuron():
    PATH = './templates/pdf/syuron2024_kimura.pdf'
    return send_file(PATH, as_attachment = True)


if __name__=='__main__':
    app.run(debug=True)