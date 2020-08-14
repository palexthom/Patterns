# singleton.py

class _Singleton:
    def __init__(self):
        print("Initialisation du Singleton")
        
    def coucou(self):
        print("Coucou")
        
instance = _Singleton()