import torch
import json

# with open("ray.json", "r") as json_file:
#     dataset = json.load(json_file)

# # data = 이미지 1장, [x, y, z] 좌표
# for data in dataset:
#     img_path = data['img_path']
#     coord = data['coord']

#     # {x, y, z} = data['xyz']

#     # [x, y] 정보로 샘플링 -> [30, 768]
#     # [30, 768] -> 이미지 생성, Train

#     # 아래는 기존의 diffusion training process

#     # interpolated_embedding # made by interpolation of 9 embeddings


