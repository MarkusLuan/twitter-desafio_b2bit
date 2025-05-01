from flask import Flask, request
from flask import make_response
from werkzeug.exceptions import HTTPException

from exceptions import user_exceptions

class ErrorHandler:
    def __init__(self, app: Flask):
        def __reportar_erro(erro: str, status_code: int):
            print(erro)

            res = make_response({
                "erro": True,
                "texto": str(erro)
            }, status_code)

            res.headers["Content-Type"] = "application/json"
            return res
        
        @app.errorhandler(401)
        def nao_autorizado(e):
            return __reportar_erro("Não autorizado!", 401)
            
        @app.errorhandler(405)
        def methodo_nao_permitido(e):
            return __reportar_erro(f"O metodo {request.method} não é permitido para este recurso!", 405)
            
        @app.errorhandler(404)
        def nao_encontrato(e):
            return __reportar_erro("Recurso não encontrado!", 404)
        
        @app.errorhandler(HTTPException)
        def erro_http(e: HTTPException):
            return __reportar_erro(e.description or "", e.code)
        
        @app.errorhandler(user_exceptions.InvalidLoginException)
        def erro_login_invalido(e: user_exceptions.InvalidLoginException):
            return __reportar_erro(str(e), 401)

        @app.errorhandler(Exception)
        def erro_tratado(e: Exception):
            return __reportar_erro(str(e), 500)