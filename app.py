from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        precio_por_tarro = 9000
        total_sin_descuento = cantidad * precio_por_tarro

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        descuento_dinero = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - descuento_dinero
        resultado = {
            'nombre': nombre,
            'total_sin_descuento': total_sin_descuento,
            'total_con_descuento': total_con_descuento,
            'descuento_dinero': descuento_dinero
        }
    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    usuarios = {
        'juan': 'admin',
        'pepe': 'user'
    }
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        if usuario in usuarios and usuarios[usuario] == contraseña:
            if usuario == 'juan':
                mensaje = f'Bienvenido administrador {usuario}'
            else:
                mensaje = f'Bienvenido usuario {usuario}'
        else:
            mensaje = 'Usuario o contraseña incorrectos'
        resultado = mensaje
    return render_template('ejercicio2.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
