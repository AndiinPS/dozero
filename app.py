from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    params={
        'title':'Soluções e serviços',
        'css':'home.css',
        'js':'home.js'
    }
    return render_template('home.html', params=params)

@app.route('/contatos')
def contact():
    params = {
        'title':'Faça contato',
        'css':'contacts.css',
        'js':'contacts.js'
    }
    return render_template('contact.html', params=params)

@app.route('/sobre')
def about():
    params = {
        'title': 'Sobre...', 
        'css': 'about.css',  
    }
    return render_template('about.html', params=params)
    

@app.route('/privacidade')
def policies():
    params = {
        'title': 'Políticas de Privacidade',
    }
    return render_template('policies.html', params=params)

@app.errorhandler(404)
def not_found(e):
    params = {
        'title': 'Erro 404',
        'css': '404.css',  
    }
    return render_template('404.html', params=params), 404

if __name__ == "__main__":
    app.run(debug=True)