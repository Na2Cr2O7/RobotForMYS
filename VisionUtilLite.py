from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

model_id = 'damo/mplug_image-captioning_coco_base_zh'
input_caption = 'https://alice-open.oss-cn-zhangjiakou.aliyuncs.com/mPLUG/image_captioning.png'

pipeline_caption = pipeline(Tasks.image_captioning, model=model_id)
result = pipeline_caption(input_caption)
print(result)
