import time
from prometheus_client import start_http_server, Gauge
import WinTmp

# Create a Prometheus gauge metric
cpu_temp_metric = Gauge('cpu_temp', 'CPU temperature every 1 sec')
gpu_temp_metric = Gauge('gpu_temp', 'GPU temperature')

if __name__ == '__main__':
    # Start the Prometheus HTTP server on port 9183
    start_http_server(9183)
    while True:
        try:
            cpu_temp = WinTmp.CPU_Temp()
            print('CPU temperature is: ', cpu_temp)
            # Set the value of the Prometheus metric for CPU temperature
            cpu_temp_metric.set(cpu_temp)
        except Exception as e:
            print(f"Error retrieving CPU temperature: {e}")

        try:
            gpu_temp = WinTmp.GPU_Temp()
            print('GPU temperature is: ', gpu_temp)
            # Set the value of the Prometheus metric for GPU temperature
            gpu_temp_metric.set(gpu_temp)
        except Exception as e:
            print("GPU temperature could not be retrieved. Skipping...")
            # You can choose to set a default value or leave it unset
            gpu_temp_metric.set(0)  # Optional: Set to 0 or any default value

        # Sleep for 1 sec
        time.sleep(1)