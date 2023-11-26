from django.db import models


class Compiler(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    compile_command = models.CharField(max_length=1024, blank=True, null=True)
    run_command = models.CharField(max_length=1024)
    file_extension = models.CharField(max_length=16)

    def __str__(self):
        return self.name
