# EZ-diffusion-model
This project uses a simulate-and-recover approach to test whether the EZ diffusion model can accurately estimate parameters from simulated data that were generated using the same model. This is a helpful cognitive modeling process that used as a lens on the data.
We randomly selected realistic model parameters based on the following guidelines:
    Boundary separation a between 0.5 and 2
    Drift rate v between 0.5 and 2
    Nondecision time t between 0.1 and 0.5
    Data is simulated for N=10, 40, and 400 trials and repeated 100x for each N
  Our results should indicate whether the EZ model remains consistent and valid.
