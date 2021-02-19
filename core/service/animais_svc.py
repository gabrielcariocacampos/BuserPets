from core.models import Animais

def cadastro(nomepessoal, telefone, nomeanimal, raça, costumes, alimentação, gosta, idade, image):
    animais=Animais.objects.create(nomepessoal=nomepessoal, telefone=telefone, nomeanimal=nomeanimal, raça=raça, costumes=costumes, alimentação=alimentação, gosta=gosta, idade=idade, image=image)
    return animais.to_dict_json()

def listaranimais():
    animais=Animais.objects.all()
    return animais  