# ---------------------------
from django.contrib import admin
from .models import User,Scheduler,ProgFile,History,EXEFILES,DetailActivity

# Register your models here.
admin.site.register(User)
admin.site.register(EXEFILES)
admin.site.register(DetailActivity)
@admin.register(Scheduler)
class SchedulerAdmin(admin.ModelAdmin):
    list_display=('ID','FILE_NAME','UNIQUE_NAME','PROGRAM_NAME','CLIENT_NAME','JOB_TITLE','FREQUENCY','STATUS','OUT_FILE_DIRECTORY')

@admin.register(ProgFile)
class ProgFileAdmin(admin.ModelAdmin):
    list_display=('ID','FILE_NAME','PROGRAM_NAME')

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display=('JobIDX','Date','Start','Finish','User','Product','File','Status','Log','ActiveCount','Page','Impression')

