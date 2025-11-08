# Randomized Commit Template — 一键部署指南

这个仓库模板可以让你的 GitHub 账号每天自动、随机提交代码，让贡献日历保持自然活跃。
它利用 GitHub Actions 定时触发脚本，在不同时间点生成随机提交。

## 🚀 一键部署步骤

### 第 1 步：创建仓库
1. 打开本模板仓库页面。
2. 点击右上角 **Use this template → Create a new repository**。
3. 填写仓库名称（如 `commit-bot`），点击 **Create repository**。

### 第 2 步：设置 Secrets
1. 打开仓库 → **Settings → Secrets and variables → Actions**。
2. 点击 **New repository secret**，依次添加：
   name- `ACTOR_NAME` → secret-你的 GitHub 用户名（如 `vaghr`）
   name- `ACTOR_EMAIL` → secret-你的 GitHub noreply 邮箱（如 `12345678+vaghr@users.noreply.github.com`）
   - （可选）`PUSH_TOKEN` → 个人访问令牌（PAT）

### 第 3 步：运行参数（可选修改）
工作流默认：每天北京时间 **09:00 / 16:00 / 23:00** 自动运行；每次随机提交 0～3 次。
可在 `.github/workflows/commit-random.yml` 中调整参数：
```yaml
SKIP_PROB: "0.08"               # 休息概率
MAX_COMMITS: "3"                # 每次运行最多提交次数
MIN_SLEEP: "15"                 # 提交间最短等待（秒）
MAX_SLEEP: "120"                # 提交间最长等待（秒）
MAX_START_DELAY_MINUTES: "60"   # 启动前随机延迟（分钟）
```

### 第 4 步：运行测试
1. 打开仓库顶部菜单 **Actions**。
2. 选择 `Randomized Daily Commits (Beijing schedule)` 工作流。
3. 点击 **Run workflow** 手动运行一次。
4. 日志出现 `Pushed commits successfully.` 表示成功。
5. 如果一直在运行未显示成功，这是因为添加了延迟，解决办法
   把  .github/workflows/commit-random.yml  中
  MAX_START_DELAY_MINUTES: "60" 
 改为
    MAX_START_DELAY_MINUTES: "0"

  即可
---

🧠 提示：自动化提交能让账户保持活跃，但结合真实项目提交会让贡献更自然。
