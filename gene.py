import trimesh

# 创建基本几何体
def generateGeometry():
    cube = trimesh.creation.box(extents=(.5,.5,.5))           # 立方体
    sphere = trimesh.creation.icosphere(radius=0.2)           # 球体
    cylinder = trimesh.creation.cylinder(radius=0.2, height=.4)  # 圆柱体
    cone = trimesh.creation.cone(radius=0.2, height=.4)        # 圆锥体

    #还有吗？
    torus = trimesh.creation.torus(major_radius=1, minor_radius=0.3)   # 环形体

    #torusKnot = trimesh.creation.torus_knot(radius=1, thickness=0.2, segments=64)   # 环形体

        # 网格
    #extrusion = trimesh.creation.extrusion(path=[[0, 0, 0], [0, 0, 1]], extrude_height=1)   # 拉伸体
    #sweep = trimesh.creation.sweep_polygon(polygon=trimesh.creation.annulus(r_min=0.5, r_max=1.0, h=0.5), path=trimesh.creation.circle(radius=0.5))   # 扫帚状体
    #poly = trimesh.creation.random_polygon(radius=0.5, n=10)   # 随机多边形





    # 将几何体保存为 OBJ 文件
    cube.export('cube.obj')
    sphere.export('sphere.obj')
    cylinder.export('cylinder.obj')
    cone.export('cone.obj')
    torus.export('torus.obj')
#torusKnot.export('torusKnot.obj')
#grid.export('grid.obj')

if __name__ == '__main__':
    generateGeometry()




# 信息打印
#print("基本几何体已保存为 OBJ 文件:")
#print("1. cube.obj")
#print("2. sphere.obj")
#print("3. cylinder.obj")
#print("4. cone.obj")
#print("5. torus.obj")
#print("6. torusKnot.obj")
#print("7. grid.obj")

#print("完成！")
#print(["cube.obj", "sphere.obj", "cylinder.obj", "cone.obj", "torus.obj"])
