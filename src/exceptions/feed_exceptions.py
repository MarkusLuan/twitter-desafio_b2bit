class FeedNotFoundException (Exception):
    def __init__(self):
        super().__init__("Postagem não encontrada!")