import yaml, os, sys

ALLOWED_STATUS = {"needed", "pending", "done"}

def check_yaml(file_path):
    ok = True
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"❌ Invalid YAML in {file_path}: {e}")
            return False

    category = os.path.splitext(os.path.basename(file_path))[0]
    if data.get("category") != category:
        print(f"❌ Category mismatch in {file_path} (expected '{category}')")
        ok = False

    items = data.get("items", [])
    seen = set()
    for item in items:
        name = item.get("name")
        status = item.get("status")
        if not name:
            print(f"❌ Missing item name in {file_path}")
            ok = False
        if name in seen:
            print(f"⚠️ Duplicate item '{name}' in {file_path}")
        seen.add(name)
        if status not in ALLOWED_STATUS:
            print(f"❌ Invalid status '{status}' in {file_path}")
            ok = False
    return ok

def main():
    all_ok = True
    for root, _, files in os.walk("categories"):
        for f in files:
            if f.endswith(".yaml"):
                if not check_yaml(os.path.join(root, f)):
                    all_ok = False
    sys.exit(0 if all_ok else 1)

if __name__ == "__main__":
    main()