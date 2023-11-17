import os
import cv2
import numpy as np
import rembg
from vedo import *

#image to 3d thumbmail 모듈

#기본 썸네일 생성
def create_thumbnail(obj_path, texture_path, output_dir="static/image3d/thumb/"):
    # Extract the base name from obj_path
    base_name = os.path.splitext(os.path.basename(obj_path))[0]
    
    # Load the 3D model and apply texture
    mesh = Mesh(obj_path)
    mesh.texture(texture_path)
    
    # Create a Plotter object
    plotter = Plotter(offscreen=True, screensize=(200, 200))
    
    # Add the mesh to the plotter
    plotter.add(mesh)
    
    # Reset the camera
    plotter.reset_camera()
    
    # Save a screenshot with the base name
    screenshot_path = os.path.join(output_dir, f"{base_name}_thumb.png")
    plotter.zoom(7).show().screenshot(screenshot_path)

def remove_bg(input_image, model_name='u2net', recenter=True, output_dir="static/image3d/thumb"):
    session = rembg.new_session(model_name=model_name)

    out_base = os.path.basename(input_image).split('.')[0]
    out_rgba = os.path.join(output_dir, out_base + '_rm.png')

    # load image
    print(f'[INFO] loading image {input_image}...')
    image = cv2.imread(input_image, cv2.IMREAD_UNCHANGED)

    # carve background
    print(f'[INFO] background removal...')
    carved_image = rembg.remove(image, session=session)  # [H, W, 4]
    mask = carved_image[..., -1] > 0

    # recenter
    if recenter:
        print(f'[INFO] recenter...')
        final_rgba = np.zeros((200, 200, 4), dtype=np.uint8)

        coords = np.nonzero(mask)
        x_min, x_max = coords[0].min(), coords[0].max()
        y_min, y_max = coords[1].min(), coords[1].max()
        h = x_max - x_min
        w = y_max - y_min
        desired_size = 200
        scale = desired_size / max(h, w)
        h2 = int(h * scale)
        w2 = int(w * scale)
        x2_min = (200 - h2) // 2
        x2_max = x2_min + h2
        y2_min = (200 - w2) // 2
        y2_max = y2_min + w2
        final_rgba[x2_min:x2_max, y2_min:y2_max] = cv2.resize(carved_image[x_min:x_max, y_min:y_max], (w2, h2), interpolation=cv2.INTER_AREA)

    else:
        final_rgba = carved_image

    # write image
    cv2.imwrite(out_rgba, final_rgba)

       