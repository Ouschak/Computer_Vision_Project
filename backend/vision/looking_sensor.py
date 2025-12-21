import logging
import cv2
import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks.python.core import base_options


class LookingSensor:
    def __init__(self, model_path="models/face_landmarker.task", debug=True):
        self.log = logging.getLogger(self.__class__.__name__)
        self.debug = debug

        # ---- Load MediaPipe Face Landmarker ----
        options = vision.FaceLandmarkerOptions(
            base_options=base_options.BaseOptions(model_asset_path=model_path),
            running_mode=vision.RunningMode.VIDEO,
            num_faces=1,
            output_face_blendshapes=False,
            output_facial_transformation_matrixes=False,
        )

        self.face_landmarker = vision.FaceLandmarker.create_from_options(options)

        self.frame_index = 0  # required for VIDEO mode timestamps

    def process_frame(self, frame_bgr):
        """
        Process a single frame and return raw vision observations.
        """

        if frame_bgr is None:
            return {"face_present": False}

        h, w, _ = frame_bgr.shape

        # ---- Convert BGR -> RGB ----
        frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)

        # ---- Wrap into MediaPipe Image ----
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=frame_rgb,
        )

        # ---- Run face landmark detection ----
        timestamp_ms = int(self.frame_index * 1000 / 30)
        result = self.face_landmarker.detect_for_video(
            mp_image,
            timestamp_ms,
        )
        self.frame_index += 1

        # ---- Face presence check ----
        if not result.face_landmarks:
            return {"face_present": False}

        # One face only
        landmarks = result.face_landmarks[0]

        # ---- Debug: draw ONE landmark (nose-ish index 1) ----
        if self.debug:
            for lm in landmarks:
                x_px = int(lm.x * w)
                y_px = int(lm.y * h)

                cv2.circle(
                    frame_bgr,
                    (x_px, y_px),
                    radius=1,
                    color=(0, 255, 0),
                    thickness=-1,
                )

        return {
            "face_present": True,
            "nose_px": (x_px, y_px),
        }

    def close(self):
        self.log.info("Closing FaceLandmarker")
        self.face_landmarker.close()
