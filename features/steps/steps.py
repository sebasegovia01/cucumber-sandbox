from behave import given, when, then


@given("I am in chrome browser")
def background_given(context):
    pass


@given("I have account")
def step_given(context):
    pass


@when("Sign in")
def step_sign_in(context):
    pass


@then("Show welcome message")
def step_show_welcome_message(context):
    print("hello")
    pass


@given("I am in sign up view")
def step_given(context):
    pass


@when("Complete sign up form with {name} and {lastname}")
def step_when(context, name, lastname):
    context.name = name
    context.lastname = lastname
    pass


@when("I click sign up button")
def step_when(context):
    pass


@when("push enter")
def step_when(context):
    pass


@then("Redirect to home view and show welcome message")
def step_then(context):
    print("Hello")
    pass


@then("First need confirm email")
def step_then(context):
    pass
