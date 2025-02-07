from bottle import route, run, static_file

@route("/hello")
def hello():
    return "Hello,World"

@route("/")
def html():
    return static_file(filename = "index.html", root=".")

@route("/echo/<thing>")
def echo(thing):
    return "Say hello to my little friend ： %s " % thing

if __name__ == "__main__":
    run(host="127.0.0.1", port="8090")