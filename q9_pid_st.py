import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# PID implementation starts here
# -------------------------------------------

def system_model(knob_angle, prev_temp):
    # Knob angle to temperature
    knob_temp = knob_angle * 0.5
    # Calculate dT or change in temperature.
    m = 8
    dT = (knob_temp - prev_temp) / m
    # new temp = current temp + change in temp.
    return prev_temp + dT


##################################################################
# YOUR CODE STARTS HERE ##########################################
##################################################################

reference = 40

# Compute PID inputs and outputs for Plot 3.
pid_knob_angle_list = []
pid_water_temp_list = []
pid_t_list = []

sim_time = 50
dt = 1

# PID controller parameters
Kp = 500.
Kd = 200.
Ki = 0.

e = np.zeros(sim_time)  # initialize the output error terms
e_dot = np.zeros(sim_time)  # initialize the output error derivative terms
e_int = np.zeros(sim_time)  # initialize the output error integral terms

water_temp = 0.
pid_knob_angle = 0.
# PID control process runs below.
# You need to complete this part.
for t in range(sim_time):
    pid_t_list += [t]
    pid_knob_angle_list += [pid_knob_angle]
    pid_water_temp_list += [water_temp]


##################################################################
# YOUR CODE ENDS HERE ##########################################
##################################################################

# -----------------------------------------------------
# The following code helps plot out your PID result
# You can directly use them without the need to change.
# ----------------------------------------------------
# Create Plot 3 - PID
# Subplot 3-1 PID control inputs
plt.figure(figsize=(8, 8))
plt.subplot(211)
plt.title(f"PID Control (Kp={Kp}, Kd={Kd}, Ki={Ki})")
plt.ylabel("Knob Angle")
# Enter Data
plt.plot(pid_t_list, pid_knob_angle_list, 'k')
plt.plot(pid_t_list, np.ones(len(pid_t_list))*180, 'r--')  # plot the constraint
plt.ylim(0, 190)

# Subplot 3-2 PID control outputs
plt.subplot(212)
plt.ylabel("Water Temp")
# Enter Data
plt.plot(pid_t_list, pid_water_temp_list, 'ro')
plt.plot(pid_t_list, np.ones(len(pid_t_list))*40, '--')  # plot the reference
plt.ylim(0, 50)
plt.savefig('plot3')  # change the file name here to save your "plot4".
plt.show()
# Plot 3 ends
# -----------------------------------------------------------
