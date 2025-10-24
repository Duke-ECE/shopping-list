import yaml, os, datetime, re

TABLE_START = "<!-- SHOPPING_TABLE_START -->"
TABLE_END = "<!-- SHOPPING_TABLE_END -->"

def load_all_items():
    items = []
    for file in sorted(os.listdir("categories")):
        if not file.endswith(".yaml"):
            continue
        category = file.replace(".yaml", "")
        with open(f"categories/{file}", "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            for i in data.get("items", []):
                items.append({
                    "category": category,
                    "name": i.get("name", ""),
                    "quantity": i.get("quantity", ""),
                    "requester": i.get("requester", ""),
                    "assignee": i.get("assignee", "") or "(unassigned)",
                    "status": i.get("status", ""),
                    "note": i.get("note", "")
                })
    return items

def status_icon(status):
    return {"done": "✅", "pending": "⏳", "needed": "❌"}.get(status, "❔")

def generate_table(items):
    header = "| 类别 | 物品 | 数量 | 发起人 | 领取人 | 状态 | 备注 |\n"
    header += "|------|------|-------|----------|----------|--------|--------|\n"
    rows = []
    for i in items:
        rows.append(
            f"| {i['category']} | {i['name']} | {i['quantity']} | "
            f"{i['requester']} | {i['assignee']} | {status_icon(i['status'])} {i['status']} | {i['note']} |"
        )
    return header + "\n".join(rows)

def update_readme(table_md):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    if TABLE_START not in content or TABLE_END not in content:
        raise RuntimeError("❌ README.md 缺少标记区块（请添加 SHOPPING_TABLE_START / END 注释）")

    pattern = re.compile(f"{TABLE_START}.*?{TABLE_END}", re.DOTALL)
    new_table = f"{TABLE_START}\n{table_md}\n{TABLE_END}"

    updated = re.sub(pattern, new_table, content)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated)
    print("✅ README.md 已更新")

def main():
    print("📂 Current working directory:", os.getcwd())
    print("📄 Target README exists:", os.path.exists("README.md"))

    items = load_all_items()
    md_table = generate_table(items)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 在表格结尾添加更新时间
    md_table += f"\n\n🕒 *Last updated: {now} by GitHub Actions*"

    update_readme(md_table)

if __name__ == "__main__":
    main()
