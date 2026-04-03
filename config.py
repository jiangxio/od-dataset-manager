import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "datasets", "calling", "images")
LABELS_DIR = os.path.join(BASE_DIR, "datasets", "calling", "labels")
BACKUP_LABELS_DIR = os.path.join(LABELS_DIR, "backup")

# 自定义类别列表。根据你的实际用例推广可修改这个列表。
CLASSES = ["call_phone", "not_call_phone", "other"]

# 数据导入时允许的图像扩展名
IMAGE_EXTS = ['.jpg', '.jpeg', '.png']
