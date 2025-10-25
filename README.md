# 🛒 Shopping Board 公示板

**欢迎来到采购清单公示板！**

本项目用于练习 **GitHub 团队协作流程**（Issues、Branch、Pull Request、Merge、CI/CD）。

所有的采购清单都以 **YAML 文件** 的形式存放在 `categories/` 目录中。

合并到 `main` 分支后，GitHub Actions 会自动汇总所有清单并更新此页面。

---

## 📊 当前采购总览

<!-- SHOPPING_TABLE_START -->
| 类别 | 物品 | 数量 | 发起人 | 领取人 | 状态 | 备注 |
|------|------|-------|----------|----------|--------|--------|
| groceries | 牛奶 | 2 箱 | 谢海林 | 谢海林 | ⏳ pending | 从山姆买 |
| groceries | 洗碗布 | 2 个 | 谢海林 | 谢海林 | ⏳ pending | 从山姆买 |
| groceries | 零食 | 待定 | 谢海林 | 谢海林 | ⏳ pending | 从山姆买 |
| groceries | 泡面 | 待定 | yzc | yzc | ⏳ pending | 从淘宝买 |

🕒 *Last updated: 2025-10-25 13:30:47 by GitHub Actions*
<!-- SHOPPING_TABLE_END -->

---

## 📘 使用说明与团队协作流程

下面的说明将带你一步步体验一个完整的团队协作开发流程，包括 Fork、创建分支、修改文件、提交PR、代码审核、自动测试、合并和冲突解决等环节。

### 1️⃣ Fork 与项目部署

1. 登录 GitHub，进入此仓库主页。
2. 点击右上角的 “Fork” → 将仓库复制到你自己的账号下。
3. 在你的仓库页面点击 Code → Copy URL。
4. 在本地克隆：

```bash
git clone https://github.com/<your-username>/shopping-list.git
cd shopping-list
```

5. 初始化环境（推荐 Python 3.12）：

```bash
pip install pyyaml
```

### 2️⃣ 创建新采购需求（Issues）

>所有新的采购任务或认领请求，都需要通过 Issue 记录。

1. 打开仓库 → 点击顶部的 Issues → New issue
2. 按模板填写：

	- 标题：例如 [Groceries] Add Milk and Bread
	- 内容：
		- 说明要购买的物品
		- 数量与需求人
		- 如果想认领任务，也可说明 “I will take this one”

3. 提交后等待维护者分配或评论。

### 3️⃣ 创建分支（Branch）

每个修改任务都应在独立分支中完成，避免直接在 `main` 修改。在你做出任何修改前，请运行：

```bash
git checkout -b feature/add-groceries
```

分支命名建议：

- `feature/add-xxx` 添加新清单或物品
- `fix/update-xxx` 修正信息
- `task/complete-xxx` 标记任务完成

### 4️⃣ 修改购物清单（YAML 文件）

所有清单都存放在 `categories/` 目录下。一个 YAML 文件对应一个类别。

#### 🆕 新建类别清单

`template` 目录下存在一个模版文件 `temp.yaml`。请 **复制** `template/temp.yaml` 到 `categories` 目录下并重命名为你的新购物清单的名字（不要直接修改模版文件本身）：

```bash
cp categories/template.yaml categories/my_new_list.yaml
```

编辑其中字段：

```yaml
category: tools
display_name: "🧰 Tools / 工具类"
items:
- name: 精密螺丝刀套装
quantity: 1
requester: alice
assignee: ""
status: needed
note: "要能够修电脑的那种"
```

#### 🆕 新增采购事项

在对应 `.yaml` 文件的 `items:` 字段下方添加一项：

```yaml
- name: 面包
quantity: 2 袋
requester: bob
assignee: ""
status: needed
note: ""
```

#### ✏️ 修改事项或分配任务

直接修改字段即可：

```yaml
assignee: alice
status: pending
```

#### ✅ 完成一个采购任务

更新状态为 `done`：

```yaml

status: done

note: "在全家买到了"

```

### 5️⃣ 提交修改

```yaml

git add categories/groceries.yaml

git commit -m "Add milk and bread to groceries list"

git push origin feature/add-groceries

```

#### ‼️ 重要：关于 commit 信息的规范：

> [!warning]
> 本项目的 commit 信息格式需要遵循 **约定式提交规范** v1.0.0。在提交任何commit之前，请务必阅读：[约定式提交](https://www.conventionalcommits.org/zh-hans/v1.0.0/)

### 6️⃣ 创建 Pull Request（PR）

1. 打开你 fork 的仓库页面；
2. GitHub 会提示「Compare & pull request」；
3. 点击按钮，填写说明（**对应 issue 编号**、修改内容）；
4. 提交后系统会自动运行 GitHub Actions 检查（YAML 校验）；
5. 等待 Maintainer 审核。

> [!warning]
> 1. 在每次你提交 Pull Request 前，都应该将源仓库同步到你的 fork 仓库以同步任何其他人的修改。
> 2. 请务必将你的 fork 仓库推送到源仓库的 `dev` 分支。

### 7️⃣ 代码审核与合并（Code Review & Merge）

- 审核者会在 PR 下方留言，提出改进建议；
- 所有自动检查通过后，可点击 “Merge pull request”；
- 合并后，`update_readme.yml` 会自动运行；
- GitHub Actions 将生成最新的 `README.md` 公示板并自动提交。

### 8️⃣ 解决冲突（Conflict Resolution）

若多名成员同时修改同一 YAML 文件，可能产生冲突：

1. 拉取最新主分支：

```bash
git fetch origin main
git merge origin/main
```
  
2. Git 会提示冲突位置；
3. 手动编辑文件解决；
4. 提交并重新 push：

```bash
git add .
git commit -m "Resolve conflict in groceries.yaml"
git push origin feature/add-groceries
```

### 9️⃣ 更新你的 Fork

每次提交 Pull Request 前，请同步主仓库最新内容：


```bash
git remote add upstream https://github.com/<original-owner>/shopping-board.git
git fetch upstream
git merge upstream/main
git push
```

### 1️⃣0️⃣ CI/CD 自动化说明

GitHub Actions 工作流：

- `check.yml`：在 PR 阶段自动检测 YAML 文件格式、重复项与合法状态；
- `update_readme.yml`：在合并后自动汇总所有清单并更新 README；

所有更新均由机器人账号 `github-actions` 提交。**请不要直接修改 `README` 。**

### 1️⃣1️⃣ 教学目标与收获

|技能|涵盖内容|
|---|---|
|**Git 基础操作**|clone, branch, merge, rebase, conflict|
|**团队协作流程**|issue 管理、PR 审核、代码合并|
|**自动化测试**|GitHub Actions 格式校验与自动更新|
|**数据结构管理**|使用 YAML 管理结构化清单|
|**文档与协作规范**|README、CONTRIBUTING、commit message|

### 1️⃣2️⃣ 贡献与反馈

- 欢迎通过 Issue 提出改进建议！
- 可新增 CI 检查逻辑、自动统计或生成网页看板；
- Maintainer 会定期合并贡献并发布新版本。
- 🛠️ 本项目设计用于教学与团队协作实践，任何成员都可自由 Fork、修改、练习。

### LICENSE / 许可证

本项目遵循 [The MIT License – Open Source Initiative](https://opensource.org/license/mit) 。