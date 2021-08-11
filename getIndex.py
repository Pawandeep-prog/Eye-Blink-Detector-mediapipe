import cv2
import mediapipe as mp
import numpy

cap = cv2.VideoCapture(0)

face = mp.solutions.face_mesh
Face = face.FaceMesh()
mp_drawing = mp.solutions.drawing_utils

while True:
	_, frame = cap.read()

	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	results = Face.process(rgb)

	if results.multi_face_landmarks:
		for face_landmarks in results.multi_face_landmarks:
			for ind, i in enumerate(face_landmarks.landmark):
				cv2.putText(frame, str(ind), (int(i.x*640), int(i.y*480)), cv2.QT_FONT_NORMAL, 0.2, (0,255,0))

				print(i.x)

	cv2.imshow("window", frame)

	if cv2.waitKey(1) == 27:
		cv2.destroyAllWindows()
		cap.release()
		break