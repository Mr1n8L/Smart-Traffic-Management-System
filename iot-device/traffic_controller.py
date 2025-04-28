def change_traffic_light(priority):
    if priority:
        print("Changing traffic light to GREEN for emergency vehicle.")
    else:
        print("Standard traffic light operation.")

if __name__ == "__main__":
    from ambulance_inference import predict_ambulance
    ambulance_detected = predict_ambulance('captured_frame.jpg')
    change_traffic_light(ambulance_detected)
