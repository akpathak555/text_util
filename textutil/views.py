from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    # get the text
    text = request.POST.get('area','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcounter=request.POST.get('charcounter','off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'",\<>./?@#$%^&*_~'''
        analyzed=""    
        for char in text:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations:','analyzed_text':analyzed}
        text=analyzed
        # analyze the text
        #return render(request,'analyze.html',params)
    if fullcaps == "on":
        analyzed=""
        for char in text:
            analyzed=analyzed+char.upper()
            
            params={'purpose':'Capitalize Punctuations:','analyzed_text':analyzed}
        text=analyzed
        # analyze the text
        #return render(request,'analyze.html',params)
    if newlineremover == "on":
        analyzed=""
        for char in text:
            if char !="\n" and char !="\r":
                analyzed=analyzed +char
            
            params={'purpose':'Remove New Line:','analyzed_text':analyzed}
        text=analyzed
        # analyze the text
        #return render(request,'analyze.html',params)
    if(extraspaceremover == "on"):
        analyzed=""
        for index,char in enumerate(text):
            if not(text[index]==" " and text[index+1]==" "):
                analyzed = analyzed + char
            
        params={'purpose':'Remove Extra Space:','analyzed_text':analyzed}
        text=analyzed
        # analyze the text
        #return render(request,'analyze.html',params)
   # this function is worked as one time a single function !!!
    if charcounter == "on":
        analyzed=len(text)    
        params={'purpose':'Total Length Of String Is:','analyzed_text':analyzed}
        # analyze the text
        #return render(request,'analyze.html',params)
    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on" and charcounter!="on"):
        return HttpResponse("<center><h1>HTTP 404 Not Found Error:</h1>You are not selected any area !!<br/>Please select any field..</center>")
    return render(request,'analyze.html',params)