from django.conf import settings
from django.shortcuts import render


class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # اگر MAINTENANCE_MODE فعال باشد
        if settings.MAINTENANCE_MODE:
            # چک کردن اینکه اگر درخواست از پنل ادمین نباشد
            if settings.MAINTENANCE_MODE_IGNORE_ADMIN_SITE and request.path.startswith('/admin/'):
                return self.get_response(request)  # اجازه دسترسی به پنل ادمین

            # بازگشت صفحه 503
            return render(request, settings.MAINTENANCE_MODE_TEMPLATE)

        # اگر Maintenance فعال نباشد، درخواست ادامه می‌یابد
        response = self.get_response(request)
        return response
