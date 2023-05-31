from flask import Flask, render_template

app = Flask(__name__)

# Ruta de inicio
@app.route('/')
def principal():
    cards = [{'title':'Mansión','description':'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae sint voluptate exercitationem voluptas culpa eaque ipsam?'},
             {'title':'Mansión','description':'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae sint voluptate exercitationem voluptas culpa eaque ipsam?'},
             {'title':'Mansión','description':'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae sint voluptate exercitationem voluptas culpa eaque ipsam?'},
             {'title':'Mansión','description':'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae sint voluptate exercitationem voluptas culpa eaque ipsam?'},
             {'title':'Mansión','description':'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae sint voluptate exercitationem voluptas culpa eaque ipsam?'},
             {'title':'Mansión','description':'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae sint voluptate exercitationem voluptas culpa eaque ipsam?'},
             {'title':'Mansión','description':'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae sint voluptate exercitationem voluptas culpa eaque ipsam?'},
             {'title':'Mansión','description':'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae sint voluptate exercitationem voluptas culpa eaque ipsam?'}
             ]
    return render_template('index.html', cards=cards)

if __name__ == '__main__':
    app.run(debug=True)