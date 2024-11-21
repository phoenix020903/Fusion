from django.urls import path
from . import  views 

urlpatterns = [
    path('leave-form-submit/', views.LeaveFormSubmitView.as_view(), name='leave-form-submit'), 
    path('bonafide-form-submit/', views.BonafideFormSubmitView.as_view(), name='bonafide-form-submit'), 
    path('admin-bonafide-requests/',views.FetchPendingBonafideRequests.as_view(),name='admin-bonafide-requests'),
    path('admin-updates/',views.UpdateBonafideStatus.as_view(),name='admin-updates'),
    path('bonafide-status/',views.GetBonafideStatus.as_view(),name='bonafide-status'),
]
