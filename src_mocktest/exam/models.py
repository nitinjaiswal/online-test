from django.db import models

# Create your models here.
class Question(models.Model):
	qid = models.IntegerField()
	qEnglish = models.CharField(max_length = 1000)
	qHindi = models.CharField(max_length = 1000)
	qOption = models.CharField(max_length = 100)
	qAnswer = models.CharField(max_length = 10)

	def __str__(self):

		return str(self.qid)


class CdpQuestion(models.Model):
	qid = models.IntegerField()
	qEnglish = models.CharField(max_length = 1000)
	qHindi = models.CharField(max_length = 1000)
	qOption = models.CharField(max_length = 100)
	qAnswer = models.CharField(max_length = 100)

	def __str__ (self):
		return str(self.qid)


class MathsQuestion(models.Model):
	qid = models.IntegerField()
	qEnglish = models.CharField(max_length = 1000)
	qHindi = models.CharField(max_length = 1000)
	qOption = models.CharField(max_length = 100)
	qAnswer = models.CharField(max_length = 100)

	def __str__ (self):
		return str(self.qid)

class EnglishQuestion(models.Model):
	qid = models.IntegerField()
	qEnglish = models.CharField(max_length = 1000)
	qOption = models.CharField(max_length = 100)
	qAnswer = models.CharField(max_length = 100)

	def __str__ (self):
		return str(self.qid)

class HindiQuestion(models.Model):
	qid = models.IntegerField()
	qHindi = models.CharField(max_length = 1000)
	qOption = models.CharField(max_length = 100)
	qAnswer = models.CharField(max_length = 100)

	def __str__ (self):
		return str(self.qid)


