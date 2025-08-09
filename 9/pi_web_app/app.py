from flask import Flask, render_template, request
import os

app = Flask(__name__)

# 读取 π 的字符串
with open("pi_digits.txt", "r", encoding="utf-8") as f:
    pi_str = f.read()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    birthday = ""
    if request.method == "POST":
        birthday = request.form.get("birthday", "").strip()
        if not birthday:
            result = "请输入生日！"
        elif not birthday.isdigit() or len(birthday) != 4:
            result = "请输入4位数字（例如 0405）"
        else:
            if birthday in pi_str:
                index = pi_str.index(birthday)
                start_idx = max(0, index - 10)
                end_idx = index + len(birthday) + 10
                context = pi_str[start_idx:end_idx]
                result = {
                    "found": True,
                    "position": index,
                    "context": context
                }
            else:
                result = {"found": False}

    return render_template("index.html", result=result, birthday=birthday)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))