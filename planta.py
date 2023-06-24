from abc import ABC

class Planta(ABC):
    cont=0
    def __init__(self, quantidade_muda: int, altura_planta: float, area_copa: float, is_grande_porte = False, tempo_adubo: str = None, plantio: bool = False ) -> None: 
       self._idplanta = __class__.gera_idplanta()
       self._quantidade_muda = quantidade_muda
       self._tempo_adubo = tempo_adubo
       self._altura_planta = altura_planta
       self._area_copa = area_copa
       self._plantio = plantio
       self._is_grande_porte = is_grande_porte

    @property
    def idplanta(self):
        return self._idplanta
    @property
    def quantidade_muda(self):
        return self._quantidade_muda
    
    @property
    def tempo_adubo(self):
        return self._tempo_adubo
    
    @property
    def altura_planta(self):
        return self._altura_planta
    
    @property
    def area_copa(self):
        return self._area_copa
    
    @property
    def plantio(self):
        return self._plantio
    
    @property
    def is_grande_porte(self):
        return self._is_grande_porte
    

    def __str__(self):
        return f'Código Planta: {self.idplanta}\n Quantidade: {self.quantidade_muda}\n Altura: {self.altura_planta} m\n Copa: {self.area_copa} m'

    @classmethod
    def gera_idplanta(cls):
        cls.cont+=1
        return str(cls.cont)