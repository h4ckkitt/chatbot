import subprocess
import time
import sys
import signal

def start_backend():
    # Launch the FastAPI backend using uvicorn
    return subprocess.Popen(["uvicorn", "app:app", "--reload", "--port", "8001"])

def start_frontend():
    # Launch the Streamlit frontend
    return subprocess.Popen(["streamlit", "run", "frontend.py"])

def main():
    try:
        print("Starting FastAPI backend...")
        backend_proc = start_backend()
        
        # Give the backend time to start before launching the frontend
        time.sleep(5)
        
        print("Starting Streamlit frontend...")
        frontend_proc = start_frontend()

        # Keep the main process alive while the child processes run
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("Shutting down processes...")
        # Terminate both processes on interrupt
        backend_proc.terminate()
        frontend_proc.terminate()
        sys.exit(0)

if __name__ == "__main__":
    main()