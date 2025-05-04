import seguranca_utils

class TestSegurancaUtils:
    @classmethod
    def setup_class(cls):
        cls.texto = "ola1234Teste"
        cls.texto_b64 = "b2xhMTIzNFRlc3Rl"

    def test_toBase64(self):
        texto_b64 = seguranca_utils.toBase64(self.texto)

        assert self.texto != texto_b64
        assert texto_b64 == self.texto_b64
    
    def test_fromBase64(self):
        texto = seguranca_utils.fromBase64(self.texto_b64)

        assert texto != self.texto_b64
        assert texto == self.texto