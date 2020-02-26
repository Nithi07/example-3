from django import forms

from QMS.models.common import Audittype




class Audittypeform(forms.ModelForm):
    
    class Meta:
        """Meta Attributes"""
        model = Audittype
        fields = "__all__"
