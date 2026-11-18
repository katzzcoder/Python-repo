from app import app

@app.route("/welcome/product")
def product():
    return "product page"