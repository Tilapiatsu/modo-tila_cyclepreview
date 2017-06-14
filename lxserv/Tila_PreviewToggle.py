
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

    def cmd_Flags(self):
        return lx.symbol.fCMD_MODEL | lx.symbol.fCMD_UNDO

    def basic_Enable(self, msg):
        return True

    def cmd_Interact(self):
        pass

    def togglePreview(self):
        if self.dyna_Bool(0):
            lx.eval('viewport.restore base.Tilapiatsu3DView false 3Dmodel')
            
        else:
            lx.eval('viewport.restore {} false primitive')
            lx.eval('iview.resume')

    def basic_Execute(self, msg, flags):
        self.togglePreview()

    def cmd_Query(self, index, vaQuery):
        lx.notimpl()


lx.bless(cmd_cyclepreview, "tila.cyclePreview")

