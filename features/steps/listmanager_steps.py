# -- FILE: features/steps/example_steps.py
from behave import given, when, then, step

@given('que el sistema tiene al menos una lista')
def step_impl(context):
   pass

@when('el usuario pida ver una')
def step_impl(context):
    pass

@then('el sistema debe mostrarsela')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count < 1111


@given("que el usuario indico que quiere que el sistema muestre lista de actividades comunes al bootear")
def step_impl(context):
    pass

@when("el pc esta iniciado")
def step_impl(context): 
    pass

@then("el sistema debe mostrar una lista de actividades comunes")
def step_impl(context):
    pass


@given("que el usuario indico que quiere que el sistema muestre lista de actividades comunes al iniciar app")
def step_impl(context):
    pass

@when("inice la app")
def step_impl(context): 
    pass

@given("que lista x no existe")
def step_impl(context):
    pass

@when("el usuario pida ver x")
def step_impl(context): 
    pass

@then("el sistema debe avisarle que x no existe")
def step_impl(context):
    pass


@given("que lista x existe")
def step_impl(context):
    pass

@when("el usuario pida modificar una lista x")
def step_impl(context): 
    pass

@then("el sistema deberia mostrarle un entorno para modificar x")
def step_impl(context):
    pass


@given("que usuario modifico x")
def step_impl(context):
    pass


@then("el sistema deberia mostrar x tal como el usuario la dejo")
def step_impl(context):
    pass


@given("que usuario ha indicado que quiere que la app inicie cuando bootea")
def step_impl(context):
    pass

@when("el usuario inicie sesion")
def step_impl(context): 
    pass

@then("el sistema deberia estar listo para recibir peticiones")
def step_impl(context):
    pass

