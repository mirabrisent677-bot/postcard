import os
from flask import Flask, render_template

app = Flask(__name__)

# پیام را از اینجا به‌راحتی تغییر بده
MESSAGE = """
کیرم تو چاهزاده رضا پخلوی
همچنین کیر جمیع دلاور مردان ایرانی تو خاندان ایران ویران کن پخلوی 
از طرف جمیع مردم ایران
"""

@app.route("/")
def home():
    return render_template("index.html", message=MESSAGE)

if __name__ == "__main__":
    app.run(debug=True)
