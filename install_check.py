import importlib
import sys, os

def check_environment(file):
    with open(file) as f:
        while f.readline().strip()!="dependencies:":
            for line in f:
                if not line.strip().startswith("-"):
                    break
                elif line.strip().endswith(":"):
                    continue
                lib = line.replace("-", "").strip()
                try:
                    l = importlib.import_module(lib)
                except Exception as e:
                    if lib=="scikitlearn":
                        lib = "sklearn"
                        try:
                            importlib.import_module(lib)
                            return True
                        except Exception as e:
                            pass
            
                    print("Failed to load module", lib)
                    return False
    return True

if __name__ == "__main__":
    if len(sys.argv)==2:
        envfile = sys.argv[1]
    else:
        envfile = [f for f in os.listdir() if f.endswith(".yaml")][0]
    if check_environment(envfile):
        print("All-Set! Packages installed.")
