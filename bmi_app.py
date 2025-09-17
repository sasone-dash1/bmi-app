from dash import Dash, html, dcc, Output, Input
import math, webbrowser
app = Dash(__name__)
app.layout = html.Div([
    html.H1("BMI計算アプリ"),
    html.Label("身長(cm)"),
    dcc.Input(id='height', type='text', value='170.0'),
    html.Br(),
    html.Label("体重(kg)"),
    dcc.Input(id='weight', type='text', value='50.0'),
    html.Br(),
    html.Div(id='bmi-output'),
    html.Div(id='result-output'),
    html.Div(id='bsa-output'),
    html.Div(id='warning-output', style={'color': 'red'})
])
@app.callback(
    Output('bmi-output', 'children'),
    Output('result-output', 'children'),
    Output('bsa-output', 'children'),
    Output('warning-output', 'children'),
    Input('height', 'value'),
    Input('weight', 'value')
)
def update_bmi(height, weight):
    try:
        hei = float(height)
        wei = float(weight)
        bmi = wei / ((hei / 100) ** 2)
        bmi_rounded = round(bmi + 1e-8, 1)
        bsa = (wei**0.425)*(hei**0.725)*0.007184
        bmi_text = f"BMI (kg/m2) = {bmi_rounded}"
        if bmi_rounded < 18.5:
            result = "痩せ型です。"
        elif bmi_rounded >= 25:
            result = "肥満気味です。"
        else:
            result = "普通体重です。"
        bsa_text = f"体表面積 (BSA) (m2) = {round(bsa, 2)}"
        return bmi_text, result, bsa_text, ""
    except ValueError:
        return "", "", "", "数値を正しく入力してください。"
if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:8050/")
    app.run(debug=True)

