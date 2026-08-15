# No More Room in Hell 2 Wiki — 建站SPEC（v1.0）

> **执行模式声明：** 直接按本SPEC执行，无需计划/提问/确认。完成所有页面后一次性汇报。
> **允许提问的3种情况：** ①SPEC自相矛盾 ②技术不可行 ③无法绕过的禁止项。
> **对标站：** 无（使用AnvilWiki模板自带UI，只换主题色；布局参考 hell-let-loose.wiki 的"数据条横排+卡片网格多列"风格，AI自己F12看）
> **模板来源：** https://github.com/leyang866-debug/AnvilWiki （clone后按本SPEC改造）

---

## 一、项目信息

| 项 | 值 |
|:----|:----|
| 游戏 | No More Room in Hell 2 |
| 类型 | 8人合作丧尸生存FPS（PVE） |
| 发售 | 2026-08-11（1.0正式版Armageddon，EA从2024-10-22） |
| 价格 | $29.99（⚠️ $19.49是旧折扣价，别写错） |
| 开发商/发行 | Torn Banner Studios |
| 引擎 | Unreal Engine 5 |
| 平台 | PC/PS5/Xbox Series X\|S（1.0首次登主机） |
| 域名 | nomoreroominhell.online（已购买） |
| GitHub | leyang866-debug/nmrih2-wiki |

## 二、技术栈（AnvilWiki模板）

- Astro 5 + Content Collections（MDX）+ Cloudflare Pages
- 模板自带：JSON驱动首页 / 多语言 / SEO工程化 / AdSense就绪 / 套模板CLI
- **多语言：** `src/i18n/routing.ts` 的 locales 改为 `['en', 'vi', 'de', 'fr', 'es']`
  - 英文无前缀（SEO最优），其他语言带前缀（/vi/ /de/ /fr/ /es/）
  - **首版翻译范围：** 英文全站 + 其他语言先做**首页+weapons页**，其余自动fallback英文（模板自带）
- **换肤（丧尸恐怖绿/暗色调）：** `src/styles/globals.css` 只改 `--brand` 变量
  - `--brand: 90 35% 30%;`（暗丧尸绿）
  - `--brand-h: 90; --brand-s: 35%;`
  - 暗色为默认主题

## 三、站点配置（src/config/site.ts）

```ts
name: 'No More Room in Hell 2 Wiki'
shortName: 'NMRIH2'
description: 'No More Room in Hell 2 guide — weapons, perks, maps, survival mode, infection, solo training, crossplay and 1.0 updates.'
domain: 'nomoreroominhell.online'
game: {
  name: 'No More Room in Hell 2',
  platform: 'PC/PS5/Xbox Series X|S',
  developer: 'Torn Banner Studios',
  publisher: 'Torn Banner Studios',
  genre: 'Co-op Survival Horror FPS',
  releaseDate: '2026-08-11'
}
social: {
  official: 'https://www.nmrih2.com/',
  discord: 'https://discord.com/servers/no-more-room-in-hell-211900829307895819',
  youtube: 'https://www.youtube.com/channel/UCygSSHjXjhLdPeDf1SDXqHw',
  reddit: 'https://www.reddit.com/r/nmrih/',
  twitter: 'https://x.com/nmrih'
}
```

## 三-b、Logo与媒体（写死）

- **Logo：** 项目 `logo/` 目录（favicon.ico/apple-touch-icon/android-chrome-192/512/webmanifest 全套已就位）——必须用，禁AI自己生成
- **图片：** 项目 `images/` 目录（**5张已就位**：1.jpg + 2-4.webp + 5.jpg）——**每页至少1图**，内页也要插图，路径写死 `/images/1.jpg` 等
- **视频：** 官方 Reanimation++ 预告 `BIb-UF_k6F0`（videos/youtube_id.txt）——首页Hero下方嵌入iframe（非链接）
- **禁：** AI自己找图/外部图床/自己生成logo

## 四、SEO（每页必须）

- 页面 title 含关键词且 ≤60字符
- meta description 含关键词且 140-160字符
- **H1只有一个**（含主关键词），H2分小节
- 开头100字内直接回答玩家搜索问题（不写"Welcome to..."）
- 正文：结论先行 → 分H2小节 → 每段3-4句可扫读
- URL slug 用关键词（如 /weapons-tier-list）
- 文章末尾加"相关文章"内链

## 五、页面↔素材映射表（写每页前先读对应素材！）

