import cv2
import mediapipe as md
import time
from flask import Response

md_drawing=md.solutions.drawing_utils
md_drawing_styles=md.solutions.drawing_styles
md_pose=md.solutions.pose

terminateStatus = False
finalScore = 0

def terminate_TF():
    global terminateStatus
    global finalScore
    terminateStatus = True
    caloriesBurned = finalScore * 0.3 #600 cal bruned per hour of play divided by 3000 swings per hour
    return finalScore, caloriesBurned

def restart_TF():
    global terminateStatus
    if terminateStatus:
        terminateStatus = False
def generate_frames():
    count = 0
    position = None
    global finalScore

    cap=cv2.VideoCapture(0)#0: takes input from webcam

    with md_pose.Pose(
        min_detection_confidence=0.7, #accuracy of prediction
        min_tracking_confidence=0.7) as pose:
        while cap.isOpened():
            success,image=cap.read()#success var stores the success message. Checks if camera is there
            if not success:
                print("Empty Camera")
                break
                
            image = cv2.cvtColor(cv2.flip(image,1),cv2.COLOR_BGR2RGB) #first convert to cvt. Then flip image. Then convert from BGR to RGB
            result = pose.process(image)

            imlist=[]#stores all points of the pose landmarks

            if result.pose_landmarks:
                md_drawing.draw_landmarks(
                    image,result.pose_landmarks,md_pose.POSE_CONNECTIONS)#gets result of each point of pose landmarks
                for id,im in enumerate(result.pose_landmarks.landmark): #iterate through all landmarks. First val is ID and second val is landmark
                    h,w,_=image.shape
                    X,Y=int(im.x*w),int(im.y*h) #x,y is ratio val of landmark. This get exact coordinate
                    imlist.append([id,X,Y])
        
            
            if len(imlist)!=0: #check for if human is within the camera
                if(imlist[15][2] < imlist[11][2]): #start with right wrist below right shoulder
                    position="down"
                    countingStatus = False
                if(imlist[15][2]>imlist[12][2] and imlist[15][1] < imlist[11][1]) and position == "down": #right/left wrist comes up closer to left shoulder. Right wrist' x position is closer to shoulder and its y positiion higher
                    position="up"
                    bothArmsAbove = False
                    if not countingStatus:
                        count+=1
                        finalScore = count
                        countingStatus = True
                        print("finalScore inside: ", finalScore)

            
            if terminateStatus:
                break
            
            def flip_text_vertically(text):
                lines = text.split("\n")
                flipped_lines = reversed(lines)
                return "\n".join(flipped_lines)

            text = f"Tennis Forehand Count: {count}"
            flipped_text = flip_text_vertically(text)

            cv2.putText(
                image,
                flipped_text,
                (10, image.shape[0] - 10),  # Lower left corner
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
                cv2.LINE_AA,
            )


            ret, jpeg = cv2.imencode('.jpg', image)
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            

            # cv2.imshow("Jumping Jacks counter",image) #displaying
            
            # key=cv2.waitKey(1)
            # if key==ord('q'):
            #     break

        cap.release()
        

def run_tennisF_counter():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')




