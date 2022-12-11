from flask import Flask,render_template
import pyodbc
app = Flask(__name__)

@app.route('/')
def index():
    #return "<h1>hola Compañeres, saludos de</h1>"
    return render_template('index.html', data = dic_data)

@app.route('/contacto/<nombre>', defaults={'numero': None} )
@app.route('/contacto/<nombre>/<numero>')
def contacto(nombre,numero):
    data={
        'titulo':'contacto',
        'nombre':nombre,
        'numero':numero
    }
    return render_template('contacto.html',data=data)


lista_cursos=['fundamentos de programacion', 
'programacion orientada a objetos', 
'Desarollo de software',
'ingles I',
'inglesII',
'ingles III',
'habilidades personales',
'habilidades personales II',
'habilidades personales III',
]

dic_data = {'titulo':'index',
'bienvenida':'Hola! desde html',
'etiqueta_2':'mi nombre es many',
'cursos':lista_cursos,
'cant_cursos':len(lista_cursos)
}#esto es un diccionario


def pagina_no_encontrada(error):
    return render_template('404.html'), 404

@app.route('/consulta')
def consulta():
    connection=pyodbc.connect('DRIVER={SQL Server};SERVER=MANY\SQLEXPRESS;DATABASE=Spanish;UID=Many\Manuel;Trusted_Connection=yes;')
    print ('conexion exitosa',connection)
    cursor=connection.cursor()
    cursor.execute("select p.ProductName, p.ColorName, p.UnitPrice, p.Size, s.ProductSubcategoryName from DimProduct p, DimProductSubcategory s where s.ProductSubcategoryKey=p.ProductSubcategoryKey and s.ProductSubcategoryName = 'Lápiz de grabación'")
    lista=cursor.fetchall()
    return render_template('consulta.html',data = lista)

@app.route('/pqr')
def pqr(): 
    return render_template('pqr.html')

if __name__ == '__main__' :
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port =5000)

