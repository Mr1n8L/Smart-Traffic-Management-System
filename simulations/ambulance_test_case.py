def simulate_traffic(congestion_level):
    if congestion_level > 70:
        print("High congestion detected. Activating dynamic signal control.")
    else:
        print("Traffic normal. Default timing applies.")

if __name__ == "__main__":
    simulate_traffic(85)
