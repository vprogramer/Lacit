import grpc
import glob
import grpcproject_pb2
import grpcproject_pb2_grpc
import pickle
import json
import cv2
import numpy as np


if __name__ == "__main__":
    channel = grpc.insecure_channel('localhost:6066')
    stub = grpcproject_pb2_grpc.ContourStub(channel)
    # Make a list of photo path.
    path = glob.glob("image/*.bmp")

    img = cv2.imread(path[0])
    # The photo was too big and it caused an error. In the end, I resized it.
    img = cv2.resize(img, (512, 1050))

    to_photo = grpcproject_pb2.Photo(photo = pickle.dumps(img))
    response = stub.Add(to_photo)

    all_skin_contours = []
    all_skin_contours = pickle.loads(response.photo)
    skin_contours = []
    for i in range(len(all_skin_contours)):
        skin_contours.append(all_skin_contours[i].tolist())
    # dict_with_contours = dict(zip(path[0], skin_contours))
    dict_with_contours = {path[0]: skin_contours}

    # Write json.
    with open('contours_grpc.json','w') as file:
        file.write(json.dumps(dict_with_contours))
