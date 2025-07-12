import os
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    name = os.environ.get('NAME')
    if name is None or len(name) == 0: # Use 'is None' para verificar NoneType
        name = "world"
    message = "Hello, " + name + "!\n"
    message += "This is a Pyramid application running on port " + str(os.environ.get("PORT", 8080)) + ".\n"
    message += "You can set the NAME environment variable to change the greeting.\n"
    return Response(message)

if __name__ == '__main__':
    # Tenta obter a porta da variável de ambiente, senão usa 8080 como padrão
    port = int(os.environ.get("PORT", 8080))
    # Note: também é boa prática usar 'is None' em vez de '== None'
    # para verificar explicitamente se é NoneType.
    
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()