import thumb



obj_path = "static/image3d/obj/c_pot2_mesh.obj"
texture_path = "static/image3d/texture/c_pot2_mesh.png"

thumb.create_thumbnail(obj_path, texture_path)

input_image = 'static/image3d/thumb/c_pot2_mesh_thumb.png'  
thumb.remove_bg(input_image)
