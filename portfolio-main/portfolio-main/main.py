#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)

    button_html = request.form.get('button_html')
    return render_template('index.html', button_html=button_html)

    button_discord = request.form.get('button_discord')
    return render_template('index.html', button_discord=button_discord)

@app.route('/feedback', methods=['POST'])
def feedback():
    if request.method == 'POST':
        email = request.form.get('email')
        text = request.form.get('text')
        print(email, text)
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)