# CLAUDE.md — 本站内容铁律（AI 每次会话自动加载，必须遵守）

> 本文件由项目所有者维护。Claude Code 每次启动自动读取本文件，无需提醒。
> 违反本文件规则的输出 = 不合格，会被打回重写。

## 🚨 第一条：内容必须"攻略化"，禁止"笔记化"

**目标读者是玩家**：他们打开页面是为了学到"怎么玩"，不是读你的资料总结。

### ❌ 禁止（笔记腔/论文脚注腔——一票否决，全部打回）
- "The supplied material lists 15 firearms..."
- "Reference notes indicate that..."
- "According to the provided sources..."
- "It is noted that..."
- "The supplied references divide melee weapons into..."
- 任何"根据资料/来源显示"的转述腔调
- 任何"这个系统存在，但不展开"的干瘪说明

### ✅ 必须（攻略腔——直接教玩家怎么玩）
- 直接写武器/机制本身："The M781 is the best all-round firearm..."
- 用**第二人称**："You should... / When you... / If you find..."
- 每个条目给出**具体怎么用/强在哪/弱在哪/什么场景用**
- 大量使用**表格**列数据（武器表：武器|评级|弹匣|特点|适用场景）
- 玩家视角："This is why... / This matters because..."

### 正反例对照（每个页面写完自查）

**❌ 反例（笔记腔）：**
> "The supplied references divide melee weapons into Blunt and Edged categories and note charged attacks."

**✅ 正例（攻略腔）：**
> "Melee weapons fall into two families. Blunt weapons like the mallet and wrench trade speed for stopping power — great for knocking zombies down in a tight hallway. Edged weapons like the cleaver and machete slice limbs off to slow the horde. The baseball bat tops both: fast, stamina-friendly, and it staggers enemies so you can reposition."

## 🚨 第二条：素材必须"展开"，禁止"要点清单当全文"

素材文件里每个要点 = 正文里的**一整段**（3-4句），不是一句话带过。
- 素材列了17个技能 → 正文要写成**技能表格**（技能名|效果|适用场景）
- 素材列了11把远程武器 → 正文要写成**武器表格+逐把点评**
- 素材给了地图任务链 → 正文要写成**分步攻略**（第1步做什么→第2步→…）

**判断标准：** 素材里出现过的每个具体数据/武器/机制，正文必须都有对应展开。遗漏 = 打回。

## 🚨 第三条：页面必须能"落地用"

写完每个页面，问自己："一个第一次玩的玩家看完这页，能不能直接上手？"
- 能 → 合格
- 只是"知道了有这个系统" → 不合格，重写

## 其他（继承自 SPEC 的底线）

- 禁词：待确认/coming soon/No official/unconfirmed/未找到
- 禁编造：素材没有的数据（官方数值/帧率）→ 写"玩家实测参考"或"官方未公布"
- 版本标注：EA旧素材写 "as of 1.0 launch, may differ"
- 每页：title≤60字符 / description 140-160 / H1唯一 / 4-6个H2
- 宁短勿水 ≠ 不展开——素材够的必须写够，素材不够才宁短
