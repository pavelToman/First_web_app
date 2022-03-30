from flask import Flask, render_template, request

app = Flask(__name__)

#použití HTML a dynamického teplate - /hw vypíše Hello, world nebo pokud je hw/?name=Pavel, tak vypíše Hello, Pavel
@app.route("/hw/")
def hw():
    return render_template("hw.html", name=request.args.get("name", "world"))

#použití dynamické routy a vrácení stringu s formatem. Pokud zadám /hello >>> Hello, Pablo, pokud zadám /hello/Pavel >>> Hello, Pavel
@app.route("/hello/")
@app.route("/hello/<jmeno>")
def hello(jmeno="Pablo"):
    return 'Hello, {}!'.format(jmeno)

#HTML a dynamický tamplate s dynamickou routou - pokud zadám /hell >>> Hello, Pes, pokud zadám /hell/kočka >>> Hello, kočka
@app.route("/hell/")
@app.route("/hell/<zvire>")
def hell(zvire="Pes"):
    return render_template("zvire.html", zvire=zvire)

#index s inputem od uživetele a metodou POST
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/greet", methods=["POST"])
def greet():
    return render_template("greet.html", jmeno=request.form.get("toto"))

#Pokud mám všude POST metodu, tak toto funguje, jak dám GET tak Eroor:Method not allowed
@app.route("/test")
def test():
    return render_template("test.html")
@app.route("/typ", methods=["POST"])
#tady nefunguje bez zadání typ="A", nefunguje ani když dám "A" jako druhý argument v request.form.typ()
#def typ(typ="A"):
#    return render_template("typ.html", typ=request.form.get("typ"))
def typ():
    if not request.form.get("typ"):
        return render_template("typ.html", typ="A")
    return render_template("typ.html", typ=request.form.get("typ"))

#GET a POST dohromady, zůstává jedna routa ale díky jiné metodě vrátím jiné html
@app.route("/spolu", methods=["GET", "POST"])
def spolu():
    if request.method == "GET":
        return render_template("spolu.html") # ve spolu.html musí být action=/spolu method="post"
    if not request.form.get("spolu"):
        return render_template("spolu.html") # pokud nic nezadám, zůstanu na spolu.html
    if request.method == "POST":
        return render_template("pospolu.html", pospolu=request.form.get("spolu"))

