from flask import render_template

def errorResponse(errorMsg):
    return render_template('404.html',errorMsg=errorMsg)