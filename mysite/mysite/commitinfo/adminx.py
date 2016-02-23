import xadmin
from commitinfo.models import Kernel_Project,Libvirt_Project,OpenStack_Project

class CommitInfoAdmin(object):
    # ...
    list_display = ('name','datetime','comment','hashvalue')

xadmin.site.register(Kernel_Project,CommitInfoAdmin)
xadmin.site.register(Libvirt_Project,CommitInfoAdmin)
xadmin.site.register(OpenStack_Project,CommitInfoAdmin)
