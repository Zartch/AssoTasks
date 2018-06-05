from django.db import models



class EventTypo(models.Model):

    nombre = models.CharField(max_length=250)
    desc = models.CharField(max_length=250)

    def __str__(self):
        return "ET:" + self.nombre



class TaskaTypo(models.Model):

    nombre = models.CharField(max_length=250)
    desc = models.TextField()
    diasLimite = models.IntegerField(default = 0)
    diasAvisar = models.IntegerField(default = 0)
    eventoTypo = models.ForeignKey(EventTypo,  on_delete=models.DO_NOTHING)


    def __str__(self):
        return "TT:" + self.nombre




