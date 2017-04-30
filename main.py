from flask import Flask, render_template, request, flash, url_for, redirect
app = Flask(__name__)


@app.route('/story', methods=['GET', 'POST'])
def story_page():
    a = []
    error = None
    try:
            if request.method == 'POST':
                b = request.form['usernameb']
                print (b)
                return render_template('form.html')
            else:
                return render_template('form.html')

    except Exception as e:
            flash(e)
            return render_template("form.html", error=error)

    



    
        
@app.route('/list', methods=['GET', 'POST'])
def list_page():
    return render_template("list.html")           




if __name__ == '__main__':
    app.run()