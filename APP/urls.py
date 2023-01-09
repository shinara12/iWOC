from django.urls import path
from APP import views

urlpatterns = [
    # -----------------------------------------------
    path('',views.index,name='index'),
    path('login/', views.login_view, name='userlogin'),
    path('user/', views.user, name='user'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('employee/', views.employee, name='employee'),
    path('superadminhomepage/',views.superadminhomepage,name='superadminhomepage'), #admin homepage
    path('adminhomepage/',views.adminhomepage,name='adminhomepage'),
    path('userhomepage/',views.userhomepage,name='userhomepage'),
    path('Newprocess/',views.Newprocess,name='Newprocess'),
    path('schedulerdata/',views.schedulerdata,name='schedulerdata'),
    path('schedulerdataadmin/',views.schedulerdataadmin,name='schedulerdataadmin'),
    path('showHistory/', views.showHistory,name='showHistory'),
    path('show',views.show,name='showusers'),
    path('schedulerdata/',views.schedulerdata,name='schedulerdata'),
    path('startScheduler/', views.startScheduler,name='startScheduler'),
    path('show',views.show,name='showusers'),
    path('editusers/<int:id>',views.editusers, name = 'editusers'),
    path('updateusers/<int:id>',views.updateusers, name = 'updateusers'),
    path('delete/<int:id>',views.destroyusers),
    path('Newprocess/',views.Newprocess,name='Newprocess'),
    path('editprocess/<int:id>', views.editprocess,name='editprocess'),
    path('updateprocess/<int:id>', views.updateprocess,name='updateprocess'),
    path('deletep/<int:id>', views.deletep),
    path('logout/', views.logout , name = 'logout'),
]
