from django.shortcuts import render
from ResumeUploaderapp.forms import ResumeForm
from ResumeUploaderapp.models import Resume
from django.views import View

class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, 'home.html', {'form': form, 'candidates': candidates})

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {'form': form})

class CandidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'candidate.html', {'candidate': candidate})
