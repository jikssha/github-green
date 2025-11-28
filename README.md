<br />
<div align="center">
  <a href="https://github.com/jikssha/randomized-commit-template">
    <img src="https://media.giphy.com/media/du3J3cXyzhj75IOgvA/giphy.gif" alt="Logo" width="120" height="120">
  </a>

  <h1 align="center">🌱 Randomized Commit Template</h1>

  <p align="center">
    <b>让你的 GitHub 贡献图“绿”得自然，“绿”得随机，“绿”得有灵魂。</b>
    <br />
    Keep your GitHub contribution graph green, organic, and totally unsuspicious.
    <br />
    <br />
    <a href="https://github.com/jikssha/randomized-commit-template/actions">
      <img src="https://img.shields.io/github/actions/workflow/status/jikssha/randomized-commit-template/ci.yml?style=flat-square&logo=github-actions&label=Build" alt="Build Status">
    </a>
    <a href="https://github.com/jikssha/randomized-commit-template/stargazers">
      <img src="https://img.shields.io/github/stars/jikssha/randomized-commit-template?style=flat-square&color=yellow" alt="Stars">
    </a>
    <a href="https://github.com/jikssha/randomized-commit-template/blob/main/LICENSE">
      <img src="https://img.shields.io/github/license/jikssha/randomized-commit-template?style=flat-square&color=blue" alt="License">
    </a>
  </p>
</div>

---

<details>
  <summary><b>📚 目录 (Table of Contents)</b></summary>
  <ol>
    <li><a href="#-about-the-project">项目介绍</a></li>
    <li><a href="#-features">核心特性</a></li>
    <li><a href="#-getting-started">快速开始</a></li>
    <li><a href="#-configuration">高级配置</a></li>
    <li><a href="#-contributing">参与贡献</a></li>
    <li><a href="#-license">版权说明</a></li>
  </ol>
</details>

---

## 🤖 About The Project

> "Why is your GitHub profile so green?" 
> "I work hard. Or maybe... I just have a smart bot." 😉

你是否曾因为几天没有提交代码而感到焦虑？或者只是想让你的 GitHub 个人主页看起来更加活跃和酷炫？

**Randomized Commit Template** 是一个基于 GitHub Actions 的自动化工具。不同于那些只会机械式每天提交一次的笨拙脚本，本项目专注于**“模拟真实人类行为”**。它会在随机的时间、产生随机数量的提交，甚至偶尔“偷懒”不提交，从而生成一张看起来完全自然的贡献热力图。

### 为什么选择这个模板？
* 🚫 **拒绝机械感**：不再是死板的一天一更。
* ☁️ **无需服务器**：完全依赖 GitHub Actions，免费且稳定。
* 🛠 **高度可配**：你可以控制提交的频率、概率和时间段。

---

## ✨ Features

* 🎲 **智能随机化 (Smart Randomization)**
    * **随机提交次数**：每天可配置 1 到 N 次提交。
    * **随机时间点**：模拟真实的开发时间分布（甚至可以避开周末！）。
    * **随机跳过**：并不是每天都会运行，模拟真实的“休息日”。
* ⚡ **GitHub Actions 驱动**
    * 利用 Crontab 定时触发，无需本地运行，设置一次，永久自动运行。
* 📝 **动态提交信息**
    * 从预设的词库中随机选取 Commit Message，看起来就像你在认真写代码。
* 🔒 **安全隐蔽**
    * 只更新特定的日志文件（如 `LAST_UPDATED`），绝不污染你的核心代码库。

---

## 🚀 Getting Started

只需三步，你也能拥有迷人的“绿墙”！

### 1. Use this Template
点击页面右上角的 **[Use this template](https://github.com/jikssha/randomized-commit-template/generate)** 按钮，将本项目 Fork 到你的账号下。
> **注意**：建议将仓库设为 **Public**，否则贡献图可能仅对你自己可见（取决于你的 GitHub 设置）。

### 2. Configure Token (可选)
如果默认的 `GITHUB_TOKEN` 权限不够（通常默认够用），你需要：
1.  在 [Settings > Developer settings](https://github.com/settings/tokens) 生成一个新的 Token (勾选 `repo` 权限)。
2.  在你新仓库的 `Settings > Secrets and variables > Actions` 中添加一个 Secret，命名为 `GH_TOKEN`。

### 3. Enable Workflow
进入你仓库的 **Actions** 标签页。
* 如果看到警告，请点击 "I understand my workflows, go ahead and enable them"。
* 你可以手动触发一次 `Run workflow` 来测试是否生效。

🎉 **搞定！** 喝杯咖啡，坐等你的 Profile 变绿吧。

---

## ⚙️ Configuration

你可以通过修改 `.github/workflows/main.yml` (或你的实际 workflow 文件名) 来自定义行为。

### 🕒 修改运行频率 (Cron)
```yaml
on:
  schedule:
    # 默认：每 6 小时检查一次
    - cron: "0 */6 * * *"
    env:
  # 每次运行的最大提交次数
  MAX_COMMITS: 5 
  # 提交的概率 (0-1)，设为 0.8 表示有 20% 的概率今天不提交（休息日）
  COMMIT_PROBABILITY: 0.8

  🤝 Contributing
如果你有更有趣的随机算法，或者想扩充提交信息的词库，欢迎贡献！

Fork 本仓库

创建你的 Feature 分支 (git checkout -b feature/AmazingFeature)

提交你的修改 (git commit -m 'Add some AmazingFeature')

推送到分支 (git push origin feature/AmazingFeature)

开启 Pull Request
