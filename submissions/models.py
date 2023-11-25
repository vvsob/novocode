from django.db import models

from django.contrib.auth.models import User
from problems.models import Problem
from compilers.models import Compiler
from django.conf import settings
import redis


redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)


class Submission(models.Model):
    token = models.CharField(max_length=36, primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='submissions')

    timestamp = models.DateTimeField(auto_now_add=True)

    source = models.FileField(upload_to='submissions/')
    compiler = models.ForeignKey(Compiler, on_delete=models.CASCADE)

    verdict = models.JSONField(null=True)

    def send_testing(self):
        self.verdict = {"format": "testing"}
        self.save()
        redis_instance.rpush("novocode:submissions", self.token)

    def delete(self, using=None, keep_parents=False):
        self.source.storage.delete(self.source.name)
        super().delete()
