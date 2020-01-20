from django.db import models
from datetime import date
import PyPDF2 as pdf2
import os
from django.shortcuts import render, redirect, get_object_or_404

# Create your models here.
class Document(models.Model):
    pdf = models.FileField(upload_to="pdfs/files", blank=True, null=True)
    name = models.CharField(max_length=120, default='document ')
    size = models.IntegerField(default= 0)
    page_number = models.IntegerField(default= 0)
    date = models.DateField("date", default=date.today)

    class Meta():
        ordering = ["-id"]
'''
    def __str__(self):
        return self.name'''

class Page(models.Model):
    id_document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='pages')
    text = models.TextField(default= ' ')
    nr = models.IntegerField(default= 0)
    thumbnail = models.ImageField(upload_to="pdfs/thumbnails", blank=True, null=True)

    class Meta():
        ordering = ["nr"]
'''
    def __str__(self):
        return self.id_document.name + ' ' + str(self.nr)'''