from core.models import Animais

def cadastroanimais(nomeanimal, raça, costumes, alimentação, gosta, idade):
    animais=Animais.objects.create(nomeanimal=nomeanimal, raça=raça, costumes=costumes, alimentação=alimentação, gosta=gosta, idade=idade)
    return animais.to_dict_json()