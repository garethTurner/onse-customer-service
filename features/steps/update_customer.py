from behave import when, then


@when('I update customer with id "{customer_id:d}" surname to "{name}"')
def update_customer2(context, customer_id, name):
    (first_name, surname) = name.split(' ', 2)
    response = context.web_client.put(
        '/customers/' + str(customer_id),
        json={'customerId': str(customer_id),
              'firstName': first_name,
              'surname': surname})

    assert response.status_code == 200, response.status_code
    context.customer_id = response.get_json()['customerId']


@then('customer with id "{customer_id:d}" has surname "{name}"')
def check_customer(context, customer_id, name):
    context.response = context.web_client.get(f'/customers/{customer_id}')
    response = context.response
    body = response.get_json()
    assert f"{body['surname']}" == name, f"found: {body['surname']}"
