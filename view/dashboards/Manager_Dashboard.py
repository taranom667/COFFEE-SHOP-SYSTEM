from  view.dashboards.DashboardView import *
class manager_dashboard(Dashboardview):
    def __init__(self):
        Dashboardview.__init__(self)
        self.window = Tk()
        self.window.geometry("100x100")