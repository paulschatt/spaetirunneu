import subprocess
import time
from invoke import task
import os
import signal
import sys

# Get the project root directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def wait_for_postgres(container_name="postgres", user="spaetirun"):
    """Wait for Postgres to be ready (optional if using Docker)."""
    print("Waiting for Postgres to be ready...")
    while True:
        result = subprocess.run(
            ["docker", "exec", container_name, "pg_isready", "-U", user],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if result.returncode == 0:
            break
        time.sleep(1)
    print("Postgres is ready!")


@task
def backend(c):
    """Start the FastAPI backend."""
    backend_dir = os.path.join(ROOT_DIR, "backend")
    venv_activate = os.path.join(backend_dir, "venv", "bin", "activate_this.py")
    # Activate virtualenv for Python subprocesses
    exec(open(venv_activate).read(), dict(__file__=venv_activate))

    print("Starting Backend...")
    proc = subprocess.Popen(
        ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0"],
        cwd=backend_dir,
    )
    return proc


@task
def frontend(c):
    """Start the frontend (Vite)."""
    frontend_dir = os.path.join(ROOT_DIR, "frontend")
    print("Starting Frontend...")
    proc = subprocess.Popen(["npm", "run", "dev"], cwd=frontend_dir)
    return proc


@task
def dev(c):
    """Start full stack (backend + frontend) and wait for Ctrl+C."""
    print("Starting Spaetirun Application...\n")

    # Optional: wait for Postgres if using Docker
    # wait_for_postgres()

    backend_proc = backend(c)
    frontend_proc = frontend(c)

    print("\nApplication started!")
    print("Backend:  http://localhost:8000")
    print("Frontend: http://localhost:5173")
    print("API Docs: http://localhost:8000/docs")
    print("\nPress Ctrl+C to stop all services")

    try:
        # Wait for both processes
        backend_proc.wait()
        frontend_proc.wait()
    except KeyboardInterrupt:
        print("\nStopping services...")
        for p in (backend_proc, frontend_proc):
            if p.poll() is None:
                p.send_signal(signal.SIGINT)
        print("Services stopped")
        sys.exit(0)