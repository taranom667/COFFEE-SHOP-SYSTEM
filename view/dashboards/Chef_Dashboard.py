from  view.dashboards.DashboardView import *
class chef_dashboard(Dashboardview):
    def __init__(self):
        Dashboardview.__init__(self)
        self.window = Tk()
        self.window.geometry("540x900")