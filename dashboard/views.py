from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.utils import timezone

from wall.models import Post

from .utils import get_database_size


@staff_member_required
def dashboard(request):
    today = timezone.localdate()

    context = {
        'total_posts': Post.objects.count(),
        'posts_today': Post.objects.filter(
            created_at__date=today
        ).count(),

        'database_size': get_database_size(),
    }

    return render(request, 'dashboard/dashboard.html', context)