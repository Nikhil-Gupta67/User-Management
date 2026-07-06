import os
import tempfile

import pytest

from app import create_app, db, User


@pytest.fixture()
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': f'sqlite:///{db_path}',
        'SECRET_KEY': 'test-secret-key',
    })

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

    with app.app_context():
        db.session.remove()
        db.drop_all()
        db.engine.dispose()

    os.close(db_fd)
    os.unlink(db_path)


def test_add_user_and_delete_user(client):
    response = client.post('/add', data={
        'name': 'Alice',
        'email': 'alice@example.com',
        'age': '30',
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'User added successfully!' in response.data

    with client.application.app_context():
        user = User.query.filter_by(email='alice@example.com').first()
        assert user is not None

    delete_response = client.post(f'/delete/{user.id}', follow_redirects=True)
    assert delete_response.status_code == 200
    assert b'User removed successfully!' in delete_response.data

    with client.application.app_context():
        assert User.query.count() == 0
