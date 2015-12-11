from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Question
import math
import random
import json as simplejson




# Create your views here.
ar1=[1,2,3,4,5,6,7,8,9,10];
ar2=[1,2,3,4,5,6,7,8,9,10];
ar3=[1,2,3,4,5,6,7,8,9,10];
ar4=[1,2,3,4,5,6,7,8,9,10];
ar5=[1,2,3,4,5,6,7,8,9,10];

def shuffleArray(array):
	i=9
	while i > 0:
		j = math.floor(random.random() * (i+1))
		tmp = array[i]
		array[i] = array[j]
		array[j] = tmp
		i = i-1
	return array

ar1 = shuffleArray(ar1)
ar2 = shuffleArray(ar2)
ar3 = shuffleArray(ar3)
ar4 = shuffleArray(ar4)
ar5 = shuffleArray(ar5)

    
def home(request):

	queryset = Question.objects.all()
	queryset1 = Question.objects.values('qid','qEnglish')

	# for instance in queryset:
	# 	if instance.qid == 1:
	# 		a = instance.qOption.split('~')
	qEnglish_array = []
	qHindi_array = []
	qOption_array = []
	qAnswer_array = []

	for i in ar1:
		for instance in queryset:
			if instance.qid == i:
				qEnglish_array.append(instance.qEnglish)
				qHindi_array.append(instance.qHindi)
				qOption_array.append(instance.qOption.split('~'))
				qAnswer_array.append(instance.qAnswer)



	
	context = {
	'queryset':queryset,
	'queryset1':queryset1,
	'qEnglish_array':qEnglish_array,
	'qOption_array':qOption_array,
	'qAnswer_array':qAnswer_array,
	#'a':a,
	'jsqueryset':simplejson.dumps(list(queryset1)),
	'ar1':ar1,
	}


	return render(request, "test.html", context)
	# return render_to_response('hom1.html',context)

# def result(request):
# 	return render(request, "result.html", {})

	 