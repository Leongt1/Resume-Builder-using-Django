from django.shortcuts import render, redirect
from .models import Profile
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io

# Create your views here.
def mainpg(request):
    if request.method=='POST':
        name = request.POST.get("name")
        phone = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        insta = request.POST.get("insta")
        github = request.POST.get("github")
        linkedin = request.POST.get("linkedin")
        careerObj = request.POST.get("co")
        workexp = request.POST.get("workexp")
        project = request.POST.get("project")
        skill = request.POST.get("skill")
        aq = request.POST.get("aq")

        profile = Profile(
        # user = User.objects.create_user(
            name = name,
            phone = phone,
            email = email,
            address = address,
            insta = insta,
            github = github,
            linkedin = linkedin, 
            careerObj = careerObj,
            workexp = workexp,
            project = project,
            skill = skill,
            aq =aq
        )

        profile.save()
        print("Resume details added")

        # if name=="":
        #     return HttpResponse("alert(Name cannot ")
    return render(request, "resume_template.html")

def resumehtml(request, id):
    user_profile = Profile.objects.get(pk=id)
    return render(request, 'template.html', {'user_profile':user_profile})
    
# def reumepdf(request, id):
#     user_profilepdf = Profile.objects.get(pk=id)
#     template = loader.get_template("/resume_pdf.html")
#     html = template.render({'user_profile':user_profilepdf})
#     options = {
#         'page-size':'Letter',
#         'encoding':'UTF-8',
#     }
#     pdf =pdfkit.from_string(html, False, options)
#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition']='attachment'
#     filename = "resume.pdf"
#     return response

def list(request):
    profile = Profile.objects.all()
    return render(request, "list.html", {'profile':profile})

# def template(request, id):
#     profile = Profile.objects.get(pk=id)
#     return render(request, "template.html", {"profile":profile})