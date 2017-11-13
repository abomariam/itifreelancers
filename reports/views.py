# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.shortcuts import render
from freelancers.models import Freelancer, Job, Profile
from django.db.models import Count, When, Case, Sum

# Create your views here.


def simple_stats(request, *args, **kwargs):

    context = {}

    context['total_freelancers'] = Freelancer.objects.count()
    context['active_freelancers'] = Freelancer.objects.annotate(Count('profiles__jobs'))\
        .filter(profiles__jobs__count__gt=0).count()
    context['working_freelancers'] = Freelancer.objects.annotate(
        jobs_count=Case(
            When(profiles__jobs__is_hired=True, then=Count('profiles__jobs'))
        )).filter(jobs_count__gt=0).count()

    context['total_jobs'] = Job.objects.count()
    context['interviews_jobs'] = Job.objects.filter(is_interviewed=True).count()
    context['hired_jobs'] = Job.objects.filter(is_hired=True).count()
    context['completed_jobs'] = Job.objects.filter(is_completed_successfully=True).count()
    context['disputed_jobs'] = Job.objects.filter(is_disputed=True).count()

    context['top_active_freelancers'] = Freelancer.objects.annotate(Count('profiles__jobs')) \
        .filter(profiles__jobs__count__gt=0)\
        .order_by('-profiles__jobs__count')[0:10]

    context['top_working_freelancers'] = Freelancer.objects.annotate(
        jobs_count=Case(
            When(profiles__jobs__is_hired=True, then=Count('profiles__jobs'))
        )).order_by('-jobs_count').filter(jobs_count__gt=0)

    context['top_working_freelancers_by_income'] = Freelancer.objects.annotate(
        income=Case(
            When(profiles__jobs__total_job_income__gt=0, then=Sum('profiles__jobs__total_job_income')), default=0
        )).filter(income__gt=0).order_by('-income')[0:10]

    context.update({
        'has_permission': True,
        'site_header': admin.site.site_header,
        'site_title': admin.site.site_title,
        'site_url': admin.site.site_url,
        'title': 'Freelancers Stats',
    })

    return render(request, 'reports/simple-stats.html', context)
