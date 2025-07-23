from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        total_sin_descuento = cantidad * 9000

        if edad < 18:
            descuento = 0
        elif 18 <= edad <= 30:
            descuento = 0.15
        else:
            descuento = 0.25

        total_con_descuento = total_sin_descuento * (1 - descuento)

        return render_template('resultado.html', nombre=nombre, total=total_sin_descuento, total_desc=total_con_descuento)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = ''
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']

        if usuario == 'juan' and password == 'admin':
            mensaje = 'Bienvenido administrador juan'
        elif usuario == 'pepe' and password == 'user':
            mensaje = 'Bienvenido usuario pepe'
        else:
            mensaje = 'Usuario o contraseña incorrecta'

        return render_template('resultado.html', mensaje=mensaje)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
