# Create your views here.
from django.shortcuts import render_to_response,RequestContext
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from commitinfo.models import Kernel_Project,Libvirt_Project,OpenStack_Project
from datetime import datetime
from django.db.models import Count

def show_table(year,project,tablename,request):
    ini_year=2011
    choices=[]
    if year=='all time':
#	  lines=Kernel_Project.objects.filter(datetime__range=(datetime(ini_year,1,1),datetime.now())).values('name','email').annotate(commit_count=Count('name'))
	  lines=project.objects.filter(datetime__range=(datetime(ini_year,1,1),datetime.now())).values('name','datetime','comment','hashvalue').order_by('-datetime')
	  choices.append(year)
	  for i in range(datetime.now().year,ini_year-1,-1):
	     choices.append(i)
    else:
	  lines=project.objects.filter(datetime__range=(datetime(int(year),1,1),datetime(int(year),12,31))).values('name','datetime','comment','hashvalue').order_by('-datetime')
	  choices.append(year)
	  for i in range(datetime.now().year,ini_year-1,-1):
	     if i!=int(year):
	        choices.append(i)
          choices.append('all time')

    total=lines.count()

    paginator = Paginator(lines, 100)
    page = request.GET.get('page')
    try:
        show_lines = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        show_lines = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        show_lines = paginator.page(paginator.num_pages)
    return RequestContext(request, {'lines':show_lines,'tabletitle':tablename,'choices':choices,'total':total,})

def index(request):
    tablename='Statistics of Kernel Project'
    if 'year' in request.GET:
	year=request.GET.get('year')
	request.session['kernel_year']=year
    else:
	if 'kernel_year' in request.session:
	    year=request.session['kernel_year']
	else:
	    year='all time'
    
    return render_to_response('info_table.html',show_table(year,Kernel_Project,tablename,request))


def libvirt_page(request):
    tablename='Statistics of Libvirt Project'
    if 'year' in request.GET:
	year=request.GET.get('year')
	request.session['libvirt_year']=year
    else:
	if 'libvirt_year' in request.session:
	    year=request.session['libvirt_year']
	else:
	    year='all time'
    
    return render_to_response('info_table.html',show_table(year,Libvirt_Project,tablename,request))

def openstack_page(request):
    tablename='Statistics of OpenStack Project'
    if 'year' in request.GET:
	year=request.GET.get('year')
	request.session['openstack_year']=year
    else:
	if 'openstack_year' in request.session:
	    year=request.session['openstack_year']
	else:
	    year='all time'
    
    return render_to_response('info_table.html',show_table(year,OpenStack_Project,tablename,request))

