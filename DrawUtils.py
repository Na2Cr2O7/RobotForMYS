import numpy as np
import pyrender
import trimesh
import random
import os
from PIL import Image
import DrawUtilsII
def add_watermark(image: Image, watermark_path='watermark.png') -> Image:
    """将水印添加到给定图像的右下角."""
    watermark = Image.open(watermark_path).convert("RGBA")  # 确保水印是RGBA格式
    image = image.convert("RGBA")  # 确保图像是RGBA格式

    # 计算水印位置
    position = (image.width - watermark.width, image.height - watermark.height)

    # 粘贴水印
    image.paste(watermark, position, watermark)  # 使用水印作为掩码，保留透明区域

    return image
def drawPicture(debug=False):
    if random.random()<0.5:
        A= DrawUtilsII.drawPicture()
        return add_watermark(A).convert('RGB')
    # 创建一个场景，背景设置为白色
    scene = pyrender.Scene(bg_color=[1.0, 1.0, 1.0, 1.0], ambient_light=[0.1, 0.1, 0.1])

    #检查文件是否存在
    if not os.path.exists('cube.obj'):
        import gene
        gene.generateGeometry()


    # 加载 3D 模型
    # 'UVsphere.obj','icosphere.obj'


    # 加载模型
    models = ['cube.obj', 'sphere.obj', 'cylinder.obj', 'cone.obj', 'torus.obj']  # 包含所有模型的列表
    appendixModels=[]
    for i in os.listdir():
        if os.path.isfile(i) and os.path.splitext(i)[1]=='.obj':
            if i not in models:
                appendixModels.append(i)
    models2=models+appendixModels
    models=models2
    num_models = 20  # 指定放置的模型数量：20


    for _ in range(num_models):
        # 随机选择模型
        model_name = random.choice(models2)
        f=False
        while not f:
            f=True
            model_name = random.choice(models2)
            try:
                mesh = trimesh.load_mesh(model_name)
            except:
                f=False
                print('X',model_name)
                
                continue
            try:
                mesh_node = pyrender.Mesh.from_trimesh(mesh)
            except:
                f=False
                print('X',model_name)
                os.remove(model_name)
                models2.remove(model_name)
                continue
        # 随机位置 (x, y, z)
        position = np.random.uniform(low=-2, high=2, size=3)  # x, y, z 范围可以根据您的需求调整

        # 随机生成旋转角度 (roll, pitch, yaw)
        roll = np.random.uniform(low=0, high=2 * np.pi)
        pitch = np.random.uniform(low=0, high=2 * np.pi)
        yaw = np.random.uniform(low=0, high=2 * np.pi)
        
        # 创建旋转矩阵
        rotation_matrix = trimesh.transformations.euler_matrix(roll, pitch, yaw)

        # 随机缩放因子（保持各方向一致）
        uniform_scale_factor = np.random.uniform(low=0.5, high=1.5)  # 一个统一的缩放因子
        scale_matrix = np.eye(4)
        scale_matrix[:3, :3] *= uniform_scale_factor  # 在所有方向上应用相同的缩放因子

        # 创建变换矩阵
        transform_matrix = np.eye(4)  # 创建一个单位矩阵
        transform_matrix[:3, 3] = position  # 设置位置
        transform_matrix = transform_matrix @ rotation_matrix  # 应用旋转
        transform_matrix = transform_matrix @ scale_matrix  # 应用缩放

        # 设置节点变换
        scene.add(mesh_node, pose=transform_matrix)

    # 添加多个灯光
    num_lights = 5  # 指定灯光数量
    for _ in range(num_lights):
        # 创建方向光
        #灯光强度 4
        light = pyrender.DirectionalLight(color=[1.0, 1.0, 1.0], intensity=4.0)
        
        # 随机设置灯光位置
        light_position = np.random.uniform(low=-3, high=3, size=3)
        
        # 创建灯光变换矩阵
        light_pose = np.eye(4)
        light_pose[:3, 3] = light_position  # 设置灯光位置
        
        # 将灯光添加到场景
        scene.add(light, pose=light_pose)

    # 设置相机
    camera = pyrender.PerspectiveCamera(yfov=np.pi / 3.0)
    camera_pose = np.eye(4)
    camera_pose[:3, 3] = np.array([0, 0, 5])  # 设置相机位置
    scene.add(camera, pose=camera_pose)

    # 设置渲染器
    renderer = pyrender.OffscreenRenderer(viewport_width=1920, viewport_height=1080)

    # 进行渲染
    rgb, depth = renderer.render(scene)

    # 关闭渲染器
    renderer.delete()

    # 保存图像
    
    image = Image.fromarray(rgb)
    image=add_watermark(image)
    return convertToRGB(image)
        
    #return add_watermark(DrawUtilsII.main(image).convert('RGB')).convert('RGB')
def convertToRGB(image):
    return image.convert('RGB')
if __name__ == '__main__':
    convertToRGB(drawPicture(debug=True)).save('test.jpg')
