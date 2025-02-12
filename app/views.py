
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView
from .utils import fetch_adzuna_jobs

def home(request):
    return render(request,'index.html')
def teams(request):
    return render(request,'teams.html')
def team(request):
    return render(request,'team.html')
def eve(request):
    return render(request,'eve.html')





class JobListView(TemplateView):
    template_name = 'jobs.html'

class JobAPIView(APIView):
    def get(self, request):
        jobs_data = fetch_adzuna_jobs()
        
        if not jobs_data or 'results' not in jobs_data:
            return Response([])
        
        formatted_jobs = []
        for job in jobs_data['results']:
            formatted_job = {
                'id': job['id'],
                'title': job['title'],
                'company': job['company']['display_name'],
                'location': job['location']['display_name'],
                'description': job['description'],
                'salary': job.get('salary_min', 'Not specified'),
                'url': job['redirect_url'],
                'posted_date': job['created']
            }
            formatted_jobs.append(formatted_job)
        
        return Response(formatted_jobs)