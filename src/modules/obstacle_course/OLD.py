def detect_cup_old():
    """
    Detects the cup and calculates distance to cup
    :return: None
    """
    # Set minimal points which he needs to detect the cup
    MIN_MATCH_COUNT = 20

    # Set the detector and create matcher
    detector = cv2.xfeatures2d.SIFT_create()

    FLANN_INDEX_KDITREE = 0
    flannParam = dict(algorithm=FLANN_INDEX_KDITREE, tree=5)
    flann = cv2.FlannBasedMatcher(flannParam, {})

    # Get training image of cup
    trainImg = cv2.imread("cup.jpg", 0)
    trainKP, trainDesc = detector.detectAndCompute(trainImg, None)

    # Get video of picamera
    cam = VideoStream(src=0, usePiCamera=False, resolution=(320, 240)).start()
    time.sleep(0.3)  # startup

    while True:
        # Get frame and turn it into black and white
        frame = cam.read()
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Set mask
        green = Color('green', [28, 39, 0], [94, 255, 255])
        mask = cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV), green.lower, green.upper)

        # Get contours and draw them when area of them is 1000 or higher
        ret, thresh = cv2.threshold(mask, 127, 255, 0)
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 1000:
                cv2.drawContours(mask, [cnt], -1, (255, 255, 255), 50)

        cv2.imshow('Masked cup', mask)

        # Detect points and compare with cup image and returns matches
        queryKP, queryDesc = detector.detectAndCompute(frame_gray, mask=mask)
        matches = flann.knnMatch(queryDesc, trainDesc, k=2)

        goodMatch = []

        # Counts matches
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                goodMatch.append(m)

        # If there are more matches then the minimal count, detect the cup and draw border
        if len(goodMatch) > MIN_MATCH_COUNT:
            tp = []
            qp = []
            for m in goodMatch:
                tp.append(trainKP[m.trainIdx].pt)
                qp.append(queryKP[m.queryIdx].pt)
            tp, qp = np.float32((tp, qp))
            H, status = cv2.findHomography(tp, qp, cv2.RANSAC, 3.0)
            h, w = trainImg.shape
            trainBorder = np.float32([[[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]])
            queryBorder = cv2.perspectiveTransform(trainBorder, H)

            moment = cv2.moments(queryBorder)

            # Calculate distance in a really ugly way
            x, y, w, h = cv2.boundingRect(queryBorder)
            distance = 0.00008650519031141868 * h ** 2 - 0.10294117647058823 * h + 35

            # Calculate the centre of mass
            cx = int(moment['m10'] / moment['m00'])
            cy = int(moment['m01'] / moment['m00'])

            # Adds text to center with 'cup'
            cv2.putText(frame, "Cup", (cx - 30, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            cv2.polylines(frame, [np.int32(queryBorder)], True, (255, 255, 255), 4)
            print("[INFO] Cup detected at distance: " + str(distance) + "cm")
        else:
            print("[INFO] Not Enough match found- %d/%d" % (len(goodMatch), MIN_MATCH_COUNT))
        cv2.imshow('Detected cup', frame)
        if cv2.waitKey(10) == ord('q'):
            break
    cam.stop()
    cv2.destroyAllWindows()
