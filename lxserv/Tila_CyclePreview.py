#!/usr/bin/env python
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
import Tila_CyclePreviewModule as c
from Tila_CyclePreviewModule import CyclePreview 


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
    

    def basic_Execute(self, msg, flags):
        reload(c)
        reload(CyclePreview)
        CP = CyclePreview.cyclepreview(self.dyna_Bool(0))
        CP.togglePreview()

    def cmd_Query(self, index, vaQuery):
        lx.notimpl()

lx.bless(cmd_cyclepreview, c.TILA_CYCLEPREVIEW)