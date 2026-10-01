from flask import Flask, request, render_template

app = Flask(__name__)


def calculate_volume(figure, param):
    try:
        value = float(param)
        if value < 0:
            return None, "Ошибка: значение не может быть отрицательным"

        if figure == 'cube':
            return value ** 3, None
        elif figure == 'sphere':
            return (4 / 3) * 3.14159 * (value ** 3), None
        elif figure == 'cylinder':
            return 3.14159 * (value ** 2) * value, None
        else:
            return None, "Ошибка: неизвестная фигура"
    except ValueError:
        return None, "Ошибка: введите корректное число"


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    figure = 'cube'
    param = ''

    if request.method == 'POST':
        figure = request.form.get('figure', 'cube')
        param = request.form.get('param', '')

        volume, err = calculate_volume(figure, param)
        if err:
            error = err
        else:
            result = f"{volume:.2f}"

    return render_template('index.html', result=result, error=error, figure=figure, param=param)


if __name__ == '__main__':
    app.run(debug=True)