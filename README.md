# SINOSHIP - 船舶与航运开源项目

## 项目简介

SINOSHIP 是一个面向船舶设计与航运领域的开源基础设施项目，提供船舶建模、仿真与优化工具。

## 🧬 技术来源与体系

本仓库是 **SINOSHOP** 海洋空间智能生态母体的一部分，为“船舶与航运”维度提供基础设施工具。

- **顶层规范与母体仓库**：[SINOSHOP-OS](https://gitee.com/sinoshop/sinoshop-os) 定义了 SLFS (Super Large Floating Structure) 核心架构与物理基准（135m×27m，五层载荷抵消体系）。
- **理论基础**：[SINOSFT](https://gitee.com/Sino-Submerged Floating Tunnel/SINOSFT) 提供悬浮隧道基础设施的数学公理与数值仿真标准。
- **相关应用实例**：基于 SLFS 架构的极地氢能仿真验证平台 [sinoshop-openice](https://gitee.com/SINOSHIP/sinoshop-openice)。

## 技术栈

- Python 3.8+
- unittest (测试框架)

## 快速开始

### 克隆项目

```bash
git clone https://gitee.com/SINOSHIP/sinoship.git
cd sinoship
```

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行示例

```bash
python main.py
```

### 运行测试

```bash
python -m unittest discover tests
```

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 参与贡献

欢迎通过 Issue 或 Pull Request 参与贡献。请确保代码风格一致，并包含相应的测试用例。

---

*贞忠昭日月，惠民播春秋。*