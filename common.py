from django.shortcuts import render, redirect
from QMS.models.common import Audittype
from QMS.form.formcommon import Audittypeform
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import  reverse_lazy  


class AudittypeList(ListView):
    model = Audittype
    template_name = 'superadmin/audittype_view.html'
    context_object_name = 'auditype'


class AudittypeCreate(CreateView):
    model = Audittype
    template_name = 'mysite/audittype.html'
    fields = ['audittype','auditcode']
    success_url = reverse_lazy('superadmin:audittype_view.html')

    def get_success_url(self):
    """Return the URL to redirect to after processing a valid form."""
    if not self.success_url:
        raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
    return str(self.success_url)  # success_url may be lazy


    def post(self, request, *args, **kwargs):
    """
    Handle POST requests: instantiate a form instance with the passed
    POST variables and then check if it's valid.
    """
    form = self.get_form()
    if form.is_valid():
        return self.form_valid(form)
    else:
        return self.form_invalid(form)

    def form_valid(self, form):
    """If the form is valid, redirect to the supplied URL."""
    return HttpResponseRedirect(self.get_success_url())


class AudittypeUpdate(UpdateView):
    model = Audittype
    template_name = 'superadmin/edit.html'
    fields = ['audittype','auditcode']
    success_url = reverse_lazy('superadmin:audittype_view.html')


class AudittypeDelete(DeleteView):
    model = Audittype
    template_name = 'superadmin/audittype_view.html'
    fields = ['audittype','auditcode']
    success_url = reverse_lazy('superadmin:audittype_view.html')






    

    

#class AudittypeUpdate(UpdateView):
#    model = Audittype


#def audittype(request):
#    if request.method == 'post':
#        form = audittypeform(request.post)
#        if form.is_valid():
#            try:
#                form.save()
#                redirect('/audittypeshow')
#            except:
#                pass
#    else:
#        form = audittypeform()

#    return render(request, 'superadmin/audittype.html', {'form':form})


#def audittypeshow(request):
#    types = Audittype.objects.all()
#    return render(request, 'superadmin/audittype_view.html', {'types':types})


#def edit(request, id):
#    type = Audittype.objects.get(id=id)
#    return render(request, 'superadmin/edit.html', {'type':type})

#def update(request, id):
#    type = Audittype.objects.get(id=id)
#    form = Audittypeform(request.POST, instance=type)
#    if form.is_valid():
#        form.save()
#        redirect('/audittypeshow')
#    return render(request, 'superadmin/edit.html', {'type':type})








