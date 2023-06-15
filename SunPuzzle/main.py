from flask import Flask, render_template, request, flash, Response
from puzzle import SunPuzzleCmdLine
import ast

sp = SunPuzzleCmdLine()
movelist = []

app = Flask(__name__)
app.secret_key = "forsmole"

@app.route("/", methods=["GET","POST"])
def index():
    #moves = sp.moves # counter is off by 1, does not increment the first click
    if request.method == "POST":
        panel = request.form["panel"]
        cur_state = request.form["cur_state"]
        f_count = request.form["f_count"]
        cur_state = ast.literal_eval(cur_state) # Treated as str, convert to dict

        f_count = int(f_count)
        cur_state, f_count = sp.panel_config(cur_state, panel, f_count)
        global movelist
        movelist.append(f"You pressed Panel {panel}")
        print(movelist)
        if cur_state == sp.ans:
            flash(f"Congratulations! You have solved the puzzle in {len(movelist)} moves!", "success")
    else:
        cur_state, f_count = sp.reset()[0], sp.reset()[1]
        movelist = []

    # print(cur_state, f_count)
    return render_template("index.html", cur_state=cur_state, f_count=f_count, ans=sp.ans,
                           movelist=movelist)

if __name__ == "__main__":
    app.run()
