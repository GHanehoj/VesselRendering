import numpy as np
import polyscope as ps
import meshio

ps.init()
ps.set_screenshot_extension(".png")
ps.set_ground_plane_mode("shadow_only")
ps.set_window_size(3000, 2000)
ps.set_SSAA_factor(2)
ps.set_up_dir("y_up")
ps.set_shadow_darkness(0.45)


WARM_GREY = (0.89, 0.808, 0.655)
DARK_GREY = (0.234, 0.325, 0.409)
PASTEL_RED = (0.512, 0.113, 0.113)
PASTEL_BLUE = (0.314, 0.511, 0.694)
PASTEL_DARK_BLUE = (0.207, 0.297, 0.523)
PASTEL_GREEN = (0.206, 0.541, 0.177)
PASTEL_YELLOW = (0.648, 0.545, 0.159)
PASTEL_PURPLE = (0.762, 0.333, 0.672)

def setview(mat):
    ps.set_camera_view_matrix(np.array(mat).reshape(4,4))



msh = meshio.read("full_4.mesh")
verts = msh.points
tets = msh.cells_dict["tetra"]


ps.register_volume_mesh(f"conn_tet", verts, tets[:1000], color=PASTEL_RED, interior_color=PASTEL_RED, edge_width=0.5)

setview([-0.177589818835258,1.11758708953857e-08,-0.984103918075562,506.248168945312,-0.791556596755981,0.59416651725769,0.142843142151833,97.2533416748047,0.584721267223358,0.804342210292816,-0.105518244206905,-1342.8515625,0.0,0.0,0.0,1.0])

ps.screenshot(
    filename="full_render0.png",
    transparent_bg=False
)
