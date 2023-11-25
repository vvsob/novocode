from django.db import models


class Problem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    statement = models.JSONField(default=dict)

    problem_xml = models.FileField(upload_to='problems/')
    problem_archive = models.FileField(upload_to='problems/')

    def __str__(self):
        return f"{self.id}. {self.name}"

    def delete(self, using=None, keep_parents=False):
        self.problem_xml.storage.delete(self.problem_xml.name)
        self.problem_archive.storage.delete(self.problem_archive.name)
        super().delete()
