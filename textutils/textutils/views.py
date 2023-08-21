# This file is made by Dhruv Sanghvi
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse("Hello")
def index(request):
    params={'name':'Dhruv','place':'Indore'}
    return render(request,'index.html',params)
def removepunc(request):
      
    return HttpResponse("Removepunc")
def capfirst(request):
    return HttpResponse("capfirst")
def newlineremove(request):
    return HttpResponse("line remover")
def spaceremove(request):
    return HttpResponse("Space Removed first")
def charcount(request):
    return HttpResponse("char count")
def analyze(request):
    

     djtext=(request.POST.get('text','default'))
     charcount=request.POST.get('charcount','off')
     newlineremover=request.POST.get('newlineremover',"off")
     removepunc =request.POST.get('removepunc','off')
     fullcaps=request.POST.get('fullcaps','off')
     extraspaceremover=request.POST.get('extraspaceremover','off')
     if removepunc=="on":
      punctuations='''!()-[]{};:'"\,<>./?@#$%^&_*~ '''
      analyzed=""
      for char in djtext:
          if char not in punctuations:
              analyzed=analyzed+char;
     
      params={'purpose':'Removed  Puncutations','analyzed_text':analyzed}
    
      return render(request,'analyze.html',params)
      
     elif (fullcaps=="on"): 
          analyzed=""
          for char in djtext:
              analyzed=analyzed+char.upper()
          params={'purpose':'Changed to Uppercase','analyzed_text':analyzed}
          return render(request,'analyze.html',params)
     elif(newlineremover=="on"):
         analyzed=""
         for char in djtext:
             if char!="\n":
                 analyzed=analyzed+char


      
         params={'purpose':'Removed New Lines','analyzed_text':analyzed}
         return render(request,'analyze.html',params)
     elif(extraspaceremover=="on"):
          analyzed=""
          for index,char in enumerate(djtext):
              if djtext[index]==" " and djtext[index+1]==" ":
                  pass;
              else:
                  analyzed=analyzed +char
          params={'purpose':'Removed Extra Spaces','analyzed_text':analyzed}
          return render(request,'analyze.html',params)
     elif(charcount=="on"):
         
          
      params={'purpose':"Calculated the no of characters",'analyzed_text':len(djtext)}
     return render(request,'analyze.html',params)
