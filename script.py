import bpy

#for area in bpy.context.screen.areas:
#    if area.type == 'VIEW_3D':
#        area.spaces[0].viewport_shade = 'RENDERED'
        
#bpy.ops.render.render(animation=True)

bpy.context.scene.render.image_settings.file_format='JPEG'
#bpy.context.scene.render.filepath = ".pic%0.2d.jpg"%i
bpy.context.scene.render.filepath = 'xampp/htdocs/bpy/pic2d.jpg'
bpy.context.scene.render.resolution_x = 1920 #perhaps set resolution in code
bpy.context.scene.render.resolution_y = 1080
#bpy.ops.render.render()
bpy.ops.render.render(use_viewport = True, write_still=True)