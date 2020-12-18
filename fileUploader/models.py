from django.contrib import admin
from django.db import models
from django.core.files.storage import FileSystemStorage


class TrafficDataFile(models.Model):
    FILE_UNPROCESSED = -1
    SAVE_PATH = '/home/thomas/PycharmProjects/trafficAnalysis/UPLOADED_FILES'
    file_storage = FileSystemStorage(location=SAVE_PATH)
    file = models.FileField(storage=file_storage)
    sourceFileName = models.CharField(max_length=30)
    sourceFileRows = models.IntegerField(default=FILE_UNPROCESSED)
    sourceFileSize = models.FloatField()
    isProcessed = models.BooleanField(default=False)

admin.site.register(TrafficDataFile)

class TrafficDataColumnNames(models.Model):
    columnName = models.CharField(max_length=30)
    trafficDataFile = models.ForeignKey(TrafficDataFile, on_delete=models.CASCADE)


class TrafficDataRow(models.Model):
    trafficDataFile = models.ForeignKey(TrafficDataFile, on_delete=models.CASCADE)
    rowNumber = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    weighted = models.FloatField()

