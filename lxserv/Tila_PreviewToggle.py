
################################################################################
#
# scriptname.py
#
# Version:
#
# Author:
#
# Description:
#
# Last Update:
#
################################################################################

import lx
import lxifc
import lxu.command


class cmd_cyclepreview(lxu.command.BasicCommand):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
        self.dyna_Add('inPreviewMode', lx.symbol.sTYPE_BOOLEAN)

        self.viewSvc = lx.service.View3Dport()

    def cmd_Flags(self):
        return lx.symbol.fCMD_MODEL | lx.symbol.fCMD_UNDO

    def basic_Enable(self, msg):
        return True

    def cmd_Interact(self):
        pass

    def get_current_view(self):
        viewSvc = lx.service.View3Dport()

        currentView = lx.object.View3D(viewSvc.View(viewSvc.Current()))
        print currentView.Matrix(0)
        print currentView.Angles()
        print currentView.Axis()
        print currentView.EyeVector()
        print currentView.WorkPlane()

    def togglePreview(self):
        if self.dyna_Bool(0):
            lx.eval('viewport.restore base.TilaTmp3DView false vptab')
            lx.eval('viewport.delete TilaTmp3DView')
            
        else:
            currentView = lx.object.View3D(self.viewSvc.View(self.viewSvc.Current()))
            print currentView.Matrix(0)
            lx.eval('!!viewport.save TilaTmp3DView vpapplication')
            lx.eval('viewport.restore {} false primitive')
            lx.eval('iview.resume')

    def basic_Execute(self, msg, flags):
        self.togglePreview()

    def cmd_Query(self, index, vaQuery):
        lx.notimpl()


lx.bless(cmd_cyclepreview, "tila.cyclePreview")

