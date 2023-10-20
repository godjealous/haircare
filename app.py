from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query_and_answer')
def query_and_answer():
    return redirect("https://e2f490f27fae70f69f.gradio.live")

@app.route('/diagnose')
def diagnose():
    return redirect("https://fe1baa30f0f892b300.gradio.live")

@app.route('/plan')
def plan():
    return redirect("https://fe1baa30f0f892b300.gradio.live")

@app.route('/agent')
def agent():
    return redirect("https://fe1baa30f0f892b300.gradio.live")

@app.route('/text2img')
def text2img():
    return redirect("https://fe1baa30f0f892b300.gradio.live")






if __name__ == '__main__':
    app.run(debug=True)

