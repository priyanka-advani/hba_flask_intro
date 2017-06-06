"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.errorhandler(404)
def page_not_found(e):
  """Home page."""

  return """<!doctype html>
              <html>
                <head>
                  <title>404 404 404</title>
                </head>
                <body>
                  <h1>This page is not here. Sorry.</h1>
                  <a href="/hello">Go to HELLO!</a>
                <body>
              </html>"""


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
                <html>
                  <head>
                    <title>Homepage Homepage Homepage</title>
                  </head>
                  <body>
                    <h1>Hi! This is the home page.</h1>
                    <a href="/hello">Go to HELLO!</a>
                  <body>
                </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <p>
        <form action="/greet">
          What's your name?<br>
          <input type="text" name="person"><br>
          Select a compliment:<br>
          <select name="compliment">
            <option value="awesome">Awesome</option>
            <option value="cool">Cool</option>
            <option value="awesomely-cool">Awesomely Cool</option>
          </select><br>
          <input type="submit" value="Submit">
        </form>
        </p>

        <p>
        <form action="/diss">
          Enter your name, even though I don't care: <br>
          <input type="text" name="person"><br>
          What should I say about you?<br>
          <select name="insult">
            <option value="not-so-cool">Not so cool</option>
            <option value="not-at-all-awesome">Not at all awesome</option>
            <option value="less-likely-cool">Less likely cool</option>
            <option value="not-very-smart">Not very smart</option>
          </select><br>
          <input type="submit">
        </form>
        </p>
      </body>
    </html>
    """


@app.route('/diss')
def ungreet_person():
    """Get user by name."""

    player = request.args.get("person")

    insult = request.args.get("insult")

    return """
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}!
      </body>
    </html>
    """.format(player=player, insult=" ".join(insult.split("-")))


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=" ".join(compliment.split("-")))


# @app.route('/form', methods=['GET'])
# def view():
#   return # html for form

# @app.route('/form', methods=['POST'])
# def view2()

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
