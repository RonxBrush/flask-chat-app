from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.secret_key = "secret_key"  # مفتاح التشفير للجلسة
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def chat():
    if "messages" not in session:
        session["messages"] = []  # تهيئة الرسائل عند بدء الجلسة

    if request.method == "POST":
        message = request.form.get("message")
        if message:
            session["messages"].append(message)  # إضافة الرسالة إلى الجلسة
            session.modified = True  # تحديث الجلسة

    return render_template("index.html", messages=session["messages"])

@app.route("/clear", methods=["POST"])
def clear_chat():
    session.pop("messages", None)  # حذف الرسائل من الجلسة
    return "", 204  # إعادة استجابة فارغة

if __name__ == "__main__":
    app.run(debug=True)
