from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            # Increase the value
            word_dictionary[word] += 1
        else:
            # ADD to the dictionary
            word_dictionary[word] = 1
        sorted_list = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    # print(fulltext)
    # The dictionary allows you to access a variable from this file in your count.html files
    # as the string that is the key in the dictionary
    return render(request, 'count.html', {'fulltext':full_text, 'count':len(word_list), 'sortedlist':sorted_list})