| 页面 | 必读素材文件 | 必写要点 |
|:----|:----|:----|
| /（首页） | 素材/首页素材.md | 简介/数据表/官方链接/核心玩法/新手4卡/1.0更新 |
| /weapons | 素材/nmrih2 weapons.md + weapons tier list.md + melee tier list.md + perks实测.md(武器部分) | 枪械清单/近战分类/远程Tier(M781榜首)/近战Tier(棒球棒No.1)/附件系统 |
| /weapons-tier-list | 素材/nmrih2 weapons tier list.md + melee tier list.md | 远程Tier表(M781/MP5/M1911)+近战Tier表(棒球棒/消防斧)，标注"community tier list based on 1.0" |
| /perks | 素材/nmrih2 perks.md + perks实测.md | 1.0技能大改(新增3Reloading/移除3)+实测17技能表(升级3选1)+重Roll成本降低 |
| /characters | 素材/nmrih2 characters.md + perks实测.md(角色部分) | Responder体系/3初始角色(Crackle/Bluff/Twilight)/背景决定技能/Permadeath |
| /maps | 素材/nmrih2 maps.md + 评测+Broadway流程.md | 6 Objective图+3 Survival图/Raven Rock新图/Broadway任务链(电力→收音机→硬盘→安全屋→撤离) |
| /survival-mode | 素材/首页素材.md(1.0更新) + 1.0状态评测.md | Survival模式机制(保护Speaker/5分钟/3波/直升机撤离)+3专属图 |
| /solo | 素材/nmrih2 solo.md | Solo Training模式(无成长/无永久死亡/练图练武器) |
| /tips | 素材/nmrih2 tips.md + 新手10须知.md | 15条1.0技巧+10条须知(噪音/感染/资源分享/卸弹) |
| /infection | 素材/首页素材.md(感染部分) + 新手10须知.md + perks实测.md | 感染信号(咳嗽/触手/幻听)/pills/gene therapy/变丧尸/防感染 |
| /crossplay | 素材/nmrih2 crossplay.md + is_cross_platform.md | 全平台互通(PC/PS5/Xbox)/8人合作/FAQ |
| /ps5 | 素材/nmrih2 ps5.md + ps5实测.md | 主机版首发/价格$29.99/60FPS目标/跨平台/故障排查FAQ |
| /xbox | 素材/nmrih2 xbox.md | Series X\|S版/Play Anywhere/订阅要求/价格 |
| /review | 素材/nmrih2 review.md + 1.0状态评测.md + 评测+Broadway流程.md(8/10) | Mixed评价(21K)/EA负面→1.0好转/玩家8/10/主机问题 |
| /release-date | 素材/nmrih2 release_date.md | 1.0(2026-08-11)/EA(2024-10-22)/22个月EA/首次登主机 |
| /1.0-update | 素材/首页素材.md(1.0更新) + nmrih2 1_0_release.md | Armageddon全内容(Survival/Raven Rock/Solo/Tutorial/主机/Crossplay/技能/难度) |
| /difficulty | 素材/nmrih2 difficulty_levels.md | 4难度(Beginner→Nightmare)/各自差异 |
| /steam-charts | 素材/nmrih2 steam_charts.md + player_count.md + steamdb.md | 实时人数说明(不写死)/历史峰值11K-15K/Owner估算 |

**共18页（首页+17内页）。** 每页：800-1200词 / 4-6个H2 / ≥1图。

## 六、内容规则（必须遵守）

1. **禁待确认词**：待确认/coming soon/No official/unconfirmed/未找到——素材确定的直接写，不确定的不写
2. **禁凑字数**：每句有信息量，禁循环废话
3. **宁短勿水**：素材不够写500词干货+汇报缺什么，不注水
4. **版本标注**：EA旧素材（近战Tier/新手10须知）写"as of 1.0 launch, may differ"；不把EA当1.0
5. **按钮文案**：Browse Guides / Explore the Wiki / Read Guide（禁START YOUR RUN/PLAY NOW宣传腔）
6. **小标题带Guide/Wiki/How to攻略感词**
7. **确定性分级**：官方(Steam/官网/Fandom)✅、媒体⚠️参考、玩家字幕=参考级标注、负面只用于评价页

## 七、验收清单（每项必须实际执行并截图留证）

- [ ] **换肤自检：** 打开首页+1内页截图，确认：背景不是纯白（暗色丧尸氛围）/卡片不是模板白/暗色模式也是暗色系——**与模板默认明显不同**
- [ ] **Logo自检：** 确认 public/ 下的 favicon.ico/apple-touch-icon/manifest 已替换为 logo/ 目录文件（删除模板默认favicon.svg），浏览器标签页图标是新logo
- [ ] **对标布局自检：** 打开 https://hell-let-loose.wiki/ 对比——首页必须出现"数据条横排+卡片网格多列"布局特征，不是模板默认的单列/简单卡片
- [ ] 18页全建（首页+17内页），英文
- [ ] 多语言：首页+weapons 有 vi/de/fr/es，其余fallback
- [ ] 每页≥1图，首页嵌入视频
- [ ] 每页 title≤60字符/description 140-160/H1唯一
- [ ] grep检查：无"待确认/coming soon/No official"
- [ ] 字数：核心页(weapons/perks/maps/tips)≥800词
- [ ] 本地 pnpm dev 跑通，路由全部200
- [ ] 不出现 $19.49（正确价$29.99）

**⚠️ 汇报要求：** 以上每项自检必须**截图留证**（首页截图+内页截图+浏览器标签页图标截图），随最终汇报一起发。不截图=未验收=不能算完成。

## 八、部署（完成后）

- 推GitHub main → site-deploy自动化（Cloudflare Worker + GA4 + GSC + sitemap）
- 域名：用户确认后绑定

## 九、明确不做的事

- ❌ 不做暗色模式/登录/评论/搜索（模板自带除外）
- ❌ 不做广告位/数据库/后端
- ❌ 不写EA旧版内容当1.0（版本标注必须）
