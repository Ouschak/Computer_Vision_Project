# import cv2
# import time


# cap = cv2.VideoCapture(0)
# frame_test=0



# if not cap.isOpened():
#     raise RuntimeError("Camera not accessible")
# fps = cap.get(cv2.CAP_PROP_FPS)
# print("FPS:", fps)
# sampleEveryFrame=int(fps)
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break   

#     frame_test+=1

#     if frame_test % (sampleEveryFrame//6) !=0:
#         continue
    
#     cv2.imshow("Camera Test", frame)
#     print(frame.shape,end="\r")
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
# cap.release()
# cv2.destroyAllWindows()




import cv2 as cv



vid=cv.VideoCapture("https://manifest.googlevideo.com/api/manifest/hls_playlist/expire/1766090038/ei/1hBEaardMKKOv_IPh5KywQw/ip/197.146.10.226/id/f8b46298c7dbae3b/itag/625/source/youtube/requiressl/yes/ratebypass/yes/pfa/1/wft/1/sgovp/clen%3D448760090%3Bdur%3D492.074%3Bgir%3Dyes%3Bitag%3D313%3Blmt%3D1752522456110201/rqh/1/hls_chunk_host/rr3---sn-f5o5-jhoz.googlevideo.com/xpc/EgVo2aDSNQ%3D%3D/cps/12/met/1766068438,/mh/Gv/mm/31,29/mn/sn-f5o5-jhoz,sn-h5qzen7l/ms/au,rdu/mv/m/mvi/3/pl/23/rms/au,au/initcwndbps/556250/bui/AYUSA3AH3OmJwfBci47p_ywuBuPxOch_BQKR-yHvMGCyzML5dG3ixaKyghGctNfTMYLj9KIxF3JYzr4b/spc/wH4Qq7_iOJsQbm_2sj74Bx7gnEbZfvGdUu8dpm6k7MiLEJ_y_Xf2NI5TfG7KussV/vprv/1/playlist_type/DVR/dover/13/txp/5432534/mt/1766067916/fvip/5/short_key/1/keepalive/yes/fexp/51552689,51565116,51565681,51580968/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,pfa,wft,sgovp,rqh,xpc,bui,spc,vprv,playlist_type/sig/AJfQdSswRQIgNeeSIo38mT4JHvk4p-jr0DPo5xnWhORGHGQiEnPsQ-wCIQCGGJu2r9L589eslDuUE4P6AiYxloc-D2Dxv3BNgbHklg%3D%3D/lsparams/hls_chunk_host,cps,met,mh,mm,mn,ms,mv,mvi,pl,rms,initcwndbps/lsig/APaTxxMwRAIgZvWooehRqXbr79utkR-pLze6vgqCpxFeiluqiNZOklYCIFMjPAk42nSgISCOLzt7GssQjH2FzwipuepAKTo1FIlr/playlist/index.m3u8")

if not vid.isOpened:
    raise RuntimeError("camera not there")

while True:

    state,frame=vid.read()
    print(frame.shape)
    frame.shape[0]//=3
    frame.shape[1]//=3    
    if not state:

        break

    cv.imshow("video",frame)
    
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

vid.release()
cv.destroyAllWindows()
