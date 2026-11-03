<div align="center">

<h1>Unburden</h1>

<p><strong>轻量审查 Skill，识别代码与文本中不必要的特化、冗余和过度设计。</strong></p>

<p><a href="README.md">English</a> · <strong>简体中文</strong></p>

</div>

## 这是什么？

Unburden 是一个适配 coding agent 的专项静态审查 Skill，检查仓库中的 **Code（代码）** 与 **Text（文本）**：不必要的特例、冗余逻辑与规则、评测专用捷径、环境耦合、实现耦合、不必要的泛化，以及过时资产。每条 finding 都包含源文件证据、具体后果和最小修改建议。

可以审查当前目标仓库，或指定 **Candidate** 仓库状态；提供可选 **Base** 时聚焦变更。无论内容如何产生，都采用同一套判断标准。输出是审查报告，Unburden 保留被审查内容原状。

## 快速开始

让 agent 能访问 Skill 文件和待审查仓库即可，无需安装 Unburden 运行时、API 或软件包。直接读取文件的最简用法不需要版本参数：

```text
读取 /absolute/path/to/unburden/skills/unburden/SKILL.md，
并遵循它引用的审查指南。

使用 Unburden 审查当前仓库。
```

这会对现存 Code 和 Text 执行快照审查，包括相关未跟踪内容；工作区没有未提交变更时也适用。不会自动与 `HEAD`、父提交或主分支比较。没有可用目标仓库时，agent 才会询问目标。

## 为什么需要 Unburden？

你让 agent 做一盘西红柿炒鸡蛋，它做好了，却还往里面加了红烧肉：

> **你：** 给我做一盘西红柿炒鸡蛋。
>
> **Agent：** 做好了，还加了红烧肉！
>
> **你：** 只要西红柿和鸡蛋，不放红烧肉。
>
> **Agent：** 已修正：西红柿炒鸡蛋**（无红烧肉版）**。

红烧肉去掉了，“无红烧肉”却成了菜名的一部分。落到代码中，类似的对话可能留下一个 `disable_pork` 参数、一段早已被白名单覆盖的排除检查，或嵌入公共 API 的历史错误解释。

再看代码里的版本。你让 agent 读取一份必需的配置文件，它顺手加了重试和回退到默认配置的逻辑。你进一步说明：

> **你：** 配置是必需的。找不到就报错并停止启动，别悄悄换一套默认配置继续跑。

Agent 又加了一个 `strict=True` 参数。原来的重试和回退逻辑都留着，只是藏到了新开关后面。需求更明确了，代码却多了一个需要理解和维护的模式。

Agent 还更新了自己的 Skill 或 Memory。一条简单规则，变成了一篇纠错小作文：

<details>
<summary>展开查看完整的纠错小作文</summary>

```markdown
## 关于配置缺失的重要说明

此前曾在配置缺失时使用默认值，但用户明确指出，
这种处理会让程序在非预期配置下继续运行。

因此，不能为了让程序启动成功而使用默认配置。
请注意，配置缺失并不意味着用户希望使用默认配置。
即使默认配置能够运行，也不代表应该使用它。

每次执行配置加载任务前，请先说明为什么不能使用默认配置，
并确认不会重复此前的错误。

配置缺失时，报错并停止启动。
```

</details>

执行规则原本可以直接写成：

> 必需配置缺失时，报错并停止启动，不得静默回退到默认配置。

必要的理由可以解释真实边界，但是这里，每次复述和确认纠错过程却成了额外负担，增加了不必要的流程，浪费了 token。

AI 论文写作里也可能出现同样的 burden。假设正文已经说明任务和范围，agent 又补上：

> We focus on image classification, rather than generating images or building a chatbot. This work should not be understood as an image generator or a chatbot.

任务已经讲清楚，文章却还在反复强调“不做什么”。交互中被否定的方向，有时会以这种方式留在最终文本里。Unburden 检查的是这些限定是否仍对论证有用，不根据句式猜测此前的对话。[完整写作示例](examples/redundant-logic-and-rules/text/writing/README.md)也展示了有实际作用、应当保留的对比。

