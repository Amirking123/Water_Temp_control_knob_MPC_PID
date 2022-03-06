import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# MPC implementation starts here
# -----------------------------------

##################################################################
# YOUR CODE STARTS HERE ##########################################
##################################################################

reference = 40

# MPC controller should be defined below.
# You need to complete this part.
class MPC:
    def __init__(self):
        self.horizon = 20
        self.m = 8

    def predict_model(self, u, T0):

        T1 = T0 + (( (0.5 * u) - T0)/self.m)

        return T1

    def cost_function(self, u, temp_water):
        cost = 0.0
        for i in range(self.horizon):
            T1 = self.predict_model(u[i], temp_water)
            cost += abs(T1-reference)
        return cost

    # ---------------------------------------------------
    # The following function serves as the MPC optimizer.
    # You can directly use this optimizer method without reimplement it
    def mpc_optimizer(self, temp_water):
        u = np.ones(self.horizon)  # create Inputs to be optimized
        # Set bounds.
        bounds = []
        for i in range(self.horizon):
            bounds += [[0, 180]]

        # Non-linear optimization.
        u_solution = minimize(self.cost_function,
                              u,
                              (temp_water,),
                              method='SLSQP',
                              bounds=bounds,
                              tol=1e-8)
        return u_solution.x
    # MPC optimizer ends

mpc = MPC()

# Compute MPC inputs and outputs for Plot 2.
mpc_knob_angle_list = []
mpc_water_temp_list = []
mpc_t_list = []

water_temp = 0.
mpc_knob_angle = 0.
sim_time = 50
# MPC control iterations run below.
# You need to complete this part.
for t in range(sim_time):
    #Line should be
    # mpc_knob_angle = mpc.mpc_optimizer(water_temp)[t]
    #To avoid the error (solution 1)
    # mpc_knob_angle = mpc.mpc_optimizer(water_temp)[0]
    # To avoid the error (solution 2)
    if t <= 19:
        mpc_knob_angle = mpc.mpc_optimizer(water_temp)[t]
    elif t <= 38:
        mpc_knob_angle = mpc.mpc_optimizer(water_temp)[t-19]
    elif t <= 57:
        mpc_knob_angle = mpc.mpc_optimizer(water_temp)[t - 38]
    water_temp = mpc.predict_model(mpc_knob_angle, water_temp)
    # print(mpc_knob_angle)
    mpc_t_list += [t]
    mpc_knob_angle_list += [mpc_knob_angle]
    mpc_water_temp_list += [water_temp]


##################################################################
# YOUR CODE ENDS HERE ##########################################
##################################################################

# ---------------------------------------------------
# The following code helps plot out your MPC result
# You can directly use them without the need to change.
# ---------------------------------------------------
# Create Plot 2 - MPC
# Subplot 2-1 MPC control inputs
plt.figure(figsize=(8, 8))
plt.subplot(211)
plt.title("MPC")
plt.ylabel("Knob Angle")
plt.plot(mpc_t_list, np.ones(len(mpc_t_list))*180, 'r--')  # plot the constraint
# Enter data
plt.plot(mpc_t_list, mpc_knob_angle_list, 'k')
plt.ylim(0, 190)

# Subplot 2-2 MPC control output
plt.subplot(212)
plt.ylabel("Water Temp")
plt.plot(mpc_t_list, np.ones(len(mpc_t_list)) * 40, '-')  # plot the reference
# Enter data
plt.plot(mpc_t_list, mpc_water_temp_list, 'ro')
plt.ylim(0, 50)
plt.savefig('plot2')
plt.show()

# Plot 2 ends
# ---------------------------------------------------
# ---------------------------------------------------

