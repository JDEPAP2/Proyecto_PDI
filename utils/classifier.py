import time, cv2, keras, os
import numpy as np
from threading import Thread

directory = os.path.dirname(__file__)
path = os.path.join(directory, 'modeloGN.h5')


class Predictor:
    model = keras.models.load_model(path)
    time_pross = 0
    time_predict = 0
    label, percent = -1,0
    frame = []

    def main(self):
        cap = cv2.VideoCapture(1)
        while True:
            start = time.time()
            success, frame = cap.read()
            frame = cv2.convertScaleAbs(frame,alpha=1.2,beta=-15)
            frame[:,:,0] = cv2.equalizeHist(frame[:,:,0])
            if not success:
                break
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                continue

            frame_bytes = buffer.tobytes()
            self.frame = frame
            if cap.get(cv2.CAP_PROP_POS_FRAMES) % 10 == 0:
                thread = Thread(target = self.callThread)
                thread.start()
                thread.join()
                pass
            
            self.time_pross = time.time() - start
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    def callThread(self):
        self.label, self.percent = self.predict(self.frame)

                    
    def predict(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = cv2.resize(frame,(224,224))
        img = img/255
        start = time.time()
        y_predict = self.model.predict([np.expand_dims(img, axis=0)])
        self.time_predict = time.time() - start
        return np.argmax(y_predict), np.max(y_predict)