import aspose.threed as a3d

#코드 효율적으로 바꾸기

scene = a3d.Scene.from_file("static/text3d/fbx/model.fbx")
scene.save("static/text3d/obj/model2.obj")