---
name: academic-writing-polish-eng
description: 用 Xiaowei Wang 的工程论文与署名修订证据起草或审校 SCI 英文，适用于写作、最小润色、深度编辑、比较版本及全文一致性检查，也用于综述图、概念框架图和信息示意图的设计、审阅与版本取舍。
---

图示任务先判断读者应从图中得出什么结论。用 references/figure-rhetoric-and-visual-logic.md 选主轴与次级关系，再用 references/author-figure-design-preferences.md 的 V01–V07 决定保留、补充、移位或删减。比较版本时回查 references/author-figure-revision-casebook.md；定稿前按 references/author-visual-negative-preferences.md 审查负担与例外。只润色文字时跳过图示模块。

先锁定科学对象、比较基线、数据、符号、引用和论断边界，再确定任务和章节。用 references/author-editing-decision-rules.md 找当前文本实际触发的诊断；同时用 references/section-writing-patterns.md 和 references/author-style-profile.md 选择适宜的英文表达。按需核对 references/lexical-and-syntactic-patterns.md 和 references/argumentation-and-rhetoric.md。编辑规则解释修改方向，已发表语料解释表达选择。两者冲突时检查语境、证据与归属，优先保持科学含义。

起草只用用户提供的事实。最小润色允许原样返回；深度审校将语言修改与待作者确认的分析、机制和数据缺口分开。比较版本先判语义，再以 references/style-evidence.md 或 references/author-revision-casebook.md 解释偏好，证据不足允许并列。全文一致性检查按位置报告术语、图表、变量和证据范围，保留自然变化。

先决定保留、局改、拆并或重组，再成稿。用 references/author-negative-preferences.md 针对已触发的问题复查，最后按 references/editing-checklist.md 审核保真。默认英文在前，随后中文简述必要理由，重大歧义单列。

更新已发表语料时运行 scripts/import_corpus.py，按 references/corpus-manifest.md 管理版本。更新带批注稿时将源文件只读置于分析目录，运行 scripts/inspect_docx.py；参照 references/revision-evolution-analysis.md 按论文、段落主题及批注锚点去重，更新案例后才调规则。不能从版本差异断定修改者。复测见 references/validation.md。用户偏好和临时要求单独处理。
