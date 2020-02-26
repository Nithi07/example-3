from django.urls import path
from QMS.views.common import AudittypeCreate, AudittypeDelete, AudittypeUpdate, AudittypeDetail
   
app_name = 'QMS'


urlpatterns = [
    path('audittype/add',AudittypeCreate.as_view(),name='audittype-add' ),
    path('auditype/',common.AudittypeDetail.as_view(),name='auditype'),
    path('audittype/<int:pk>',AudittypeUpdate.as_view(),'audittype-update' ),
    path('audittype/<int:pk>/delete',AudittypeDelete.as_view(),'audittype-delete' ),
   ]
