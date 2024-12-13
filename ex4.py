from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
#    return Flask.render_template() # Внутри () пишем название html-файла в кавычках
    return render_template() # Внутри () пишем название html-файла в кавычках

if __name__ == "__main__":
    app.run()