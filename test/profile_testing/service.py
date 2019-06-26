from space_api import API

api = API('books-app', '192.168.43.226:8081')

service = api.service('service')


def echo_func(params, auth, cb):
    cb('response', params)


# def func2(params, auth, cb):
#     cb('response', 'my_response')


service.register_func('echo_func', echo_func)
# service.register_func('func2', func2)

service.start()
api.close()
