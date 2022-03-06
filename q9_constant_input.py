import numpy as np
import matplotlib.pyplot as plt


def system_model(knob_angle, prev_temp):
    # Knob angle to temperature
    knob_temp = knob_angle * 0.5
    # Calculate dT or change in temperature.
    m = 8
    dT = (knob_temp - prev_temp) / m
    # new temp = current temp + change in temp.
    return prev_temp + dT


# --------------------------
# Calculate data for Plot 1.
knob_angle_list = []
water_temp_list = []
t_list = []
knob_angle = 80
water_temp = 0.0
for t in range(50):
    t_list += [t]
    knob_angle_list += [knob_angle]
    water_temp_list += [water_temp]
    water_temp = system_model(knob_angle, water_temp)

# Create Plot 1 - Constant Input Case
# Subplot 1-1 Constant Inputs
plt.figure(figsize=(8, 8))
plt.subplot(211)
plt.title("Constant Input")
plt.ylabel("Knob Angle")
plt.plot(t_list, np.ones(len(t_list))*180, 'r--')
# Enter Data
plt.plot(t_list, knob_angle_list, 'k')
plt.ylim(0, 190)
# Subplot 1-2 Outputs
plt.subplot(212)
plt.ylabel("Water Temp")
plt.plot(t_list, np.ones(len(t_list))*40, '--')
# Enter Data
plt.plot(t_list, water_temp_list, 'ro')
plt.ylim(0, 50)
plt.savefig('plot1')
plt.show()

