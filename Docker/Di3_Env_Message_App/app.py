import os

def main():
    name = os.environ.get("NAME", "DevOps student")
    environment = os.environ.get("ENVIRONMENT", "local")
    
    print("===================================")
    print("  DI3 – Eigen Docker image (env)  ")
    print("===================================")
    print(f"Hello, {name}!")
    print(f"Running in environment: {environment}")
    print("===================================")

if __name__ == "__main__":
    main()
