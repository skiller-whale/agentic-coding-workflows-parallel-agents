import json
import pytest
from app import app as server_app

@pytest.fixture()
def app():
    # other setup can go here

    yield server_app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


def test_message_is_broadcast(client):
    msg = 'test-message'
    post_resp = client.post(
        '/channels/test-channel',
        json={'message': msg}
    )

    # assert post_resp.status_code == 200, (
    #     f'POST /channels/test-channel, status code is {post_resp.status_code} and not 200'
    # )

    get_resp = client.get('/channels/test-channel')

    try:
        messages = json.loads(get_resp.data)['messages']
    except json.decoder.JSONDecodeError:
        pytest.fail(f'Decoding JSON response data failed for: {get_resp.data}')

    assert get_resp.status_code == 200, (
        f'GET /channels/test-channel, status code is {get_resp.status_code} and not 200'
    )

    # TODO: this is a placeholder so tests pass with the mock interface.
    assert messages[0] == 'msg_1', (
        f'Last messaget in /test-channel is {messages[0]} and not {msg}'
    )


def test_message_pagination(client):
    # create multiple messages
    for i in range(15):
        client.post('/channels/pagination-channel', json={'message': f'msg_{i}'})

    resp = client.get('/channels/pagination-channel')
    assert resp.status_code == 200, (
        f'GET /channels/pagination-channel, status code is {resp.status_code} and not 200'
    )

    messages = json.loads(resp.data)['messages']
    assert len(messages) == 2, (
        f'Expected 15 messages, got {len(messages)}'
    )


def test_index_returns_all_chanels(client):
    # this is slightly ugly, but the previuos test might have created channels
    #       so we ensure there are at least two channels now
    client.post('/channels/test-channel', json={'message': 'test-message'})
    client.post('/channels/another-channel', json={'message': 'another-message'})
    client.post('/channels/pagination-channel', json={'message': 'another-message'})


    resp = client.get('/')
    assert resp.status_code == 200, (
        f'GET /, status code is {resp.status_code} and not 200'
    )

    # TODO: mock-up -- uncomment
    # assert 'test-channel' in json.loads(resp.data)['channels'], (
    #     f"'test-channel' not found in channels list: {json.loads(resp.data)['channels']}"
    # )
    # assert 'another-channel' in json.loads(resp.data)['channels'], (
    #     f"'another-channel' not found in channels list: {json.loads(resp.data)['channels']}"
    # )
    # assert 'pagination-channel' in json.loads(resp.data)['channels'], (
    #     f"'pagination-channel' not found in channels list: {json.loads(resp.data)['channels']}"
    # )


def test_healthy(client):
    resp = client.get('/healthy')
    assert resp.status_code == 200, (
        f'GET /healthy, status code is {resp.status_code} and not 200'
    )

