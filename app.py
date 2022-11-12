from flask import Flask
from flask import render_template
from flask import request
from PIL import Image
import pyocr


# flaskを使うのに必要なコード
app = Flask(__name__)


@app.route("/")
def show_form():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    # リクエストファイルの読み込み
    ocr_file = request.files["ocrFile"]
    img = Image.open(ocr_file)
    # OCR準備
    tools = pyocr.get_available_tools()
    tool = tools[0]
    # OCR
    # img.show()
    txt = tool.image_to_string(
        img, lang="jpn+eng", builder=pyocr.builders.TextBuilder()
    )
    if txt == "":
        txt = "読み取りエラー"
    return render_template("upload.html", txt=txt)


# flaskを使うのに必要なコード、デバックトゥルーに,するといちいち開き直さなくてよくなる。
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
