import numpy as np

def simulate_trial(a, v, t):
    decision_time = np.random.normal(loc=a/v, scale=t)  
    correct = np.random.rand() < 0.5 + v/4  
    return decision_time, correct

def simulate_experiment(N, a, v, t):
    """Simulate the experiment with N trials."""
    trials = [simulate_trial(a, v, t) for _ in range(N)]
    return np.array(trials)

def main():
    a = np.random.uniform(0.5, 2)
    v = np.random.uniform(0.5, 2)
    t = np.random.uniform(0.1, 0.5) #parameters from canvas
    
    for N in [10, 40, 4000]: #parameters from canvas
        data = simulate_experiment(N, a, v, t)
        np.savetxt(f"simulated_data_{N}.csv", data, delimiter=",") #from chat on how to save experiment

if __name__ == "__main__":
    main()
