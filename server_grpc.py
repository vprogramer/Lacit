import grpc
from concurrent import futures
import time
import numpy as np
import cv2
import pickle
import grpcproject_pb2
import grpcproject_pb2_grpc


def use_findContours(img):
    hsv_min = np.array((0, 43, 20), np.uint8)
    hsv_max = np.array((30, 169, 255), np.uint8)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)
    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    max_len_contours = 0
    index_max_contour = 0
    for i in range(len(contours)):
        if max_len_contours < len(contours[i]):
            max_len_contours = len(contours[i])
            index_max_contour = i

    return contours[index_max_contour]


class ContourFromPhoto(grpcproject_pb2_grpc.ContourServicer):
    def Add(self, request, context):
        response = grpcproject_pb2.Photo()
        response.photo = pickle.dumps(use_findContours(pickle.loads(request.photo)))
        return response


if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpcproject_pb2_grpc.add_ContourServicer_to_server(ContourFromPhoto(), server)
    server.add_insecure_port('[::]:6066')
    server.start()
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)
