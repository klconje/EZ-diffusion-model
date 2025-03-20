import numpy as np
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path, header=None).values 

def estimate_parameters(data):
    mean_rt = np.mean(data[:, 0])  # Mean response time
    accuracy = np.mean(data[:, 1])  # Mean accuracy

    # Ensure v_est doesn't produce invalid values (e.g., division by zero)
    v_est = 4 * (accuracy - 0.5)
    if v_est == 0:
        v_est = 1e-6  # Small value to prevent division errors

    a_est = mean_rt * v_est
    t_est = mean_rt - (a_est / v_est)

    return a_est, v_est, t_est

def main():
    N_values = [10, 40, 4000]
    results = []

    for N in N_values:
        file_path = f"simulated_data_{N}.csv"
        data = load_data(file_path)
        a_est, v_est, t_est = estimate_parameters(data)

        results.append({
            "N": N,
            "a_est": round(a_est, 3),
            "v_est": round(v_est, 3),
            "t_est": round(t_est, 3)
        })
    print(pd.DataFrame(results))

if __name__ == "__main__":
    main()
#referenced chat
