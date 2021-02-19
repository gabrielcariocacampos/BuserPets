# coding: utf-8
import json
from django.http.response import HttpResponse, JsonResponse
from django.contrib import auth
from commons.django_model_utils import get_or_none
from commons.django_views_utils import ajax_login_required
from core.service import log_svc, todo_svc, animais_svc
from django.views.decorators.csrf import csrf_exempt


def dapau(request):
    raise Exception('break on purpose')


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)


def logout(request):
    if request.method.lower() != 'post':
        raise Exception('Logout only via post')
    if request.user.is_authenticated():
        log_svc.log_logout(request.user)
    auth.logout(request)
    return HttpResponse('{}', content_type='application/json')


def whoami(request):
    i_am = {
        'user': _user2dict(request.user),
        'authenticated': True,
    } if request.user.is_authenticated() else {'authenticated': False}
    return JsonResponse(i_am)


@ajax_login_required
def add_todo(request):
    todo = todo_svc.add_todo(request.POST['new_task'])
    return JsonResponse(todo)


@ajax_login_required
def list_todos(request):
    todos = todo_svc.list_todos()
    return JsonResponse({'todos': todos})


def _user2dict(user):
    d = {
        'id': user.id,
        'name': user.get_full_name(),
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'permissions': {
            'ADMIN': user.is_superuser,
            'STAFF': user.is_staff,
        }
    }
    return d

def cadastro(request):
    nomepessoal=request.POST['nomepessoal']
    telefone=request.POST['telefone']
    nomeanimal=request.POST['nomeanimal'] 
    raça=request.POST['raça']
    costumes=request.POST['costumes']
    alimentação=request.POST['alimentação']
    gosta=request.POST['gosta']
    idade=request.POST['idade']
    image=request.FILES['image']
    animais = animais_svc.cadastro(nomepessoal=nomepessoal, telefone=telefone, nomeanimal=nomeanimal, raça=raça, costumes=costumes, alimentação=alimentação, gosta=gosta, idade=idade, image=image)
    return JsonResponse(animais, safe=False)

#def cadastropessoal(request):
 #   request.user
    # cidade=request.POST['cidade']
    # endereço=request.POST['endereço']
    # casa=request.POST['casa']
    # filhos=request.POST['filhos']
    # horas=request.POST['horas']
    # idade1=request.POST['idade1']
    # # username=request.POST['username']
    # # password=request.POST['password']
    # # email=request.POST['email']
    # pessoas = pessoas_svc.cadastropessoal(nome=nome, cidade=cidade, endereço=endereço,
    #                                       casa=casa, filhos=filhos, horas=horas,
    #                                       idade1=idade1,
    #                                       # username=username, password=password, email=email
    #                                       user=request.user
    #                                       )
    # return JsonResponse(pessoas, safe=False)

def listaranimais(request):
    animais=list(animais_svc.listaranimais())
    info=[]
    for a in animais:
        info.append(a.to_dict_json())
    return JsonResponse(info, safe = False)