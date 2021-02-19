from django.db import models
from django.contrib.auth.models import User

class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True)
    fromuser = models.ForeignKey(User, null=True, blank=True, related_name="activitylogs_withfromuser")
    jsondata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s / %s / %s' % (
            self.type,
            self.logged_user,
            self.created_at,
        )


class Todo(models.Model):
    description = models.CharField(max_length=512)
    done = models.BooleanField(default=False)

    def to_dict_json(self):
        return {
            'id': self.id,
            'description': self.description,
            'done': self.done,
        }

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
class Animais(models.Model):
    nomepessoal=models.CharField(max_length=32, blank=True, null=True)
    telefone=models.CharField(max_length=11, null=True)
    nomeanimal=models.CharField(max_length=32)
    raça=models.CharField(max_length=32)
    costumes=models.CharField(max_length=122)
    alimentação=models.CharField(max_length=122)
    gosta=models.CharField(max_length=122)
    idade=models.IntegerField(default=1)
    image=models.ImageField(upload_to="animais", blank=True, null=True)
    #pet=models.OneToOneField(animais, null=True, on_delete=models.SET_NULL) # 1 pra 1, integridade referencial no banco de dados.
    #user=models.OneToOneField(User, on_delete=models.CASCADE)

    def to_dict_json(self):
        return {
            'nomepessoal':self.nomepessoal,
            'telefone':self.telefone,
            'nomeanimal':self.nomeanimal,
            'raça':self.raça,
            'costumes':self.costumes,
            'alimentação':self.alimentação,
            'gosta':self.gosta,
            'idade':self.idade,
            'image':self.image.url
            }


