import cv2
import mediapipe as md

md_drawing=md.solutions.drawing_utils
md_drawing_styles=md.solutions.drawing_styles
md_pose=md.solutions.pose

count = 0

position = None

cap=cv2.VideoCapture(0)#0: takes input from webcam

with md_pose.Pose(
    min_detection_confidence=0.7, #accuracy of prediction
    min_tracking_confidence=0.7) as pose:
    while cap.isOpened():
        success,image=cap.read()#success var stores the success message. Checks if camera is there
        if not success:
            print("Emoty Camera")
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
            if(imlist[12][2] and imlist[11][2] >= imlist[14][2] and imlist[13][2]): #12,11 are shoulders. 13,14 are elbows. if elbows lower than shoulder, start the count
                position="down"
            if(imlist[12][2] and imlist[11][2] <= imlist[14][2] and imlist[13][2]) and position == "down": #once elbows bent back up, push up is finished so increment count
                position="up"
                count+=1
                print(count)

        
        
        def flip_text_vertically(text):
            lines = text.split("\n")
            flipped_lines = reversed(lines)
            return "\n".join(flipped_lines)

        text = f"Push-up Count: {count}"
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
        cv2.imshow("Push-up counter",image) #displaying
        
        key=cv2.waitKey(1)
        if key==ord('q'):
            break

    cap.release()





