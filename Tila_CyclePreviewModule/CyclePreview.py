import lx
import modo

class cyclepreview():

	def __init__(self, inPreviewMode):
		self.viewSvc = lx.service.View3Dport()
		self.inPreviewMode = inPreviewMode
		self.renderCamera = modo.Item(lx.eval('render.camera ?'))
		self.scn = modo.Scene()
		self.currScn = modo.scene.current()
		self.tmpCameraView = {}

	def print_current_view(self):
		currentView = lx.object.View3D(self.viewSvc.View(self.viewSvc.Current()))
		print dir(currentView)
		print currentView.Matrix(0)
		print currentView.Angles()
		print currentView.Axis()
		print currentView.EyeVector()
		print currentView.WorkPlane()

	def get_camera_view(self):
		self.scn.select(self.renderCamera)
		posX = lx.eval('transform.channel pos.X ?')
		posY = lx.eval('transform.channel pos.Y ?')
		posZ = lx.eval('transform.channel pos.Z ?')

		rotX = lx.eval('transform.channel rot.X ?')
		rotY = lx.eval('transform.channel rot.Y ?')
		rotZ = lx.eval('transform.channel rot.Z ?')

		target = lx.eval('item.channel camera$target ?')

		focal = lx.eval('item.channel camera$focalLen ?')
		dof = lx.eval('item.channel camera$dof ?')
		focus = lx.eval('item.channel camera$focusDist ?')
		irisBlades = lx.eval('item.channel camera$irisBlades ?')
		irisRot = lx.eval('item.channel camera$irisRot ?')
		edgeWeight = lx.eval('item.channel camera$irisBias ?')

		motionBlur = lx.eval('item.channel camera$motionBlur ?')
		blurLength = lx.eval('item.channel camera$blurLen ?')
		shutterSpeed = lx.eval('item.channel camera$blurLen ?')
		blurOffset = lx.eval('item.channel camera$blurOff ?')

		self.scn.deselect()

		return {'pX': posX,
				'pY': posY,
				'pZ': posZ,
				'rX': rotX,
				'rY': rotY,
				'rZ': rotZ,
				'target': target,
				'focal': focal,
				'dof': dof,
				'focus': focus,
				'irisBlades': irisBlades,
				'irisRot': irisRot,
				'edgeWeight': edgeWeight,
				'motionBlur':  motionBlur,
				'blurLength': blurLength,
				'shutterSpeed': shutterSpeed,
				'blurOffset': blurOffset}
	
	def sync_camera_view(self, camera, cameraView):
		self.scn.select(camera)

		# lx.eval('transform.channel pos.X %s' % cameraView['pX'])
		# lx.eval('transform.channel pos.Y %s' % cameraView['pY'])
		# lx.eval('transform.channel pos.Z %s' % cameraView['pZ'])
		# lx.eval('transform.channel rot.X %s' % cameraView['rX'])
		# lx.eval('transform.channel rot.Y %s' % cameraView['rY'])
		# lx.eval('transform.channel rot.Z %s' % cameraView['rZ'])
		# lx.eval('item.channel camera$target %s' % cameraView['target'])
		# lx.eval('item.channel camera$focalLen %s' % cameraView['focal'])

		lx.eval('item.channel camera$dof %s' % cameraView['dof'])
		lx.eval('item.channel camera$focusDist %s' % cameraView['focus'])
		lx.eval('item.channel camera$irisBlades %s' % cameraView['irisBlades'])
		lx.eval('item.channel camera$irisRot %s' % cameraView['irisRot'])
		lx.eval('item.channel camera$irisBias %s' % cameraView['edgeWeight'])

		lx.eval('item.channel camera$motionBlur %s' % cameraView['motionBlur'])
		if cameraView['motionBlur']:
			lx.eval('item.channel camera$blurLen %s' % cameraView['blurLength'])
			lx.eval('item.channel camera$blurLen %s' % cameraView['shutterSpeed'])
			lx.eval('item.channel camera$blurOff %s' % cameraView['blurOffset'])

		self.scn.deselect()

	def togglePreview(self):
		if self.inPreviewMode:
			lx.eval('viewport.restore base.TilaTmp3DView false 3Dmodel')
			lx.eval('viewport.delete TilaTmp3DView')

			self.scn.select(self.renderCamera)	
			lx.eval('delete')
			
		else:
			# currentView = lx.object.View3D(self.viewSvc.View(self.viewSvc.Current()))
			self.tmpCameraView = self.get_camera_view()

			tmpCamera = self.scn.addItem('camera')
			tmpCamera.name = 'TilaTmpCamera'

			self.scn.select(tmpCamera)
			lx.eval('camera.syncView')
			self.sync_camera_view(tmpCamera, self.tmpCameraView)
			self.scn.deselect()

			lx.eval('render.camera %s' % 'TilaTmpCamera')

			# lx.eval('!!viewport.save TilaTmp3DView vp3dEdit')
			lx.eval('!!viewport.save TilaTmp3DView vp3dEdit')
			lx.eval('viewport.restore {} false primitive')
			lx.eval('iview.resume')