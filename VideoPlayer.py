import cv2

def main():
    video_path = 'path_to_your_video_file.mp4'  # 替换为你的视频文件路径
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Video playback completed.")
            break

        cv2.imshow('Video Player', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