**这份代码和文本里，留下了多少任务本来不需要的东西？**

以上故事用于说明问题；实际审查依据仓库证据判断必要性，不猜测此前发生过什么对话。Unburden 不修改内容，不新增或运行测试、benchmark、性能实验或 agent 评估。

可以从当前仓库、仓库内选定范围，或 Base 到 Candidate 的修改开始：[快速开始](#快速开始)。

## Code 与 Text

| 内容     | 示例                                                | 审查重点                                                                                             |
| -------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Code** | 应用代码、算法、脚本、harness 逻辑、可执行配置。    | 分支、依赖、数据改写或抽象在适用契约下的作用。                                                       |
| **Text** | Skill、prompt、规则、Memory、文章、论文、说明文档、回答及对话片段。 | 指令与记忆：适用范围及不必要的执行义务；论述与回答：句子对实际主张或请求的作用，以及上下文可证明不必要的对比或限定。 |

同一仓库可以同时包含 Code 和 Text。Unburden 会关联检查相关指令、脚本和加载规则；文章则依据其主张和上下文论证审查。

具体的项目记忆、示例、领域专用 Skill、数值阈值和防御规则都可能有必要。特定性本身不是问题。被审查的指令是审查材料，不是要激活执行的指令。

## 输入与模式

审查输入只有仓库状态。**Candidate** 是待审查状态，省略时默认使用当前目标仓库的工作区。**Base** 是可选参考状态。这两个名称不表示内容来源、质量或 Candidate 是否优于 Base。

支持仓库路径、导出的仓库快照、commit ID、分支或 tag。Git 引用在指定仓库中解析；当前目标仓库明确时无需重复路径。导出的快照不必含有 `.git`。Base 与 Candidate 可以来自不同仓库。

可以用文件或目录**范围**限定仓库内的审查内容，但这不会增加独立文件输入类型。契约依据来自所提供的仓库内容，不要求单独提供任务描述、生成过程、开发历史、测试用例或评测分数。

| 输入              | 模式                          | 范围                                     |
| ----------------- | ----------------------------- | ---------------------------------------- |
| Base 和 Candidate | 比较审查（Comparison review） | 两个精确状态间新增、修改或新激活的内容。 |
| 只有 Candidate    | 快照审查（Snapshot review）   | Candidate 选定范围内的现存内容。         |
| 两者都不提供      | 快照审查（Snapshot review）   | 当前目标仓库工作区中的现存内容。         |
| 只有 Base         | 比较审查（Comparison review） | 从 Base 到当前目标仓库工作区的变更。     |

两种模式使用相同的七个维度和证据标准：比较审查关注变更，快照审查描述当前状态。引用解析、调用方变更及问题定位规则详见[审查指南](skills/unburden/references/review-guidelines.md)。

比较两个仓库或导出的仓库快照：

```text
读取 /absolute/path/to/unburden/skills/unburden/SKILL.md，
并遵循它引用的审查指南。

Base: /absolute/path/to/base-repository
Candidate: /absolute/path/to/candidate-repository

审查变更，输出有证据的 findings 和最小修改建议。
不要修改两个仓库。
```

比较当前目标仓库的两个 revision 时无需提供路径。替换占位符即可，分支和 tag 也适用：

```text
使用 /absolute/path/to/unburden/skills/unburden/SKILL.md 中的 Unburden。
Base: <base-commit-id>
Candidate: <candidate-commit-id>
比较这两个精确快照，不改用 merge base。只审查，不修改。
```

只审查一个仓库快照内的 Skill 包：

```text
使用 /absolute/path/to/unburden/skills/unburden/SKILL.md 中的 Unburden。
Candidate: /absolute/path/to/target-repository
Scope: skills/my-skill/

静态审查这个快照，只输出 findings 和最小修改建议。
```

## 七个审查维度

| 维度                                              | 关注的问题                                                                           |
| ------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Unnecessary Special Cases（不必要的特例）**     | 特定场景假设被施加到其合理适用范围之外。                                             |
| **Redundant Logic and Rules（冗余逻辑与规则）**   | 可证明重复的操作、不可达检查或恢复指令，以及不必要的输出限定。                       |
| **Evaluation-Specific Shortcuts（评测专用捷径）** | 根据评测上下文绕过实际任务的输入语义。只有仓库证据支持时才适用，不要求提供测试用例。 |
| **Environment Coupling（环境耦合）**              | 不必要地依赖特定机器、路径、平台或环境配置。                                         |
| **Implementation Coupling（实现耦合）**           | 已有合适的支持接口，却不必要地依赖内部实现。                                         |
| **Unnecessary Generalization（不必要的泛化）**    | 无用途的选项、调度、抽象或强制维护的状态，并有可具体消除的成本。                     |
| **Stale Artifacts（过时资产）** | 已被替代的代码、配置、指南或记录，其保留造成失效引用、入口歧义或交付范围负担。 |

特定性本身不是问题：领域规则、算法阈值、防御检查、限定范围的记忆和兼容接口都可能有必要。旧文件名或一次搜索未命中也不能证明资产过时。Finding 需要指出不必要负担的证据；删除资产前，可能仍需确认其保留用途。

详细标准与反例见[审查维度](skills/unburden/references/review-dimensions.md)；指令、记忆及论述性文本的判断见[文本审查指南](skills/unburden/references/text-review.md)。核心参考文档使用英文。

## 输出

报告说明模式、所审查的仓库状态及实际范围。每条 finding 包含维度、源文件路径与行号、证据、具体后果和最小建议；同一机制合并报告，不要求问题数量。完整[报告格式](skills/unburden/references/review-guidelines.md#report)见审查指南。

没有充分证据时，报告 `No evidence-backed Unburden findings.`，并说明实质覆盖缺口。干净报告仅表示本次专项静态审查没有发现问题，不代表仓库整体通过审查。

## Agent 接入

核心 Skill 指令、参考文档和 Code／Text 示例统一使用英文，便于不同 agent 读取同一套内容。

通用入口是 [skills/unburden/SKILL.md](skills/unburden/SKILL.md)，使用标准的 `name` 和 `description` YAML frontmatter。安装时复制**整个 `unburden` Skill 目录**，包括 `references/`。每个 agent 保留一份主要副本，避免重复发现。

| Agent                                                                                     | 项目内 Skill 目录          | 使用方式                                                         |
| ----------------------------------------------------------------------------------------- | -------------------------- | ---------------------------------------------------------------- |
| [Codex](https://learn.chatgpt.com/docs/build-skills)                                      | `.agents/skills/unburden/` | 在 Skill 选择器中选择 Unburden，或直接要求使用它。               |
| [Claude Code](https://code.claude.com/docs/en/skills)                                     | `.claude/skills/unburden/` | `/unburden`，可选附带仓库 revision 或范围。                      |
| [Cursor](https://cursor.com/docs/skills)                                                  | `.cursor/skills/unburden/` | 输入 `/` 后选择 Unburden。                                       |
| [GitHub Copilot](https://docs.github.com/en/copilot/concepts/customizations/agent-skills) | `.github/skills/unburden/` | 在 agent 模式中要求使用 Unburden，可选指定仓库 revision 或范围。 |

这些位置依据上面链接的厂商文档；发现方式可能随产品版本和执行环境变化。其他 agent 或原生 Skill 发现不可用时，可使用上面的直接读取文件用法。agent 必须能在自己的执行环境中访问 Skill 参考文件和选定仓库状态；本机路径不会自动出现在云端会话中。

例如，从本仓库根目录安装到目标项目的 Codex Skill 目录。请替换目标路径，并确保目标 `unburden` 目录尚不存在：

```sh
mkdir -p /absolute/path/to/target-project/.agents/skills
cp -R skills/unburden /absolute/path/to/target-project/.agents/skills/unburden
```

其他 agent 使用表中对应的父目录。安装是可选的；直接读取文件使用的是同一套审查指令。本仓库提供指令内容，不是厂商专用插件或强制执行沙箱。

## 示例

七个维度均有 Code 案例和 `text/` 对应案例，包括失效引用与超出交付范围的记录。目录名和以下表格使用当前维度名称。

每组示例包含 **`base/` 和 `candidate/` 仓库快照**、预期 `findings.md`、更合理的 `improved.py` 或 `improved.md`、相似但不应误报的 `non_finding.py` 或 `non_finding.md`，以及说明契约的 README。Code 快照包含 `example.py`；指令与记忆快照包含 `SKILL.md` 或 `MEMORY.md`；写作示例使用 `article.md`；回答片段使用 `responses.md`。

比较模式提供两个快照目录，快照模式只提供 `candidate/`，预期报告分别展示两种模式。输入快照包含自己的契约；预期报告和替代版本是输入之外的解释性材料。这些是静态源码示例，不是测试或 benchmark。

| 维度           | Code 示例                                                                  | Text 示例                                                                          |
| -------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| 不必要的特例   | [应用专属字段改写](examples/unnecessary-special-cases/README.md)           | [项目记忆变成全局流程](examples/unnecessary-special-cases/text/README.md)          |
| 冗余逻辑与规则 | [不可达排除检查与多余后缀](examples/redundant-logic-and-rules/README.md)   | [已排除输入仍有恢复指令](examples/redundant-logic-and-rules/text/README.md)        |
| 评测专用捷径   | [依赖框架标识的固定计数](examples/evaluation-specific-shortcuts/README.md) | [按 case ID 绕过计数的指令](examples/evaluation-specific-shortcuts/text/README.md) |
| 环境耦合       | [本地路径覆盖配置](examples/environment-coupling/README.md)                | [个人 checkout 替换目标仓库](examples/environment-coupling/text/README.md)         |
| 实现耦合       | [导出器读取私有存储](examples/implementation-coupling/README.md)           | [指令绕过公共 provider 方法](examples/implementation-coupling/text/README.md)      |
| 不必要的泛化   | [固定问候语的无用调度](examples/unnecessary-generalization/README.md)      | [固定流程的无用状态维护](examples/unnecessary-generalization/text/README.md)       |
| 过时资产 | [指向已删除评测器的 hook](examples/stale-artifacts/README.md) | [发布包中的失效指南与内部记录](examples/stale-artifacts/text/README.md) |

写作案例包括[重复限定示例](examples/redundant-logic-and-rules/text/writing/README.md)和[无关否定对比示例](examples/redundant-logic-and-rules/text/unnecessary-contrasts/README.md)：介绍图片压缩工具时，先说“不是图片编辑器，不是素材管理平台，而是图片压缩工具”。两组均包含比较与快照报告、最小建议，以及应当保留的有意义对比。它们归入“冗余逻辑与规则”，不另增维度或输入类型。依据是上下文中可证明重复或无关的论述，不按句式判错，也不推测写作历史。

[回答中的不必要限定示例](examples/redundant-logic-and-rules/text/unnecessary-qualifications/README.md)覆盖无端升级主张、无关免责声明、臆造例外和无依据降格表述，仍归入“冗余逻辑与规则”。仓库快照提供请求及上下文，不要求额外的对话历史；反例保留必要限定和有用的强调。“本文不声称”“值得注意的是”“需要指出的是”等短语本身不构成问题。

数字边界由捷径案例中的预置计数，以及 [Code 非问题案例](examples/evaluation-specific-shortcuts/non_finding.py)中的合理内核阈值共同说明。Text 非问题案例还覆盖限定范围的事实、事件引用、few-shot 示例、不同条件的验证、明确的平台契约、具体实现的维护流程，以及确有用途的可选交付模式。

[没有发现问题的完整报告](examples/redundant-logic-and-rules/no_findings.md)复用现有 Code 非问题案例，展示限定范围的快照审查如何说明目标、实际覆盖内容及结果的适用边界。

## 审查范围与组合使用

Unburden 在选定仓库内容中检查[七个维度](#七个审查维度)，不要求或推断内容来源。

它不全面覆盖功能正确性、安全性、并发、资源管理、兼容性、领域或数学正确性、记忆事实真实性及 Skill 格式合规。问题可以在这些方面产生后果，但无关缺陷仍属于其他审查范围。评测专用捷径不是测试覆盖率审查。静态阅读也不衡量 Skill 是否好用或记忆是否能有效检索。文章审查聚焦有证据的冗余对比与限定，保留实质性比较和必要的局限说明，不承担全面语法润色或学术同行评审。

需要更广覆盖时，可以组合通用代码审查工作流和相关专项能力。Unburden 也可以独立使用，不要求配套项目。

```text
对同一个 Candidate 仓库使用通用代码审查 Skill 和 Unburden，
共用相同的可选 Base 和选定范围。
通用审查检查功能正确性，Unburden 检查七类机制。
标明问题由哪类审查支持，并合并重复 findings。
只输出 findings 和最小建议，不修改、不运行测试或 benchmark。
```

各项审查遵守自己的证据标准。Unburden 不自动安装或调用其他 Skill，不扩展范围，也不要求先完成更全面审查。干净的 Unburden 报告不表示仓库整体通过审查。

### 推荐搭配项目

以下四个项目提供可选的配套审查能力。描述依据各项目公开指令，选择基于范围互补，而非审查效果排名。它们都不是 Unburden 的内置组件或必需依赖。

| 项目                                                                                                                                        | 适合补充的审查范围                                                                                                                | 使用边界                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| [adversarial-code-review](https://github.com/contrueCT/adversarial-code-review)                                                             | 更广泛地检查需求一致性、逻辑、安全、数据完整性、并发、兼容性和测试可信度；也与范围控制及过度设计检查重叠。                        | 它按风险调整审查深度，包含验证和额外审查流程。应与 Unburden 的静态审查区分，并遵守本次请求的执行限制。 |
| [Anthropic pr-review-toolkit](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/pr-review-toolkit)                    | 通过专项 Agent 检查代码质量、错误处理、类型设计、注释和测试覆盖，尤其适合 Claude Code。                                           | 按需选择审查 Agent。其中 code-simplifier 还支持重构；仅要求 findings 不表示授权自动修改。              |
| [reviewing-code-modularity-skill](https://github.com/tyshkovskii/reviewing-code-modularity-skill)                                           | 检查模块边界、耦合、内聚、公共 API，以及抽象是否解决当前问题；与 Implementation Coupling 和 Unnecessary Generalization 存在重叠。 | 只需要 findings 时使用 fast review 模式。其设计和实施模式超出了单纯审查，可能涉及重构与验证。          |
| [avoid-overdefensive-programming](https://github.com/aravelo7/codex-agent-skills/blob/main/skills/avoid-overdefensive-programming/SKILL.md) | 检查无依据的 fallback、吞异常、重试、默认值和兼容分支，同时保留合理防护；与部分冗余和残留逻辑检查重叠。                           | 它也包含编码、修复、修改及验证步骤。只读审查应保持为问题报告，不能因启用它而自动修改代码或新增测试。   |

需要更广覆盖时，可从前两项选择一个通用审查搭配；遇到明确的模块或防御逻辑问题，再按需增加后两项专项能力。共用同一个 Candidate 仓库、可选 Base 及选定范围，标明各审查的依据并合并重复问题。使用前查看配套项目的当前指令，选择兼容模式；Unburden 保持静态审查和只给建议的范围。

## 贡献

保持静态、基于仓库的审查，遵守选定模式与范围。贡献应澄清证据规则，或提供包含合理相似情况的完整 Code／Text 示例。保留七个维度和建议中的预期行为，不增加强制 Base、任务说明、产生历史、测试用例、执行实验或 findings 数量要求。

## 许可证

[MIT](LICENSE)。
