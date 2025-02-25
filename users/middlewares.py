from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

class ExperienceSalaryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            try:
                experience = int(request.POST.get('experience', 0))
                if experience <= 1:
                    salary = 1000
                elif 2 <= experience <= 3:
                    salary = 2000
                elif 4 <= experience <= 5:
                    salary = 3000
                else:
                    salary = 5000
                request.salary = salary
            except (ValueError, TypeError):
                return JsonResponse({'error': 'Некорректные данные опыта'}, status=400)
