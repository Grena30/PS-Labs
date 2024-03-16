from utils import *


# TASK 1
Ts1 = 0.01
Ts2 = 0.001
limit_signal = 1
limit_filter = 50
ts1_plot = round(limit_signal/Ts1)
ts2_plot = round(limit_signal/Ts2)

# 1.1
t1, x1 = generate_white_noise(Ts1, limit_filter)
plot_signal(t1[:ts1_plot * 5], x1[:ts1_plot * 5], title="White noise, step 0.01")

# 1.2
plot_signal(t1[:ts1_plot], x1[:ts1_plot], title="White noise histogram, step 0.01", histogram=True)

# 1.3
t2, x2 = generate_white_noise(Ts2, limit_filter)
plot_signal(t2[:ts2_plot * 5], x2[:ts2_plot * 5], title="White noise, step 0.001")

# 1.4
plot_signal(t2[:ts2_plot], x2[:ts2_plot], title="White noise histogram, step 0.001", histogram=True)

# 1.5
y1 = filter_signal(Ts1, x1)
plot_signal(t1, y1, title="Filtered noise, step 0.01")

# 1.6
y2 = filter_signal(Ts2, x2)
plot_signal(t2, y2, title="Filtered noise, step 0.001")


# TASK 2
R1 = 50
R2 = 1
step1 = 1
step2 = 0.001
M = [3, 5, 10, 20, 50, 100]

# 2.1
m, s = generate_signal(R1, step1)
plot_multiple_signals(m, [s], title="Original signal")

# 2.2
m, d = generate_signal(R1, step1, random=True)
plot_multiple_signals(m, [d], title="Noise signal")

# # 2.3
plot_multiple_signals(m, [s, d], labels=["Original signal",  "Noise signal"], title="Original and noise signal")

# 2.4
x = s + d
plot_multiple_signals(m, [s, x], labels=["Original signal", "Modified signal"], title="Original and modified signal")

# 2.5
y1 = filter_signal_mfa(M[0], x)
plot_multiple_signals(m, [y1, x, s], labels=["Filtered signal", "Modified signal", "Original signal"], title="Multiple signals, M=3")

# 2.6
y2 = filter_signal_mfa(M[1], x)
plot_multiple_signals(m, [y2, x, s], labels=["Filtered signal", "Modified signal", "Original signal"], title="Multiple signals, M=5")

y3 = filter_signal_mfa(M[2], x)
plot_multiple_signals(m, [y3, x, s], labels=["Filtered signal", "Modified signal", "Original signal"], title="Multiple signals, M=10")

# 2.7
m, s = generate_signal(R2, step2, sawtooth_signal=True)
m, d = generate_signal(R2, step2, random=True)
x = s + d
y4 = filter_signal_mfa(M[3], s)
plot_multiple_signals(m, [y4, x, s], labels=["Filtered signal", "Modified signal", "Original signal"], title="Multiple signals, M=20")

# 2.8
y5 = filter_signal_mfa(M[4], s)
plot_multiple_signals(m, [y5, x, s], labels=["Filtered signal", "Modified signal", "Original signal"], title="Multiple signals, M=50")

y6 = filter_signal_mfa(M[5], s)
plot_multiple_signals(m, [y6, x, s], labels=["Filtered signal", "Modified signal", "Original signal"], title="Multiple signals, M=100")