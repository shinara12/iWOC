from django.contrib import admin
from django.urls import path
from APP import views

urlpatterns = [
    # -----------------------------------------------
    path('',views.index,name='index'),
    path('login/', views.login_view, name='userlogin'),
    path('user/', views.user, name='user'),
    path('admin/', admin.site.urls),
    # path('customer/', views.customer, name='customer'),
    # path('employee/', views.employee, name='employee'),
    path('superadminhomepage/',views.superadminhomepage,name='superadminhomepage'), #admin homepage
    path('adminhomepage/',views.adminhomepage,name='adminhomepage'),
    path('userhomepage/',views.userhomepage,name='userhomepage'),
    path('Newprocess/',views.Newprocess,name='Newprocess'),
    path('Newprocessuser/',views.Newprocessuser,name='Newprocessuser'),
    path('schedulerdata/',views.schedulerdata,name='schedulerdata'),
    path('schedulerdataadmin/',views.schedulerdataadmin,name='schedulerdataadmin'),
    path('schedulerdatauser/', views.schedulerdatauser , name = 'schedulerdatauser'),    # newly added 
    path('showHistory/', views.showHistory,name='showHistory'),
    path('show/',views.show,name='showusers'),
    path('schedulerdata/',views.schedulerdata,name='schedulerdata'),
    path('startScheduler/', views.startScheduler,name='startScheduler'),
    # path('show/',views.show,name='showusers'),
    path('show_user_info/',views.show_user_info,name='show_user_info'),
    path('editusers/<int:id>',views.editusers, name = 'editusers'),
    path('updateusers/<int:id>',views.updateusers, name = 'updateusers'),
    path('delete/<int:id>',views.destroyusers),
    path('Newprocess/',views.Newprocess,name='Newprocess'),
    path('editprocess/<int:id>', views.editprocess,name='editprocess'),
    path('editprocess_user/<int:id>', views.editprocess_user,name='editprocess_user'),
    path('updateprocess/<int:id>', views.updateprocess,name='updateprocess'),
    # path('schedulerdata/<int:id>', views.updateprocess,name='updateprocess'),
    path('updateprocess_user/<int:id>', views.updateprocess_user,name='updateprocess_user'),    
    path('deletep/<int:id>', views.deletep),
    path('logout/', views.logout , name = 'logout'),
    path('stopprocess/', views.stopprocess , name = 'stopprocess'), 
    path('show_recent_acti/', views.show_recent_acti , name = 'show_recent_acti'),
    path('schedulerdata_superadmin/', views.schedulerdata_superadmin , name = 'schedulerdata_superadmin'),  
    

]
