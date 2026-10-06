<div align="center">

# LydiaHub

<img src="assets/hero.svg" alt="LydiaHub · Turn an idea into something useful" width="100%">

> **I turn those “surely I shouldn't have to struggle with this again” moments at work into small tools you can actually use.**
>
> Start with one specific problem. Build something usable. Improve it with real feedback.

[![Free tools](https://img.shields.io/badge/Basic_tools-Free-2ea44f?style=flat-square)](https://afdian.com/a/lydiahub2026)
[![Local first](https://img.shields.io/badge/Local--first-By_design-6f42c1?style=flat-square)](#what-matters-to-me)
[![Latest release](https://img.shields.io/badge/Download-Say_It_Plainly_v0.9.0-0969da?style=flat-square)](https://github.com/lydiahub19921013/shuorenhua/releases/latest)

[Find your tool](#choose-by-the-problem) · [Downloads & early access](#downloads--early-access) · [Recent updates](#recent-updates)

Team products I contribute to: [BFTOOLS](https://github.com/mercedesbestsupplier-maker#products) · [Portfolio](https://github.com/lydiahub2026)

</div>

---

<a id="按你现在卡住的事来选"></a>

## Choose by the problem

| What is getting in your way? | Tool | What it helps you do | Current status |
| --- | --- | --- | --- |
| You understand every word of a long message, but still don't know what you're being asked to do | [Say It Plainly](https://github.com/lydiahub19921013/shuorenhua/blob/main/README.en.md) | Identify actions and questions, then draft a reply that reflects what you actually mean | macOS v0.9.0; download available; Chinese interface |
| A client's “small change” keeps growing, and nobody can say how much extra work it adds | [Scope Check](products/biefangong/README.md) | Compare a new request with the agreed scope; spot additions, changes, and unanswered questions | macOS v0.1.0; private testing; Chinese interface |
| Ideas and tasks disappear while you switch between apps | [Desktop Flow](https://afdian.com/album/1f24622aa83511f184a452540025c377) | Catch them on your desktop, save as Markdown, and connect to Obsidian or Codex when useful | macOS v1.0.0; Windows v1.0.3 |
| You spend hours in Codex and want a workspace that feels more like yours | [Codex Skin Workshop](https://afdian.com/album/26288eaca83511f19cc352540025c377) | Search, preview, install, switch, and restore skins | macOS; free access; original app by [@luhaozwork](https://github.com/luhaozwork), my enhancements and skins |
| Every new content topic sends you back through the same research and sorting steps | [Xiaoran Topic Assistant](https://afdian.com/a/lydiahub2026) | Put repeated research steps into a workflow, leaving the judgment to you | Released; see the access page |
| Inquiries sit in a spreadsheet, with no clear priority or next step | [Lydia Foreign Trade System](https://github.com/lydiahub19921013/lydia-foreign-trade-system) | Import CSV or JSON; review grades, missing evidence, and next actions before confirming follow-up | MIT; local setup with Node.js 20+ |
| You want to check dimensions, volume, and bag counts before buying landscape materials | [CoverCalc Pro toolkit](https://github.com/lydiahub19921013/covercalcpro-landscape-quantity-kit) | Check rectangular or circular volumes, formulas, pack sizes, and shopping quantities | MIT; browser checker / [live calculator](https://covercalcpro.com/#calculator) |
| A browser agent times out, loses its place, or submits twice, and you can't tell what happened | [Browser Agent Blueprint](https://github.com/lydiahub19921013/browser-agent-blueprint) | Reuse prompt modules and run a real local browser against a synthetic page to inspect checkpoints, risk gates, and resume boundaries | MIT; 12 modules, 4 workflow templates, 6 demo scenarios; model integrations not tested |

New here? Open the [getting-started page](GETTING-STARTED.md). Pick the problem you recognize and try one tool.

---

## Two products I'm focusing on

### Say It Plainly · Understand the message, then reply in your own words

“Find a lever for user value and close the loop quickly.” You know the words. The hard part is figuring out what to do first, how far to take it, and how to reply without pretending the request was clear.

Say It Plainly breaks a message into actions and the questions worth checking, then drafts a reply around what you actually mean. It checks for added promises about timing, scope, responsibility, or guarantees. The draft goes back into your chat input; you review it before sending.

**[Product and v0.9.0 downloads](https://github.com/lydiahub19921013/shuorenhua)** · [English overview](https://github.com/lydiahub19921013/shuorenhua/blob/main/README.en.md)

### Scope Check · Make the extra work clear before doing it

To a client, it may be “just add a mobile version.” For the person doing the work, it can change the pages, APIs, tests, and delivery date together.

Scope Check keeps the agreement currently confirmed for each project. Paste a new client message and it highlights additions, changes to the agreement, and details that need clarification before work starts. It also drafts a calm confirmation reply that doesn't commit you in advance.

<img src="assets/biefangong-v0.1.0.png" alt="Scope Check v0.1.0 running in its current Chinese interface" width="520">

**[Features and testing status](products/biefangong/README.md)**

---

## Open-source projects · See the code and try it yourself

### Browser Agent Blueprint · A lost receipt calls for verification before retrying

A browser agent clicks Save and times out. If it clicks again after restarting, it may create a duplicate record. This project records verified actions, uncertain submissions, and remaining budgets separately: 12 original plain-text prompt modules, 4 workflow templates, and a real local browser demo. Two separate processes let you check that the saved-record count remains 1 after resume.

The demo uses deterministic host code and makes no model calls. Muse, Grok, and Codex have integration contracts; those model integrations have not been live-tested. Automatic wake-up and production crash consistency need host support. The repository explains its scope and provenance.

**[Modules and reproducible demo](https://github.com/lydiahub19921013/browser-agent-blueprint)** · [Getting started](https://github.com/lydiahub19921013/browser-agent-blueprint#quick-start) · [Report a synthetic failure case](https://github.com/lydiahub19921013/browser-agent-blueprint/issues)

### Lydia Foreign Trade System · Sort the inquiries before deciding who to follow up with

Start with an inquiry sheet you already have. Check the columns before importing, then review A / B / C / D / HOLD grades, missing evidence, and next actions. When evidence is missing, look up public company information as needed. Keep customer groups separate and export important batches as complete backups.

The interface and screenshots use fictional examples, not actual customers or sales results. It runs locally by default and does not send bulk messages. Local data is not encrypted; the project explains its use boundaries.

**[Project and real screenshots](https://github.com/lydiahub19921013/lydia-foreign-trade-system)** · [English getting started](https://github.com/lydiahub19921013/lydia-foreign-trade-system/blob/main/docs/README.en.md) · [Report an issue](https://github.com/lydiahub19921013/lydia-foreign-trade-system/issues)

### CoverCalc Pro · Check the quantities before placing an order

Measured length, width, and depth tell you how much space to fill. The volume printed on a bag tells you how many bags to buy. This toolkit keeps the two calculations separate. Check rectangular or circular spaces and inspect the formulas, field definitions, and coverage CSV.

The single-area checker is an HTML file you can open directly in a browser, without an account or third-party dependencies. The full live calculator is at covercalcpro.com. Repository examples don't guess prices, densities, or supplier rules.

**[Open the live calculator](https://covercalcpro.com/#calculator)** · [Toolkit and demo](https://github.com/lydiahub19921013/covercalcpro-landscape-quantity-kit) · [Try the local checker](https://github.com/lydiahub19921013/covercalcpro-landscape-quantity-kit/blob/main/docs/TRY-IT.md)

---

## Other work I keep improving

- **Desktop Flow:** keep a fleeting task or idea on your desktop, then move it into Obsidian, Codex, or a review workflow when useful.
- **Codex Skin Workshop:** make a daily workspace more comfortable, with a way to restore the original appearance. [@luhaozwork](https://github.com/luhaozwork) developed the original app; I contribute feature enhancements and a collection of several hundred skins.
- **WorkBuddy Digital Employee Workbench:** turn repeated research, topic selection, formatting, and checking into workflows you can run.
- **Echo:** make room for conversations about life stages, choices, and relationships that you can return to later.
- **AI Cost Copilot:** see where API costs go before choosing models and assembling workflows.

Projects without a public download are labeled in development or in testing. A local build is a different state from a public release.

I also work with the [BFTOOLS team](https://github.com/mercedesbestsupplier-maker) on product direction, user experience, and public product pages, with a current focus on promoting the content-operations tool. [BFTiles](https://github.com/mercedesbestsupplier-maker/BFTiles) was originally developed by [@dingzd1995](https://github.com/dingzd1995).

<a id="我做产品时守的边界"></a>

## What matters to me

- **Start with a real task.** Make one specific thing work well before adding more features.
- **Keep data local when practical.** Projects, agreements, and records that can stay on your computer aren't uploaded by default.
- **Keep key decisions yours.** Replies are reviewed before sending; project scope changes after your confirmation.
- **Be honest about status.** Tests, device verification, signing, notarization, and public release are reported separately.

<a id="下载与内测"></a>

## Downloads & early access

- [Lydia Foreign Trade System: source and setup](https://github.com/lydiahub19921013/lydia-foreign-trade-system)
- [CoverCalc Pro: live calculator](https://covercalcpro.com/#calculator) / [formulas and local checker](https://github.com/lydiahub19921013/covercalcpro-landscape-quantity-kit)
- [Say It Plainly: latest download](https://github.com/lydiahub19921013/shuorenhua/releases/latest)
- [Afdian: tools and updates](https://afdian.com/a/lydiahub2026)
- [Feishu: free product collection](https://jcnrbes3t04e.feishu.cn/drive/folder/VRnafPFVDlcNXrdtpSwcWaWFnEj)
- Bugs and feature ideas: open an Issue in the relevant public repository.
- Early access, custom work, and maintenance: WeChat `lydiahub2026`.

Basic tools will continue to be shared for free. Custom features, deployment help, data migration, and ongoing maintenance can be discussed separately. Some linked interfaces and distribution pages currently use Chinese.

## Find me online

[Facebook · Mercedes Costa](https://www.facebook.com/people/Mercedes-Costa/100074622692401/) · [Quora · MercedesCosta](https://www.quora.com/profile/MercedesCosta) · [TikTok · @covercalcpro](https://www.tiktok.com/@covercalcpro) · [X · MA HIBBERD](https://x.com/LRosamarina)

<a id="最近更新"></a>

## Recent updates

- **2026-10-06:** added Browser Agent Blueprint: original browser-agent prompt modules, a local resume demo, and integration contracts clearly labeled as not live-tested.
- **2026-09-28:** added project links, setup guides, and demos for Lydia Foreign Trade System and the CoverCalc Pro toolkit; linked the English overview for Say It Plainly while keeping existing products, covers, and downloads.
- **2026-09-08:** Scope Check reached its v0.1.0 testing candidate, identifying added work, changed agreements, and questions needing confirmation.
- **2026-09-07:** Say It Plainly v0.9.0 became available through GitHub Releases.
- **2026-09-04:** Desktop Flow updated to Windows v1.0.3, with its core workflow verified on Windows 10 and 11; Mac uses the v1.0.0 DMG.
- **2026-09-04:** reorganized the Afdian page around Desktop Flow, Codex Skin Workshop, and the combined product entry.

---

**A good tool helps you guess less, redo less, and save your energy for the decisions that need you.**
