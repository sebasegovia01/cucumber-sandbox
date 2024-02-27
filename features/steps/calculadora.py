from behave import given, when, then


@given('ingreso el primer digito "{num1}"')
def step_ingreso_primer_digito(context, num1):
    context.num1 = int(num1)

@given('ingreso el segundo digito "{num2}"')
def step_ingreso_segundo_digito(context, num2):
    context.num2 = int(num2)

@when('presiono el boton suma')
def step_presiono_boton_suma(context):
    context.resultado = context.num1+context.num2

@then('El resultado deberia ser "{result}"')
def step_ingreso_segundo_digito(context, result):
    assert context.resultado == int(result)