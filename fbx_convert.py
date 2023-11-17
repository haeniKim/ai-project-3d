
import aspose.threed as a3d

scene = a3d.Scene.from_file("static/text3d/obj/model.obj")
scene.save("static/text3d/fbx/model.fbx")