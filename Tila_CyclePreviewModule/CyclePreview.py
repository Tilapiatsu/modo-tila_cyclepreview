import lx
import modo

class cyclepreview():

	def __init__(self, inPreviewMode):
		self.viewSvc = lx.service.View3Dport()
		self.inPreviewMode = inPreviewMode
		print self

	def get_current_view(self):
		self.viewSvc = lx.service.View3Dport()

		currentView = lx.object.View3D(viewSvc.View(viewSvc.Current()))
		print currentView.Matrix(0)
		print currentView.Angles()
		print currentView.Axis()
		print currentView.EyeVector()
		print currentView.WorkPlane()

	def togglePreview(self):
		if self.inPreviewMode:
			# lx.eval('viewport.restore base.TilaTmp3DView true 3Dmodel')
			# lx.eval('viewport.restore base.TilaTmp3DView false vptab')
			lx.eval('viewport.restore base.TilaTmp3DView false 3Dmodel')
			# lx.eval('viewport.delete TilaTmp3DView')
			
		else:
			currentView = lx.object.View3D(self.viewSvc.View(self.viewSvc.Current()))
			print currentView.Matrix(0)
			lx.eval('!!viewport.save TilaTmp3DView vp3dEdit')
			lx.eval('viewport.restore {} false primitive')
			lx.eval('iview.resume')