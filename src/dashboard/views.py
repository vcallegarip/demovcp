# from django.views.generic.base import TemplateView
#
# class Dashboard(TemplateView):
#     # template_name = "index.html"
#     saludo = 'Hello World!'


# from django.http import HttpResponse
# from django.views.generic import View
#
# class Dashboard(View):
#
#     def get(self, request):
#         # <view logic>
#         return HttpResponse('result')


from django.views.generic import TemplateView

class Dashboard(TemplateView):

    template_name = 'index.html' # or define get_template_names()

    def get_context_data(self, **kwargs):

        context = super(Dashboard, self).\
            get_context_data(**kwargs)
        context['first_names'] = ['Nathan', 'Richard']

        return context
