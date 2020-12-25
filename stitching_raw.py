import cv2
import numpy as np

left = cv2.imread('10.png')
left1 = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY)
right = cv2.imread('13.png')
right1 = cv2.cvtColor(right, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create();
kp1, des1 = sift.detectAndCompute(left1,None)
kp2, des2 = sift.detectAndCompute(right1,None)

#FLANN_INDEX_KDTREE = 0
#index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
#search_params = dict(checks = 50)
#match = cv2.FlannBasedMatcher(index_params, search_params)
match = cv2.BFMatcher()
matches = match.knnMatch(des1,des2,k=2)

good = []
for m,n in matches:
    if m.distance < 0.4*n.distance:
        good.append(m)

draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                   singlePointColor = None,
                   flags = 2)

matches = cv2.drawMatches(left,kp1,right,kp2,good,None,**draw_params)

MIN_MATCH_COUNT = 10
if len(good) > MIN_MATCH_COUNT:
    src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    h,w = left1.shape
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    dst= cv2.perspectiveTransform(pts,M)
    #right1 = cv2.polylines(right,[np.int32(dst)],True,255,3, cv2.LINE_AA)
else:
    print('not enough matches are found. %d/%d', (len(good)/MIN_MATCH_COUNT))

dst = cv2.warpPerspective(left,M,(right.shape[1] + left.shape[1], right.shape[0]))
dst[0:right.shape[0],0:right.shape[1]] = right

def trim(frame):
    #crop top
    if not np.sum(frame[0]):
        return trim(frame[1:])
    #crop top
    if not np.sum(frame[-1]):
        return trim(frame[:-2])
    #crop top
    if not np.sum(frame[:,0]):
        return trim(frame[:,1:])
    #crop top
    if not np.sum(frame[:,-1]):
        return trim(frame[:,:-2])
    return frame

cv2.namedWindow('left keypoints', cv2.WINDOW_NORMAL)
cv2.resizeWindow('left keypoints' , 1000,600)
cv2.imshow('left keypoints',trim(dst))
cv2.imwrite('stitched_raw.png', trim(dst))
